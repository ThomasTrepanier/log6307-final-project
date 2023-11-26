# models.py

class De(models.Model):

    fr = models.BooleanField("[...]")
    de = models.SmallIntegerField("[...]")
    gd = models.SmallIntegerField("[...]")
    na = models.SmallIntegerField("[...]")
    s_d = models.SmallIntegerField("[...]", blank=True)

    # [several_attributes, Meta, __str__() removed for readability]

    def save(self, *args, **kwargs):
        if self.fr:
            self.s_d = self.de
        else:
            self.s_d = self.gd + self.na
        super().save(*args, **kwargs)

# admin.py

class DeAdmin(admin.ModelAdmin):
    list_display = ("[...]", "s_d", "gd", "na", "de", "fr" )
