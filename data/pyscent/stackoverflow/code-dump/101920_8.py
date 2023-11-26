import random

class De(models.Model):

    fr = models.BooleanField("[...]")
    de = models.SmallIntegerField("[...]")
    gd = models.SmallIntegerField("[...]")
    na = models.SmallIntegerField("[...]")
    # [several_attributes, Meta, __str__() removed for readability]

    def s_d(self):
        """
        Just as example: adds a perturbation so it is not possible
        to inherit ordering by db columns
        """
        X = random.randrange(128)
        if self.fr:
            return self.de*X
        else:
            return self.gd*X + self.na
    s_d.admin_order_field = 'cielcio_to_be_removed'
    s_d = property(s_d)
