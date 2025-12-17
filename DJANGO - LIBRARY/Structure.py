# ============================================================================
# DJANGO PROJECT STRUCTURE
# ============================================================================

'''
Understanding The Django Project Structure Is Crucial For Effective Development.
This File Explains Every Component And Its Purpose.
'''

# ============================================================================
# PROJECT DIRECTORY STRUCTURE
# ============================================================================

'''
After Creating A Django Project, You'll Have This Structure:

myproject/                      # Root Project Directory
    manage.py                   # Command-Line Utility For Project Tasks
    myproject/                  # Python Package For Your Project
        __init__.py             # Empty File That Tells Python This Is A Package
        settings.py             # Configuration For This Django Project
        urls.py                 # URL Declarations For This Project (Routing Table)
        asgi.py                 # Entry-Point For ASGI-Compatible Web Servers
        wsgi.py                 # Entry-Point For WSGI-Compatible Web Servers
    db.sqlite3                  # Default SQLite Database (Created After First Migration)
'''

# ============================================================================
# PROJECT FILES EXPLAINED
# ============================================================================

# 1. manage.py
'''
Purpose: Command-Line Utility For Administrative Tasks

Common Commands:
- python manage.py runserver        # Start Development Server
- python manage.py startapp         # Create A New App
- python manage.py makemigrations   # Create Migration Files
- python manage.py migrate          # Apply Migrations To Database
- python manage.py createsuperuser  # Create Admin User
- python manage.py shell            # Open Python Shell With Django Context
- python manage.py test             # Run Tests
- python manage.py collectstatic    # Collect Static Files For Production

Note: Never Modify This File Unless You Know What You're Doing.
'''

# 2. settings.py
'''
Purpose: Configuration File For Django Project

Key Sections:
- SECRET_KEY: Cryptographic Key For Security (Keep It Secret!)
- DEBUG: Toggle Debug Mode (True For Development, False For Production)
- ALLOWED_HOSTS: List Of Allowed Host/Domain Names
- INSTALLED_APPS: List Of All Django Apps Activated In This Project
- MIDDLEWARE: List Of Middleware Components
- ROOT_URLCONF: Python Path To URL Configuration
- TEMPLATES: Template Engine Configuration
- DATABASES: Database Configuration
- AUTH_PASSWORD_VALIDATORS: Password Validation Rules
- LANGUAGE_CODE, TIME_ZONE: Localization Settings
- STATIC_URL, STATIC_ROOT: Static Files Configuration
- MEDIA_URL, MEDIA_ROOT: User-Uploaded Files Configuration
Security Note: Never Commit SECRET_KEY Or Sensitive Credentials To Version Control!
Use Environment Variables For Sensitive Data.
'''

# 3. urls.py
'''
Purpose: URL Routing Configuration (URL Dispatcher)

This File Defines The Mapping Between URLs And Views.
It's Like A Table Of Contents For Your Website. 

Example:
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('blog/', include('blog.urls')),
        path('api/', include('api.urls')),
    ]

Best Practices:
- Use include() To Reference Other URL Configurations
- Keep Project-Level urls.py Simple And Delegate To App-Level urls
- Use Namespaces To Avoid URL Name Conflicts
'''

# 4. wsgi.py
'''
Purpose: Web Server Gateway Interface Configuration

Used For Deploying Django With WSGI-Compatible Servers Like:
- Gunicorn
- uWSGI
- mod_wsgi (Apache)

This File Is The Entry Point For WSGI Servers To Serve Your Project.
You Typically Don't Need To Modify This File.
'''

# 5. asgi.py
'''
Purpose: Asynchronous Server Gateway Interface Configuration

Used For Deploying Django With ASGI-Compatible Servers Like:
- Daphne
- Uvicorn
- Hypercorn

Required For:
- WebSockets
- HTTP/2
- Long-polling
- Async views

This File Is The Entry Point For ASGI Servers.
'''

# 6. __init__.py
'''
Purpose: Marks Directory As A Python Package

This Empty File Tells Python That The Directory Should Be Treated As A Package.
You Can Add Package-Level Initialization Code Here If Needed.
'''

# 7. db.sqlite3
'''
Purpose: Default SQLite Database File

Created Automatically When You Run Migrations For The First Time.
Contains All Your Application Data During Development.

Note: SQLite Is Great For Development But Not Recommended For Production.
Use PostgreSQL, MySQL, Or Other Robust Databases For Production.
'''

# ============================================================================
# DJANGO APP STRUCTURE
# ============================================================================

'''
Apps Are Reusable Components That Encapsulate Specific Functionality.
After Creating An App With 'python manage.py startapp myapp':

myapp/                          # App Directory
    __init__.py                 # Makes This Directory A Python Package
    admin.py                    # Register Models For Django Admin
    apps.py                     # App Configuration
    models.py                   # Define Database Models
    views.py                    # Define View Functions/Classes
    tests.py                    # Unit Tests For The App
    urls.py                     # App-Specific URL Patterns (You Create This)
    migrations/                 # Database Migration Files
        __init__.py 
    templates/                  # HTML Templates (You Create This)
        myapp/                  # Namespace Templates With App Name
            template1.html
            template2.html
    static/                     # Static Files (You Create This)
        myapp/                  # Namespace Static Files With App Name
            css/
                style.css
            js/
                script.js
            images/
                logo.png
'''

# ============================================================================
# APP FILES EXPLAINED
# ============================================================================

# 1. admin.py
'''
Purpose: Register Models With Django's Admin Interface

Example:
    from django.contrib import admin
    from .models import Book
    
    @admin.register(Book)
    class BookAdmin(admin.ModelAdmin):
        list_display = ['title', 'author', 'published_date']
        search_fields = ['title', 'author']
        list_filter = ['published_date']

Features:
- Automatic CRUD Interface For Models
- Customizable List Views
- Search And Filtering
- Inline Editing Of Related Models
'''

# 2. apps.py
'''
Purpose: App Configuration

Contains Metadata About The App And Allows Customization.

Example:
    from django.apps import AppConfig
    
    class MyappConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'myapp'
        verbose_name = 'My Application'
        
        def ready(self):
            # Import Signals Or Perform Startup Tasks
            import myapp.signals

Used To Configure App Behavior And Register Signals.
'''

# 3. models.py
'''
Purpose: Define Database Models (Tables)

Models Are Python Classes That Define The Structure Of Your Database.

Example:
    from django.db import models
    
    class Book(models.Model):
        title = models.CharField(max_length=200)
        author = models.ForeignKey('Author', on_delete=models.CASCADE)
        published_date = models.DateField()
        isbn = models.CharField(max_length=13, unique=True)
        
        class Meta:
            ordering = ['-published_date']
            verbose_name_plural = 'Books'
        
        def __str__(self):
            return self.title

Each Model Class Becomes A Database Table.
Model Attributes Become Table Columns.
'''

# 4. views.py
'''
Purpose: Define View Functions Or Classes (Business Logic)

Views Process Requests And Return Responses.

Function-Based View Example:
    from django.shortcuts import render
    from .models import Book
    
    def book_list(request):
        books = Book.objects.all()
        return render(request, 'myapp/book_list.html', {'books': books})

Class-Based View Example:
    from django.views.generic import ListView
    from .models import Book
    
    class BookListView(ListView):
        model = Book
        template_name = 'myapp/book_list.html'
        context_object_name = 'books'

Views Connect URLs To Templates And Models.
'''

# 5. tests.py
'''
Purpose: Write Unit Tests For Your App  

Django Provides A Testing Framework Built On Python's unittest.

Example:
    from django.test import TestCase
    from .models import Book
    
    class BookModelTest(TestCase):
        def setUp(self):
            Book.objects.create(title='Test Book', author='Test Author')
        
        def test_book_creation(self):
            book = Book.objects.get(title='Test Book')
            self.assertEqual(book.author, 'Test Author')

Run Tests With: python manage.py test
'''

# 6. urls.py (You Create This)
'''
Purpose: Define URL Patterns Specific To This App

Example:
    from django.urls import path
    from . import views
    
    app_name = 'myapp'  # Namespace For This App
    
    urlpatterns = [
        path('', views.book_list, name='book_list'),
        path('<int:pk>/', views.book_detail, name='book_detail'),
        path('create/', views.book_create, name='book_create'),
    ]

Include This In Project urls.py:
    path('books/', include('myapp.urls')),
'''

# 7. migrations/
'''
Purpose: Store Database Migration Files

Migration Files Are Automatically Generated When You Run:
    python manage.py makemigrations

They Contain Instructions For Modifying The Database Schema.

Example migration file: 0001_initial.py

Migration Files Should Be Committed To Version Control.
They Allow Tracking Of Database Schema Changes Over Time.
'''

# 8. templates/ (You Create This)
'''
Purpose: Store HTML Template Files

Best Practice: Namespace Templates By App Name
    templates/
        myapp/
            base.html
            book_list.html
            book_detail.html

This Prevents Template Name Conflicts Between Apps.

Templates Can Extend Base Templates And Use Django Template Language (DTL).
'''

# 9. static/ (You Create This)
'''
Purpose: Store Static Files (CSS, JavaScript, Images)

Best Practice: Namespace Static Files By App Name
    static/
        myapp/
            css/style.css
            js/main.js
            images/logo.png

Access In Templates:
    {% load static %}
    <link rel="stylesheet" href="{% static 'myapp/css/style.css' %}">

For Production, Collect Static Files With:
    python manage.py collectstatic
'''

# ============================================================================
# ADDITIONAL FILES AND DIRECTORIES
# ============================================================================

# requirements.txt
'''
Purpose: List All Python Package Dependencies

Example:
    Django==4.2.0
    djangorestframework==3.14.0
    psycopg2-binary==2.9.6
    pillow==9.5.0

Install Dependencies:
    pip install -r requirements.txt

Generate Requirements.txt:
    pip freeze > requirements.txt

Best Practice: Use Separate Requirements Files:
    requirements/
        base.txt        # Common Dependencies
        dev.txt         # Development Dependencies
        prod.txt        # Production Dependencies
'''

# .gitignore
'''
Purpose: Specify Files To Exclude From Version Control

Essential Entries For Django Projects:
    *.pyc
    __pycache__/
    db.sqlite3
    /media
    /static
    .env
    venv/
    .vscode/
    .idea/

Never Commit:
- Secret Keys
- Database Files (Use Migrations Instead)
- Virtual Environments
- IDE-Specific Files
'''

# .env (You Create This)
'''
Purpose: Store Environment Variables And Secrets

Example:
    DEBUG=True
    SECRET_KEY=Your-Secret-Key-Here
    DATABASE_URL=postgresql://user:Password@localhost/dbname

Load In settings.py:
    import os
    from pathlib import Path
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'

Use Python-Decouple Or Django-Environ For Easier Management.
'''

# ============================================================================
# COMPLETE PROJECT STRUCTURE EXAMPLE
# ============================================================================

'''
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    app1/
        __init__.py
        admin.py
        apps.py
        models.py
        views.py
        urls.py
        tests.py
        migrations/
        templates/
            app1/
        static/
            app1/
    app2/
        (same structure as app1)
    templates/              # Project-Level Templates
        base.html
        404.html
        500.html
    static/                 # Project-Level Static Files
        css/
        js/
        images/
    media/                  # User-Uploaded Files
    requirements.txt
    .gitignore
    .env
    README.md
    db.sqlite3
'''