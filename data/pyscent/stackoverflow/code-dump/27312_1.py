from django.db import models
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce

# Create your models here.
class AuthorQuerySet(models.QuerySet):
    def annotate_with_copies_sold(self):
        return self.annotate(copies_sold=Coalesce(Sum('books__copies_sold'),Value(0)))

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    objects = AuthorQuerySet.as_manager()

class Book(models.Model):
    title = models.CharField(max_length=30)
    copies_sold = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
