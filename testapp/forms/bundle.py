from django.forms import fields, widgets
from django.forms.models import ModelForm

from formset.collection import FormCollection

from testapp.models.bundle import Bundle, Opportunity


class OpportunityForm(ModelForm):
    id = fields.IntegerField(
        required=False,
        widget=widgets.HiddenInput,
    )

    class Meta:
        model = Opportunity
        fields = ['id', 'name']


class OpportunityCollection(FormCollection):
    min_siblings = 0
    extra_siblings = 1
    team = OpportunityForm()
    legend = "Opportunities"
    add_label = "Add Opportunity"
    related_field = 'bundle'

    def retrieve_instance(self, data):
        if data := data.get('opportunity'):
            try:
#                return self.instance.opportunity_set.get(id=data.get('id') or 0)
# uncomment the above line and comment the below line to see the issue
                return self.instance.opportunities.get(id=data.get('id') or 0)
            except (AttributeError, Opportunity.DoesNotExist, ValueError):
                return Opportunity(name=data.get('name'), bundle=self.instance)


class BundleForm(ModelForm):
    class Meta:
        model = Bundle
        fields = '__all__'


class BundleCollection(FormCollection):
    bundle = BundleForm()
    opportunities = OpportunityCollection()
