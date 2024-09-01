#from rest_framework import generics
#from .models import Book
#from .serializers import BookSerializer

# Create your views here.
#class BookList(generics.ListAPIView):
#    queryset = Book.objects.all()  # Retrieve all books from the database
#    serializer_class = BookSerializer  # Use BookSerializer to serialize the data


# Update the View with a ViewSet
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all Book objects from the database
    serializer_class = BookSerializer  # Use BookSerializer for data serialization
