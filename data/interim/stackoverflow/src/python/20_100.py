class De(models.Model):
    ...
    def calculate_s_d(self):
        if self.fr:
            return self.de
        else:
            return self.gd + self.na

    calculate_s_d.admin_order_field = Case(
        When(fr=True, then='s_d'),
        When(fr=False, then=F('gd') + F('na')),
        default=Value(0),
        output_field=IntegerField(),
    )

    s_d = property(calculate_s_d)
