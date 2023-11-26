def decorate(**kwargs):
    def wrap(function):
        for name, value in kwargs.iteritems():
            setattr(function, name, value)

        return function
    return wrap

class De(models.Model):

    fr = models.BooleanField("[...]")
    de = models.SmallIntegerField("[...]")
    gd = models.SmallIntegerField("[...]")
    na = models.SmallIntegerField("[...]")
    # [several_attributes, Meta, __str__() removed for readability]

    @property
    @decorate(admin_order_field='_s_d')
    def s_d(self):
        if self.fr:
            return self.de
        else:
            return self.gd + self.na
