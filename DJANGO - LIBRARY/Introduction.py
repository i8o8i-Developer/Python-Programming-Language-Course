# ============================================================================
# INTRODUCTION TO DJANGO
# ============================================================================

# What is Django?
'''
Django Is A High-Level Python Web Framework That Encourag1es rapid development 
And Clean, Pragmatic Design. It Is Built By Experienced Developers To Take Care 
Of Much Of The Hassle Of Web Development, Allowing You To Focus On Writing Your 
App Without Needing To Reinvent The Wheel.

Key Features:
- Pre-Built Components (Batteries Included)
- User Authentication System
- Content Administration Interface
- Site Maps And RSS Feeds
- Security Features (CSRF, XSS, SQL Injection Protection)
- ORM (Object-Relational Mapping)
- Template Engine
- Form Handling
- Internationalization Support
'''

# ============================================================================
# DJANGO MVT ARCHITECTURE
# ============================================================================

'''
Django Follows The Model-View-Template (MVT) Architectural Pattern, Which Is A 
Variant Of The Model-View-Controller (MVC) Pattern.
'''

# MODEL - Data Layer
'''
The Model Is Responsible For Defining The Data Structure Of The Application.

Responsibilities:
- Defines Database Schema
- Manages Data Retrieval, Storage, And Manipulation
- Provides Data Validation
- Handles Relationships Between Different Data Types

Implementation:
Models Are Defined As Python Classes That Subclass django.db.models.Model. 
Each Attribute Of The Class Represents A Database Field.

Example:
    from django.db import models
    
    class Book(models.Model):
        title = models.CharField(max_length=200)
        author = models.CharField(max_length=100)
        published_date = models.DateField()
'''

# VIEW - Business Logic Layer
'''
The View Is Responsible For Processing User Requests And Returning Responses.

Responsibilities:
- Processes HTTP Requests
- Interacts With Models To Retrieve Or Modify Data
- Applies Business Logic
- Returns HTTP Responses (HTML, JSON, Redirects, Etc.)

Implementation:
Views Can Be Defined As:
1. Function-Based Views (FBV) - Python Functions
2. Class-Based Views (CBV) - Python Classes

Example:
    from django.shortcuts import render
    
    def book_list(request): 
        books = Book.objects.all()
        return render(request, 'books/list.html', {'books': books})
'''

# TEMPLATE - Presentation Layer
'''
The Template Is Responsible For Defining How Data Is Displayed To The User.

Responsibilities:
- Defines The HTML Structure
- Displays Dynamic Content Using Template Variables
- Applies Template Logic (Loops, Conditionals)
- Handles Template Inheritance For Reusability

Implementation:
Templates Are HTML Files With Django Template Language (DTL) Syntax.
They Contain Placeholder Variables And Template Tags To Dynamically 
Generate Content Based On Data Passed From The View.

Example:
    <h1>{{ book.title }}</h1>
    <p>Author: {{ book.author }}</p>
    <p>Published: {{ book.published_date|date:"Y-m-d" }}</p>
'''

# ============================================================================
# INSTALLATION
# ============================================================================

# Installing Django
'''
To Install Django, Use The Python Package Manager pip.
'''

# Install Django
pip install django

# Verify Installation
django-admin --version

# Install Specific Version
pip install django==4.2.0

# Install Latest LTS (Long Term Support) Version
pip install django==4.2

'''
Note: It's Recommended To Use A Virtual Environment For Django Projects.

Creating A Virtual Environment:
    python -m venv myenv
    
Activating Virtual Environment:
    Windows: myenv\\Scripts\\activate
    Linux/Mac: source myenv/bin/activate
'''

# ============================================================================
# CREATING A DJANGO PROJECT
# ============================================================================

# Create A New Django Project
django-admin startproject projectname

# Navigate To Project Directory
cd projectname

'''
This Creates A Project Directory With The Following Structure:

projectname/
    manage.py              # Command-Line Utility For Project Management
    projectname/
        __init__.py        # Makes This Directory A Python Package
        settings.py        # Project Configuration
        urls.py            # URL Routing For The Project
        asgi.py            # ASGI Configuration For Deployment
        wsgi.py            # WSGI Configuration For Deployment

Best Practices:
- Use Lowercase Names With Underscores For Project Names
- Avoid Using Python Or Django Built-In Module Names
- Choose Descriptive Names That Reflect Your Project's Purpose
'''

# ============================================================================
# RUNNING THE DEVELOPMENT SERVER
# ============================================================================

# Start The Development Server
python manage.py runserver

# Run On A Specific Port
python manage.py runserver 8080

# Run On A Specific IP And Port
python manage.py runserver 0.0.0.0:8000

'''
Default Access: http://127.0.0.1:8000/

Important Notes:
- The Development Server Automatically Reloads When You Make Code Changes
- DO NOT Use This Server In Production Environments
- For Production, Use Proper Web Servers Like Gunicorn, uWSGI With Nginx/Apache

Stopping The Server:
- Press Ctrl+C In The Terminal
'''


# ============================================================================
# CREATING A DJANGO APP
# ============================================================================

# Create A New App
python manage.py startapp appname

'''
This Creates An App Directory With:

appname/
    __init__.py          # Makes This A Python Package
    admin.py             # Admin Interface Configuration
    apps.py              # App Configuration
    models.py            # Database Models
    tests.py             # Unit Tests
    views.py             # View Functions/Classes
    migrations/          # Database Migration Files
        __init__.py

Apps vs Projects:
- A Project Is A Collection Of Configurations And Apps
- An App Is A Web Application That Does Something (Blog, Auth, Etc.)
- An App Can Be Used In Multiple Projects (Reusable)
- A Project Contains Multiple Apps
'''

# ============================================================================
# REGISTERING THE APP
# ============================================================================

'''
After Creating An App, You Must Register It In settings.py:
'''

# In settings.py, add to INSTALLED_APPS:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your Apps
    'appname',              # Option 1: Simple Name
    # 'appname.apps.AppnameConfig',  # Option 2: Full Path (Recommended)
]

'''
Why Register Apps?
- Django Needs To Know Which Apps To Load
- Enables Model Discovery For Migrations
- Activates App-Specific Settings And Configurations
- Makes Templates And Static Files Discoverable
'''

# ============================================================================
# DATABASE MIGRATIONS
# ============================================================================

'''
Migrations Are Django's Way Of Propagating Changes You Make To Your Models 
(Adding A Field, Deleting A Model, Etc.) Into Your Database Schema.
'''

# Create migration Files
python manage.py makemigrations

# Create migrations For A Specific App
python manage.py makemigrations appname

# View Migration SQL Without Applying
python manage.py sqlmigrate appname 0001

# Check For Migration Issues
python manage.py check

# Apply Migrations To Database
python manage.py migrate

# Apply Migrations For A Specific App
python manage.py migrate appname

# Show Migration Status
python manage.py showmigrations

'''
Migration Workflow:
1. Make Changes To Models.py
2. Run Makemigrations (Creates Migration Files)
3. Review Generated Migrations
4. Run Migrate (Applies Changes To Database)

Common Commands:
- python manage.py makemigrations --dry-run  # Preview Changes
- python manage.py migrate --fake            # Marks Applied Without Running
- python manage.py migrate appname zero      # Reverse All Migrations For An App
'''

# ============================================================================
# CREATING A SUPERUSER
# ============================================================================

'''
A Superuser Account Provides Full Access To The Django Admin Interface.
'''

# Create Superuser Interactively
python manage.py createsuperuser

'''
You'll Be Prompted For:
- Username
- Email Address (Optional)
- Password (Entered Twice For Confirmation)

Accessing The Admin:
1. Start The Development Server
2. Navigate to http://127.0.0.1:8000/admin/
3. Login With Superuser Credentials

Note: You Can Create Additional Superusers Or Regular Users Through:
- Django Admin Interface
- Django Shell (python manage.py shell)
- Custom Management Commands
'''
# ACCESSING THE ADMIN INTERFACE
'''To Access The Django Admin Interface, Start The Development Server And Navigate To http://127.0.0.1:8000/admin/ In Your Web Browser. Log In Using The Superuser Credentials You Created.'''
# This Interface Allows You To Manage Your Application's Data Through A User-Friendly Web Interface.

# CONCLUSION
'''Django Is A Powerful And Flexible Web Framework That Simplifies The Process Of Building Web Applications. By Following The Model-View-Template Architecture, It Promotes A Clean Separation Of Concerns, Making It Easier To Develop, Maintain, And Scale Your Applications. With Its Rich Set Of Built-In Features And Extensive Documentation, Django Is An Excellent Choice For Both Beginners And Experienced Developers Looking To Create Robust Web Applications Quickly.'''