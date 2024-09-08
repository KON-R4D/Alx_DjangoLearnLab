from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# BookSerializer serializes Book model fields and includes custom validation.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Validates that the publication year is not set in the future.
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer serializes the Author model and includes related books.
class AuthorSerializer(serializers.ModelSerializer):
    # Uses a nested serializer to include all related books of an author.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
