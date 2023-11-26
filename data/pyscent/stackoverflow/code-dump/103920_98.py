class DeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().annotate(
            s_d=Case(
                When(fr=True, then='s_d'),
                When(fr=False, then=F('gd') + F('na')),
                default=Value(0),
                output_field=IntegerField(),
            )
        )


class De(models.Model):
    fr = models.BooleanField("[...]")
    de = models.SmallIntegerField("[...]")
    gd = models.SmallIntegerField("[...]")
    na = models.SmallIntegerField("[...]")
    objects = DeManager()


class DeAdmin(admin.ModelAdmin):
    list_display = ("[...]", "s_d", "gd", "na", "de", "fr" )
