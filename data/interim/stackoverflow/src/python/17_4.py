import docs.models

class WizardConfig(models.Model):
    tenant = models.ForeignKey(Tenant, null=False, blank=False, on_delete=models.CASCADE)
    consent1 = models.ForeignKey(docs.models.DocLib, null=True, blank=True, on_delete=models.CASCADE,related_name='consent1')
