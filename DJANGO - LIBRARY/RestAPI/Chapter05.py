# Filtering In QuerySets
'''====================
In Django, Filtering Is A Powerful Way To Retrieve Specific Records From The Database Based On Certain Conditions. The `filter()` Method Is Used On QuerySets To Apply These Conditions. Here Are Some Common Examples Of Filtering In QuerySets:'''

# views.py
from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db.models import Q

def filter_books(request):
    # Example 1: Filter Books By Author Name
    books_by_author = Book.objects.filter(author__name='John Doe')

    # Example 2: Filter Books Published After A Certain Year
    books_after_year = Book.objects.filter(publication_year__gt=2010)

    # Example 3: Filter Books With A Specific Genre
    books_in_genre = Book.objects.filter(genre='Science Fiction')

    # Example 4: Complex Filtering Using Q Objects
    complex_filter = Book.objects.filter(
        Q(author__name='Jane Smith') | Q(publication_year__lt=2000)
    )

    data = {
        'books_by_author': serialize('json', books_by_author),
        'books_after_year': serialize('json', books_after_year),
        'books_in_genre': serialize('json', books_in_genre),
        'complex_filter': serialize('json', complex_filter),
    }
    return JsonResponse(data)

# models.py
from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100)

# In This Example, We Demonstrate Various Ways To Filter Books Based On Author Name, Publication Year, Genre, And More Complex Conditions Using Q Objects.
# The Results Are Serialized To JSON And Returned In A JsonResponse.
# You Can Customize The Filtering Conditions As Per Your Requirements.
# Note: Make Sure To Import The Necessary Modules And Adjust The Model Fields According To Your Actual Models.

# ====================

# To Test This View, You Can Map It To A URL In Your urls.py File:
# urls.py
from django.urls import path
from .views import filter_books
urlpatterns = [
    path('filter-books/', filter_books, name='filter_books'),
]
# Now, When You Access The /filter-books/ URL, You Will Get A JSON Response Containing The Filtered Book Records Based On The Specified Conditions.

'''===================='''
# Search Functionality In QuerySets
'''====================
Django Provides A Convenient Way To Implement Search Functionality In QuerySets Using The `filter()` Method Along With The `icontains` Lookup. This Allows You To Perform Case-Insensitive Searches On Text Fields. Here Is An Example Of How To Implement Search Functionality In A Django View:'''
# views.py
from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db.models import Q
def search_books(request):
    query = request.GET.get('q', '')  # Get The Search Query From The Request
    if query:
        # Perform A Case-Insensitive Search On The Title And Author Name Fields
        search_results = Book.objects.filter(
            Q(title__icontains=query) | Q(author__name__icontains=query)
        )
    else:
        search_results = Book.objects.none()  # Return An Empty QuerySet If No Query Is Provided

    data = {
        'search_results': serialize('json', search_results),
    }
    return JsonResponse(data)
# models.py
from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100)

# In This Example, We Define A View Called `search_books` That Retrieves A Search Query From The Request's GET Parameters. It Uses The `icontains` Lookup To Perform A Case-Insensitive Search On The `title` And `author__name` Fields Of The `Book` Model. The Results Are Serialized To JSON And Returned In A JsonResponse.

# To Test This View, You Can Map It To A URL In Your urls.py File:

# urls.py
from django.urls import path
from .views import search_books
urlpatterns = [
    path('search-books/', search_books, name='search_books'),
]
# Now, When You Access The /search-books/?q=your_search_term URL, You Will Get A JSON Response Containing The Books That Match The Search Term In Either The Title Or The Author's Name.
'''===================='''


# All Types Of Filtering In QuerySets
'''====================
Django Provides A Variety Of Filtering Options In QuerySets To Retrieve Specific Records Based On Different Conditions. Here Are Some Common Types Of Filtering You Can Use:'''

from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db.models import Q

def various_filters(request):
    # Exact Match
    exact_match = Book.objects.filter(title='Django For Beginners')

    # Case-Insensitive Match
    case_insensitive = Book.objects.filter(title__iexact='django for beginners')

    # Contains
    contains_filter = Book.objects.filter(title__contains='Django')

    # Case-Insensitive Contains
    icontains_filter = Book.objects.filter(title__icontains='django')

    # Greater Than
    greater_than = Book.objects.filter(publication_year__gt=2015)

    # Less Than
    less_than = Book.objects.filter(publication_year__lt=2000)

    # Range
    range_filter = Book.objects.filter(publication_year__range=(2000, 2020))

    # In A List
    in_list = Book.objects.filter(genre__in=['Science Fiction', 'Fantasy'])

    # Is Null
    is_null = Book.objects.filter(author__isnull=True)

    data = {
        'exact_match': serialize('json', exact_match),
        'case_insensitive': serialize('json', case_insensitive),
        'contains_filter': serialize('json', contains_filter),
        'icontains_filter': serialize('json', icontains_filter),
        'greater_than': serialize('json', greater_than),
        'less_than': serialize('json', less_than),
        'range_filter': serialize('json', range_filter),
        'in_list': serialize('json', in_list),
        'is_null': serialize('json', is_null),
    }
    return JsonResponse(data)

# models.py
from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100)
# In This Example, We Demonstrate Various Types Of Filtering In Django QuerySets, Including Exact Matches, Case-Insensitive Matches, Contains, Greater Than, Less Than, Range, In A List, And Is Null. The Results Are Serialized To JSON And Returned In A JsonResponse.

# To Test This View, You Can Map It To A URL In Your urls.py File:

# urls.py
from django.urls import path
from .views import various_filters
urlpatterns = [
    path('various-filters/', various_filters, name='various_filters'),
]
# Now, When You Access The /various-filters/ URL, You Will Get A JSON Response Containing The Filtered Book Records Based On The Different Conditions Specified.
'''===================='''

# Filetering Based On Date And Time In QuerySets
'''====================
Django Provides Several Lookups To Filter QuerySets Based On Date And Time Fields. Here Are Some Common Examples Of How To Filter Based On Date And Time In Django:'''

from django.shortcuts import render
from .models import Event
from django.http import JsonResponse
from django.core.serializers import serialize
from django.utils import timezone

def filter_events_by_date(request):
    # Filter Events Happening Today
    today = timezone.now().date()
    events_today = Event.objects.filter(date__date=today)

    # Filter Events Happening This Month
    events_this_month = Event.objects.filter(date__month=today.month, date__year=today.year)

    # Filter Events Happening This Year
    events_this_year = Event.objects.filter(date__year=today.year)

    # Filter Events Before A Specific Date
    specific_date = timezone.datetime(2023, 12, 31)
    events_before_date = Event.objects.filter(date__lt=specific_date)

    # Filter Events After A Specific Date
    events_after_date = Event.objects.filter(date__gt=specific_date)

    data = {
        'events_today': serialize('json', events_today),
        'events_this_month': serialize('json', events_this_month),
        'events_this_year': serialize('json', events_this_year),
        'events_before_date': serialize('json', events_before_date),
        'events_after_date': serialize('json', events_after_date),
    }
    return JsonResponse(data)

# models.py
from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)

# In This Example, We Define A View Called `filter_events_by_date` That Demonstrates Various Ways To Filter Events Based On Date And Time. We Filter Events Happening Today, This Month, This Year, Before A Specific Date, And After A Specific Date. The Results Are Serialized To JSON And Returned In A JsonResponse.

# To Test This View, You Can Map It To A URL In Your urls.py File:

# urls.py
from django.urls import path
from .views import filter_events_by_date
urlpatterns = [
    path('filter-events-by-date/', filter_events_by_date, name='filter_events_by_date'),
]
# Now, When You Access The /filter-events-by-date/ URL, You Will Get A JSON Response Containing The Filtered Event Records Based On The Date And Time Conditions Specified.
'''===================='''

# Filtering Based On Related Models In QuerySets
'''====================
Django Allows You To Filter QuerySets Based On Related Models Using The Double Underscore (`__`) Notation. This Enables You To Traverse Relationships Between Models And Apply Filters On Related Fields. Here Is An Example Of How To Filter Based On Related Models In Django:'''

from django.shortcuts import render
from .models import Book
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db.models import Q
def filter_books_by_author_country(request):
    # Filter Books Where The Author's Country Is 'USA'
    books_by_usa_authors = Book.objects.filter(author__country='USA')

    # Filter Books Where The Author's Name Contains 'Smith'
    books_by_smith_authors = Book.objects.filter(author__name__icontains='Smith')

    data = {
        'books_by_usa_authors': serialize('json', books_by_usa_authors),
        'books_by_smith_authors': serialize('json', books_by_smith_authors),
    }
    return JsonResponse(data)

# models.py
from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100)
# In This Example, We Define A View Called `filter_books_by_author_country` That Filters Books Based On The Country And Name Of Their Related Author Model. The Results Are Serialized To JSON And Returned In A JsonResponse.

# To Test This View, You Can Map It To A URL In Your urls.py File:

# urls.py
from django.urls import path

from .views import filter_books_by_author_country
urlpatterns = [
    path('filter-books-by-author-country/', filter_books_by_author_country, name='filter_books_by_author_country'),
]
# Now, When You Access The /filter-books-by-author-country/ URL, You Will Get A JSON Response Containing The Filtered Book Records Based On The Related Author's Country And Name.
'''===================='''


# Filtering In QuerySets Using A Custom filters.py File
'''====================
To Organize Your Filtering Logic Better, You Can Create A Custom `filters.py` File In Your Django App. This File Can Contain Functions That Handle Different Filtering Scenarios. Here Is An Example Of How To Implement Filtering In A Custom `filters.py` File:'''
# filters.py
import django
from django import forms
from .models import Book

class BookFilterForm(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'author__name': ['exact', 'icontains'],
            'publication_year': ['gt', 'lt', 'range'],
            'genre': ['exact', 'in'],
        }

# views.py
from django.shortcuts import render
from .models import Book
from .filters import BookFilterForm
from django.http import JsonResponse
from django.core.serializers import serialize

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filter_class = BookFilterForm
    
def filter_books(request):
    filter_form = BookFilterForm(request.GET, queryset=Book.objects.all())
    filtered_books = filter_form.qs

    data = {
        'filtered_books': serialize('json', filtered_books),
    }
    return JsonResponse(data)


# models.py
from django.db import models
class Author(models.Model):
    name = models.CharField(max_length=100)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=100)

# In This Example, We Create A `BookFilterForm` In The `filters.py` File That Defines Various Filtering Options For The `Book` Model. In The View, We Instantiate The Filter Form With The Request's GET Parameters And Retrieve The Filtered QuerySet. The Results Are Serialized To JSON And Returned In A JsonResponse.

# To Test This View, You Can Map It To A URL In Your urls.py File:

# urls.py
from django.urls import path
from .views import filter_books
urlpatterns = [
    path('filter-books/', filter_books, name='filter_books'),
]

# Now, When You Access The /filter-books/ URL With Appropriate Query Parameters, You Will Get A JSON Response Containing The Filtered Book Records Based On The Conditions Specified In The Query Parameters.
'''===================='''
