#from django.urls import path
#from .views import BookList

#urlpatterns = [
#    path('books/', BookList.as_view(), name='book-list'),  # URL for accessing the BookList view
#]


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)

# Include the router URLs
urlpatterns = [
    path('', include(router.urls)),  # Include all generated URL patterns
]
