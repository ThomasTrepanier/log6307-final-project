class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=40, blank=True)
    phone = models.IntegerField()
