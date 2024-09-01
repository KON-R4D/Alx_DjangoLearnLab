from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Use BookSerializer to serialize the data
