from django.db import models


class Bundle(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Bundle"
        verbose_name_plural = "Bundles"

    def __str__(self):
        return self.name


class Opportunity(models.Model):
#    bundle = models.ForeignKey("Bundle", models.CASCADE, blank=True, null=True)
    bundle = models.ForeignKey("Bundle", models.CASCADE, blank=True, null=True, related_name='opportunities')
    name = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        verbose_name = "Opportunity"
        verbose_name_plural = "Opportunities"

    def __str__(self):
        return self.name
