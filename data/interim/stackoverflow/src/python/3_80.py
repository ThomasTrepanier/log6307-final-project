class YearInSchool(models.TextChoices):
    FRESHMAN = 'FR', _('Freshman')
    SOPHOMORE = 'SO', _('Sophomore')
    JUNIOR = 'JR', _('Junior')
    SENIOR = 'SR', _('Senior')
    GRADUATE = 'GR', _('Graduate')

class Student(models.Model):
   year_in_school = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.FRESHMAN,
    )
