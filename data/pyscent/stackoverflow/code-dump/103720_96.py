class De(models.Model):

    fr = models.BooleanField("[...]")
    de = models.SmallIntegerField("[...]")
    gd = models.SmallIntegerField("[...]")
    na = models.SmallIntegerField("[...]")
    # [several_attributes, Meta, __str__() removed for readability]

    def s_d(self):
        if self.fr:
            return self.de
        else:
            return self.gd + self.na
    s_d.admin_order_field = '_s_d'
    s_d = property(s_d)
