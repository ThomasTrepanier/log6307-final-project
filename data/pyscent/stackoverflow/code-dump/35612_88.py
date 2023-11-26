from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce


class AuthorManager(models.Manager):
    def get_queryset(self):
        return AuthorQuerySet(self.model, using=self._db)

    def annotate_with_copies_sold(self):
        return self.get_queryset().annotate_with_copies_sold()


class AuthorQuerySet(models.QuerySet):
    def annotate_with_copies_sold(self):
        return self.annotate(copies_sold=Sum('books__copies_sold'))


class Author(models.Model):
    objects = AuthorManager()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Book(models.Model):
    title = models.CharField(max_length=30)
    copies_sold = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')