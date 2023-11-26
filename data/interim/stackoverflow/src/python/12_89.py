class AuthorQueryset(models.QuerySet):
    def total_copies_sold(self):
        ...

class Author(models.Model):
    objects = models.Manager.from_queryset(AuthorQueryset)()
