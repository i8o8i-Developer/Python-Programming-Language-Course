'''Introduction To Templates In Django'''
# Django Templates Allow You To Separate The Presentation Layer From The Business Logic In Your Web Application.
# They Enable You To Create Dynamic HTML Pages By Embedding Variables And Logic Within HTML Files.

# VIEWS.PY CODE EXAMPLE:
from django.http import HttpResponse
from django.template import loader
def index(request):
    template = loader.get_template('index.html')
    context = {
        'title': 'Welcome to Django Templates',
        'heading': 'Django Template Example',
        'message': 'This Is A Simple Example Of Using Templates In Django.'
    }
    return HttpResponse(template.render(context, request))

# To Use This Code, Ensure You Have A Django Project Set Up With An 'index.html' Template In The Appropriate Templates Directory.
# The 'index.html' File Could Look Something Like This:
'''
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>{{ message }}</p>
</body>
</html>
'''

# This Code Defines A Simple Django View That Renders An HTML Template With Dynamic Content Using Context Variables.
'''urls.py CODE EXAMPLE :'''
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
# In This Example, The URL Pattern Maps The Root URL To The index View, Which Renders The Template With The Provided Context.
# When You Access The Root URL Of Your Django Application, The index View Will Be Called, Rendering The 'index.html' Template With The Dynamic Data Passed In The Context Dictionary.

'''Project Urls.py CODE EXAMPLE :'''
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('YourApp.urls')),
]
# This Code Includes The App's URL Configurations In The Project's Main URL Configuration, Allowing The App's Views To Be Accessible From The Root URL.

'''PROJECT settings.PY CODE EXAMPLE :'''
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Additionally, You Can Use Django's Template Language To Add Logic Such As Loops And Conditionals Within Your Templates.

'''REGISTERING APP IN DJANGO SETTINGS.PY'''
# To Use An App In Your Django Project, You Need To Register It In The settings.py File Of Your Project.
# This Is Done By Adding The App's Name To The INSTALLED_APPS List In settings
# Here Is An Example Of How To Register An App Called 'library' In settings.py:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'library',  # Registering The 'library' App
]
# After Adding The App To INSTALLED_APPS, Django Will Be Aware Of The App And Its Components, Such As Models, Views, And Templates.
# Make Sure To Restart Your Django Development Server After Making Changes To settings.py For The Changes To Take Effect.