# ============================================================================
# DJANGO MODELS & ORM (Object-Relational Mapping)
# ============================================================================

'''
Models Are Python Classes That Define The Structure Of Your Database.
The Django ORM (Object-Relational Mapping) Allows You To Interact With Your 
Database Using Python Code Instead Of SQL.
'''

# ============================================================================
# CREATING YOUR FIRST MODEL
# ============================================================================

from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

'''
Key Points:
- Each Model Is Aa Python Class That Subclasses django.db.models.Model
- Each Attribute Represents A Database Field
- Django Automatically Creates An 'id' Primary Key Field
- __str__ Method Defines The String Representation
- Meta Class Contains Metadata Options
'''

# ============================================================================
# COMMON FIELD TYPES
# ============================================================================

'''
String Fields:
- CharField(max_length)         # Short Text With Max Length
- TextField()                   # Long Text Without Length Limit
- EmailField()                  # Email Validation
- URLField()                    # URL Validation
- SlugField()                   # URL-Friendly Slugs
Numeric Fields:
- IntegerField()                # Integer Numbers
- BigIntegerField()             # Large Integers
- SmallIntegerField()           # Small Integers (-32768 to 32767)
- DecimalField(max_digits, decimal_places)  # Precise Decimal Numbers
- FloatField()                  # Floating Point Numbers
Date and Time Fields:
- DateField()                   # Date Only
- TimeField()                   # Time Only
- DateTimeField()               # Date And Time
- DurationField()               # Time Span

Boolean Fields:
- BooleanField()                # True/False
- NullBooleanField()            # True/False/None (Deprecated, Use BooleanField With null=True)

File Fields:
- FileField(upload_to)          # File Uploads
- ImageField(upload_to)         # Image Uploads (Requires Pillow)
Other Fields:
- JSONField()                   # JSON Data
- UUIDField()                   # UUID
- BinaryField()                 # Binary Data
'''

# ============================================================================
# FIELD OPTIONS
# ============================================================================

class Book(models.Model):
    title = models.CharField(
        max_length=200,
        help_text="Enter The Book Title"
    )
    isbn = models.CharField(
        max_length=13,
        unique=True,                    # Must Be Unique Across All Records
        help_text="13 Character ISBN Number"
    )
    description = models.TextField(
        blank=True,                     # Can Be Empty In Forms
        null=True,                      # Can Be NULL In Database
        help_text="Brief Description"
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0.00,                   # Default Value
        help_text="Price In USD"
    )
    is_available = models.BooleanField(
        default=True,
        help_text="Is This Book Available?"
    )
    pages = models.IntegerField(
        validators=[MinValueValidator(1)],  # Custom Validation
        help_text="Number Of Pages"
    )

'''
Common Field Options:
- null=True/False          # Allow NULL In Database
- blank=True/False         # Allow Empty In Forms
- default=value            # Default Value
- unique=True/False        # Unique Constraint
- choices=CHOICES          # Predefined Choices
- help_text="text"         # Help Text For Forms
- verbose_name="name"      # Human-Readable Name
- validators=[...]         # Custom Validators
- editable=True/False      # Editable In Forms
- db_index=True/False      # Create Database Index
- primary_key=True/False   # Make This The Primary Key
'''

# ============================================================================
# MODEL RELATIONSHIPS
# ============================================================================

# One-To-Many Relationship (ForeignKey)
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,       # Delete Books When Publisher Is Deleted
        related_name='books'            # Access Books From Publisher: Publisher.Books.All()
    )

'''
on_delete Options:
- CASCADE: Delete Related Objects
- PROTECT: Prevent Deletion If Related Objects Exist
- SET_NULL: Set To NULL (Requires null=True)
- SET_DEFAULT: Set To Default Value
- SET(): Set To Specific Value
- DO_NOTHING: Do Nothing (May Cause Database Errors)
'''

# Many-To-Many Relationship
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(
        Author,
        related_name='books',
        blank=True
    )

# Many-To-Many with Extra Fields (Through Model)
class Book(models.Model):
    title = models.CharField(max_length=200)

class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(
        Book,
        through='BookAuthor'
    )

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=100)  # Extra Field
    order = models.IntegerField()                     # Extra Field
    
    class Meta:
        ordering = ['order']

# One-To-One Relationship
class Author(models.Model):
    name = models.CharField(max_length=100)

class AuthorProfile(models.Model):
    author = models.OneToOneField(
        Author,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    biography = models.TextField()
    website = models.URLField()
    social_media = models.JSONField(default=dict)

# ============================================================================
# QUERYING THE DATABASE (CRUD OPERATIONS)
# ============================================================================

# CREATE - Adding Data
# Method 1: Create And Save
author = Author(first_name='John', last_name='Doe', email='john@example.com')
author.save()

# Method 2: Create In One Step
author = Author.objects.create(
    first_name='Jane',
    last_name='Smith',
    email='jane@example.com'
)

# Method 3: Bulk Create (More Efficient)
Author.objects.bulk_create([
    Author(first_name='Bob', last_name='Johnson', email='bob@example.com'),
    Author(first_name='Alice', last_name='Williams', email='alice@example.com'),
])

# READ - Retrieving Data
# Get All Records
all_authors = Author.objects.all()

# Get Specific Record By Primary Key
author = Author.objects.get(id=1)
author = Author.objects.get(pk=1)  # pk Is Shorthand for Primary Key

# Get First/Last Record
first_author = Author.objects.first()
last_author = Author.objects.last()

# Filter Records
authors = Author.objects.filter(last_name='Doe')
authors = Author.objects.filter(email__icontains='example.com')

# Exclude Records
authors = Author.objects.exclude(last_name='Smith')

# Chaining Filters
authors = Author.objects.filter(last_name='Doe').exclude(first_name='John')

# Get Or Create
author, created = Author.objects.get_or_create(
    email='john@example.com',
    defaults={'first_name': 'John', 'last_name': 'Doe'}
)

# UPDATE - Modifying Data
# Method 1: Get, Modify, Save
author = Author.objects.get(id=1)
author.first_name = 'Jonathan'
author.save()

# Method 2: Update Multiple Records
Author.objects.filter(last_name='Doe').update(last_name='Smith')

# Method 3: Update Or Create
author, created = Author.objects.update_or_create(
    email='john@example.com',
    defaults={'first_name': 'John', 'last_name': 'Doe'}
)

# DELETE - Removing Data
# Delete Single Record
author = Author.objects.get(id=1)
author.delete()

# Delete Multiple Records
Author.objects.filter(last_name='Smith').delete()

# Delete all records (be careful!)
# Author.objects.all().delete()

# ============================================================================
# QUERY FILTERS & LOOKUPS
# ============================================================================

'''
Exact Match:
    Author.objects.filter(last_name='Doe')
    Author.objects.filter(last_name__exact='Doe')

Case-Insensitive Match:
    Author.objects.filter(last_name__iexact='doe')

Contains:
    Author.objects.filter(email__contains='example')
    Author.objects.filter(email__icontains='EXAMPLE')  # Case-InSensitive
    
Starts/Ends With:
    Author.objects.filter(last_name__startswith='D')
    Author.objects.filter(last_name__istartswith='d')  # Case-Insensitive
    Author.objects.filter(email__endswith='.com')
    Author.objects.filter(email__iendswith='.COM')

In List:
    Author.objects.filter(id__in=[1, 2, 3])
    Author.objects.filter(last_name__in=['Doe', 'Smith'])

Greater Than / Less Than:
    Book.objects.filter(price__gt=20)        # greater Than
    Book.objects.filter(price__gte=20)       # greater Than or Equal
    Book.objects.filter(price__lt=50)        # less Than
    Book.objects.filter(price__lte=50)       # less Than or Equal

Range:
    Book.objects.filter(price__range=(10, 50))

Date Lookups:
    Book.objects.filter(published_date__year=2023)
    Book.objects.filter(published_date__month=12)
    Book.objects.filter(published_date__day=25)
    Book.objects.filter(created_at__date='2023-12-25')

NULL Checks:
    Author.objects.filter(bio__isnull=True)
    Author.objects.filter(bio__isnull=False)

Regex:
    Author.objects.filter(last_name__regex=r'^D.*')
    Author.objects.filter(last_name__iregex=r'^d.*')  # Case-Insensitive
'''

# ============================================================================
# COMPLEX QUERIES (Q OBJECTS & F EXPRESSIONS)
# ============================================================================

from django.db.models import Q, F

# Q Objects for Complex Lookups
# OR Condition
authors = Author.objects.filter(
    Q(first_name='John') | Q(last_name='Doe')
)

# AND Condition (default, But Can Be Explicit)
authors = Author.objects.filter(
    Q(first_name='John') & Q(last_name='Doe')
)

# NOT Condition
authors = Author.objects.filter(
    ~Q(last_name='Smith')
)

# Complex Combinations
authors = Author.objects.filter(
    (Q(first_name='John') | Q(first_name='Jane')) & ~Q(last_name='Smith')
)

# F Expressions For Field Comparisons
# Compare Two Fields
books = Book.objects.filter(pages__gt=F('price') * 10)

# Update Based On Existing Value
Book.objects.update(price=F('price') * 1.10)  # 10% Price Increase

# Annotation With F
from django.db.models import Sum
Book.objects.annotate(
    total_value=F('price') * F('stock_quantity')
)

# ============================================================================
# AGGREGATION & ANNOTATION
# ============================================================================

from django.db.models import Count, Sum, Avg, Max, Min

# Aggregate (Returns dictionary)
result = Book.objects.aggregate(
    total_books=Count('id'),
    avg_price=Avg('price'),
    max_price=Max('price'),
    min_price=Min('price'),
    total_value=Sum('price')
)
# Result: {'total_books': 100, 'avg_price': 25.50, ...}

# Annotate (Adds Field To Each Object)
publishers = Publisher.objects.annotate(
    book_count=Count('books'),
    avg_book_price=Avg('books__price')
)

for publisher in publishers:
    print(f"{publisher.name}: {publisher.book_count} books")

# Complex Aggregation
authors = Author.objects.annotate(
    num_books=Count('books'),
    total_pages=Sum('books__pages')
).filter(num_books__gt=5)

# ============================================================================
# RELATED OBJECT QUERIES
# ============================================================================

# Forward Relation (Many-To-One)
book = Book.objects.get(id=1)
publisher = book.publisher                    # Access Related Publisher

# Reverse Relation (One-To-Many)
publisher = Publisher.objects.get(id=1)
books = publisher.books.all()                 # Access All Books From Publisher

# Many-To-Many
book = Book.objects.get(id=1)
authors = book.authors.all()                  # All Authors Of The Book

author = Author.objects.get(id=1)
books = author.books.all()                    # All Books By The Author

# Add/Remove Many-To-Many
book.authors.add(author1, author2)
book.authors.remove(author1)
book.authors.clear()                          # Remove All
book.authors.set([author1, author2])         # Replace All  

# ============================================================================
# SELECT_RELATED & PREFETCH_RELATED (Optimization)
# ============================================================================

# select_related (for ForeignKey and OneToOne)
# Uses SQL JOIN - Retrieves Related Objects In Single Query
books = Book.objects.select_related('publisher').all()

for book in books:
    print(book.publisher.name)  # No Additional Query

# prefetch_related (for ManyToMany and reverse ForeignKey)
# Uses Separate Query And Python Joins
books = Book.objects.prefetch_related('authors').all()

for book in books:
    for author in book.authors.all():  # No Additional Queries
        print(author.name)

# Combine Both
books = Book.objects.select_related('publisher').prefetch_related('authors')

# ============================================================================
# ORDERING
# ============================================================================

# Order By Single Field
authors = Author.objects.order_by('last_name')

# Order By Multiple Fields
authors = Author.objects.order_by('last_name', 'first_name')

# Descending Order
authors = Author.objects.order_by('-created_at')

# Random Order
authors = Author.objects.order_by('?')

# Order By Related Field
books = Book.objects.order_by('publisher__name')

# ============================================================================
# LIMITING RESULTS
# ============================================================================

# First 5 Records
authors = Author.objects.all()[:5]

# Skip First 5, Get Next 5 (Pagination)
authors = Author.objects.all()[5:10]

# Get Specific Record By Index
author = Author.objects.all()[0]  # First Record
# Note: Negative Indexing Not Supported
# author = Author.objects.all()[-1]  # This Will Raise An Error

# ============================================================================
# DISTINCT & VALUES
# ============================================================================

# Remove Duplicates
last_names = Author.objects.values_list('last_name', flat=True).distinct()

# Get Specific Fields As Dictionaries
authors = Author.objects.values('first_name', 'last_name')
# Result: [{'first_name': 'John', 'last_name': 'Doe'}, ...]

# Get Specific Fields As Tuples
authors = Author.objects.values_list('first_name', 'last_name')
# Result: [('John', 'Doe'), ...]

# Get Single Field As Flat List
emails = Author.objects.values_list('email', flat=True)
# Result: ['john@example.com', 'jane@example.com', ...]

# ============================================================================
# EXISTS & COUNT
# ============================================================================

# Check If Records Exist (More Efficient Than Count)
has_authors = Author.objects.filter(last_name='Doe').exists()

# Count Records
author_count = Author.objects.count()
doe_count = Author.objects.filter(last_name='Doe').count()

# ============================================================================
# RAW SQL QUERIES
# ============================================================================

# Execute Raw SQL
authors = Author.objects.raw('SELECT * FROM myapp_author WHERE last_name = %s', ['Doe'])

# Direct SQL Execution
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM myapp_author WHERE id = %s", [1])
    row = cursor.fetchone()

# ============================================================================
# MODEL METHODS
# ============================================================================

class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    
    def get_discounted_price(self):
        """Calculate Price After Discount"""
        return self.price * (1 - self.discount / 100)
    
    def save(self, *args, **kwargs):
        """Override Save Method For Custom Logic"""
        # Custom logic Before Save
        self.title = self.title.strip()
        super().save(*args, **kwargs)
        # Custom logic After Save
    
    def delete(self, *args, **kwargs):
        """Override Delete Method For Custom Logic"""
        # Custom logic Before Delete
        super().delete(*args, **kwargs)
        # Custom logic After Delete
    
    @property
    def is_expensive(self):
        """Property For Expensive Check"""
        return self.price > 50
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['title', 'price']),
        ]
        constraints = [
            models.CheckConstraint(check=models.Q(price__gte=0), name='price_gte_0'),
        ]

# ============================================================================
# MODEL MANAGERS (Custom QuerySets)
# ============================================================================

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class Book(models.Model):
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default='draft')
    
    objects = models.Manager()              # Default Manager
    published = PublishedManager()          # Custom Manager

# Usage:
all_books = Book.objects.all()              # All Books
published_books = Book.published.all()      # Only Published Books

# ============================================================================
# SIGNALS
# ============================================================================

from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=Author)
def author_saved(sender, instance, created, **kwargs):
    if created:
        print(f"New Author Created: {instance.get_full_name()}")
    else:
        print(f"Author Updated: {instance.get_full_name()}")
    
@receiver(pre_delete, sender=Book)
def book_deleted(sender, instance, **kwargs):
    print(f"About To Delete Book: {instance.title}")

'''
Common Signals:
- pre_save: Before Save() Method
- post_save: After Save() Method
- pre_delete: Before Delete() Method
- post_delete: After Delete() Method
- m2m_changed: When ManyToMany Relationship Changes
'''

# ============================================================================
# MODEL VALIDATION
# ============================================================================

from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.core.exceptions import ValidationError

class Book(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    email = models.EmailField(validators=[EmailValidator()])
    
    def clean(self):
        """Custom Validation"""
        if self.rating < 1 or self.rating > 5:
            raise ValidationError('Rating Must Be Between 1 and 5')
    
    def save(self, *args, **kwargs):
        self.full_clean()  # Run Validation
        super().save(*args, **kwargs)

# ============================================================================
# BEST PRACTICES
# ============================================================================

'''
1. Always Use select_related() And prefetch_related() To Avoid N+1 Queries
2. Use bulk_create() For Creating Multiple Objects Efficiently
3. Add db_index=True To Frequently Filtered Fields
4. Use __str__() Method For Readable Object Representation
5. Keep Models Focused - One Model Per Table Concept
6. Use related_name For Reverse Relations
7. Always Specify on_delete For ForeignKey
8. Use blank=True For Optional Form Fields
9. Use null=True For Optional Database Fields
10. Document Complex Models With Docstrings
11. Use Meta Class For Model Options
12. Create Custom Managers For Common Queries
13. Use Signals Sparingly (Can Make Code Harder To Debug)
14. Always Validate Data In Clean() Method
15. Use Transactions For Related Operations
'''