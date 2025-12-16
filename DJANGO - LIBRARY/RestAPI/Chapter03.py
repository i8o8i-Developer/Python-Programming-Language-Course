# Posting API on DJANGO REST Framework :
'So far we have created models and migrated them to the database. Now, we will create a REST API to interact with these models using Django REST Framework. Follow the steps below to create a simple API for a Book model.'

# serializers.py
from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# views.py
from rest_framework import viewsets # or from rest_framework.viewsets import ModelViewSet 
from .models import Book
from .serializers import BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# admin.py
from django.contrib import admin
from .models import Book
admin.site.register(Book)

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter # Or from rest_framework import routers
from .views import BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)

'Option 1: Using include'
urlpatterns = [
    path('', include(router.urls)),
]
'Option 2: Directly Using router.urls'
# urlpatterns += router.urls

# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'Your_App_Name',
]

# Migrate And Run The Server
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver

#------------------------------------------------------------

'Segregating Into Different Pages : Post List API' # Which Is Pagination In Django REST Framework

# So What Is Pagination ?
'Pagination Is The Process Of Dividing A Large Set Of Data Into Smaller, Manageable Chunks Or Pages. In Web Applications, Pagination Is Commonly Used To Improve Performance And User Experience By Limiting The Amount Of Data Displayed At Once. Instead Of Loading All Records From A Database In A Single Request, Pagination Allows The Server To Send Only A Subset Of Records, Reducing Load Times And Bandwidth Usage.'

# settings.py
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,  # Number Of Items Per Page
}

# views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Pagination Is Automatically Applied Based On settings.py Configuration
# Now, When You Access The Book API EndPoint, The Results Will Be Paginated.
# Example API Request: GET /books/
# Example API Response:
'''
{
    "count": 50,
    "next": "http://example.com/api/books/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Book Title 1",
            "author": "Author Name",
            ...
        },
        ...
    ]
}
'''
# You Can Navigate Through Pages Using The "Next" And "Previous" Links Provided In The Response.

' Modifying The Pagination Style'
# views.py
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination  # Apply It Here

#------------------------------------------------------------