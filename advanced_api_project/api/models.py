from django.db import models

# Create your models here.


# The Author model represents a book author with a simple name field.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# The Book model represents a book, linking back to an author with a foreign key.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
