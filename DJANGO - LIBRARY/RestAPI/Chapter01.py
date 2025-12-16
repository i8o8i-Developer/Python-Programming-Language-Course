# What Is API ?
' Application Programming Interface . Allows One Software Application To Interact With Another Software Application . Using A Set Of Defined Rules .'

# REST API
' Representational State Transfer . A Set Of Rules That Developers Follow When They Create Their API . RESTful APIs Are Designed To Take Advantage Of Existing Protocols . Most Commonly Used Protocol Is HTTP .'

# REST API METHODS [ HTTP Request methods ]
' GET , POST , PUT , DELETE .'

# DJANGO REST FRAMEWORK
' A Powerful And Flexible Toolkit For Building Web APIs In Django . It Provides An Easy Way To Serialize Data , Handle Requests And Responses , And Implement Authentication And Permissions .'

# API Returns Data In JSON Format :
'''{
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_date": "1925-04-10"
}'''

# And Also In XML Format :
'''<book>
    <id>1</id>
    <title>The Great Gatsby</title>
    <author>F. Scott Fitzgerald</author>
    <published_date>1925-04-10</published_date>
</book>'''

# -----------------

# How To Install Django REST Framework ?
'''To Install Django REST Framework , You Can Use The Python Package Manager pip . Open Your Command Line Interface And Run The Following Command :'''
# pip install django
# pip install djangorestframework
# pip install markdown       # Optional , For Browsable API
# pip install django-filter  # Optional , For Filtering Support

# After Installing , Add 'rest_framework' To The INSTALLED_APPS List In Your Django Project's settings.py File :
'''INSTALLED_APPS = [
    ...
    'rest_framework',
]'''

If You Are Intended To Use The Browsable API You'll Also Want To Add REST Framework's Login And Logout Views To Your Project's urls.py File :
'''from django.urls import path, include
urlpatterns = [
    ...
    path('api-auth/', include('rest_framework.urls')),
]'''

# Now You Are Ready To Use Django REST Framework In Your Project !

# -----------------

# Basic Structure Of A Django REST Framework Project
'''1. Models.py - Define Your Data Models
2. Serializers.py - Convert Complex Data Types To Native Python Data Types
3. Views.py - Handle The Business Logic And API Endpoints
4. Urls.py - Route Requests To The Appropriate Views
5. Settings.py - Configure Django REST Framework Settings'''

# Hello World Using Django REST Framework :

#views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import APIView

class HelloWorld(APIView):
    def get(self, request):
        return Response({"message": "Hello, World!"})
#urls.py
from django.urls import path
from .views import HelloWorld
urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello-world'),
]
# Now , When You Run Your Django Server And Navigate To /hello/ , You Should See The JSON Response :
'''{
    "message": "Hello, World!"
}'''
# This Is A Simple Example , But Django REST Framework Provides Many More Features To Build Robust APIs .
# You Can Explore Features Like Authentication , Permissions , Pagination , Filtering , And More In The Official Documentation : https://www.django-rest-framework.org/