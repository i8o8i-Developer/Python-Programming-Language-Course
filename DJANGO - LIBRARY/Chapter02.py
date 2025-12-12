# URLs Also Known As "Uniform Resource Locators" Or Here Routes

# Urls.py File PYTHON CODE : 
from django.http import HttpResponse
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]

# Views.py File PYTHON CODE :
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse("Welcome to the Home Page!")
def about(request):
    return HttpResponse("This is the About Page.")
def contact(request):
    return HttpResponse("Contact Us At Contact@Example.com")
# In This Example, We Define Three URL Patterns: The Home Page, About Page, and Contact Page. Each Pattern Is Associated With A View Function That Returns A Simple HTTP Response.
# In Django, URLs Are Defined In A File Called urls.py. Each URL Pattern Is Associated With A View Function That Handles The Request And Returns A Response.
# The Path Function Is Used To Define URL Patterns. The First Argument Is The URL Pattern As A String, The Second Argument Is The View Function That Will Handle Requests To That URL, And The Third Argument Is An Optional Name For The URL Pattern.
# When A User Visits A URL, Django Matches The URL To The Defined Patterns And Calls The Corresponding View Function To Generate A Response.
# This Is A Basic Example Of How URLs Work In Django. You Can Expand On This By Adding More Complex URL Patterns, Using Path Converters, And Organizing Your URLs Into Multiple Files For Larger Projects.

# Note: To Use This Code, You Need To Have A Django Project Set Up. The urls.py File Should Be Placed In An App Directory, And The Views Should Be Defined In The Corresponding views.py File.
'''Code :

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Your_App_Name.urls')),  # Replace 'Your_App_Name' With The Name Of Your Django App
] 
'''


# Dynamic Path Segments Allow You To Capture Values From The URL And Pass Them As Arguments To Your View Functions.
# Here Is An Example Of How To Use Dynamic Path Segments In Django URLs:
from django.http import HttpResponse
from django.urls import path
from . import views
urlpatterns = [
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
]
# In This Example, The URL Pattern Captures An Integer Value From The URL And Passes It To The article_detail View Function As The article_id Argument.
# Views.py File PYTHON CODE :
from django.http import HttpResponse , HttpResponseNotFound
from django.shortcuts import render
def article_detail(request, article_id):
    if article_id == 1:
        return HttpResponse("Displaying Article 1")
    elif article_id == 2:
        return HttpResponse("Displaying Article 2")
    else:
        return HttpResponseNotFound("Article Not Found")
# In This Example, The article_detail Function Uses The article_id Parameter To Determine Which Article To Display.
# When A User Visits A URL Like /article/1/, The article_detail Function Will Be Called With article_id Set To 1.
# This Allows You To Create Dynamic URLs That Can Handle Different Content Based On The URL Parameters.


# -----------------
'''PATH CONVERTERS'''
# Django Provides Several Built-In Path Converters That You Can Use To Specify The Type Of Data You Want To Capture From The URL. Here Are The Most Commonly Used Path Converters:
# str: Matches Any Non-Empty String, Excluding The Path Separator (/).
# int: Matches Zero Or Any Positive Integer.
# slug: Matches Any Slug String Consisting Of Letters, Numbers, Hyphens, And Underscores.
# uuid: Matches A Valid UUID.

# Here Is An Example Of Using Different Path Converters In Django URLs:
from django.http import HttpResponse
from django.urls import path
from . import views
urlpatterns = [
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('item/<uuid:item_uuid>/', views.item_detail, name='item_detail'),
]

# Views.py File PYTHON CODE :
from django.http import HttpResponse
from django.shortcuts import render
def user_profile(request, username):
    return HttpResponse(f"User Profile Page For: {username}")
def post_detail(request, post_id):
    return HttpResponse(f"Post Detail Page For Post ID: {post_id}")
def category_detail(request, category_slug):
    return HttpResponse(f"Category Detail Page For Category: {category_slug}")
def item_detail(request, item_uuid):
    return HttpResponse(f"Item Detail Page For Item UUID: {item_uuid}")
# In This Example, We Define Four URL Patterns Using Different Path Converters: str, int, slug, And uuid. Each Pattern Captures A Different Type Of Data From The URL And Passes It To The Corresponding View Function.
# This Allows You To Create More Specific And Type-Safe URL Patterns In Your Django Application.


#------------------
"""SLUGS IN DJANGO URLS"""
# A Slug Is A Short Label For Something, Containing Only Letters, Numbers, Hyphens, Or Underscores. In Django, Slugs Are Commonly Used In URLs To Identify Resources In A Readable And SEO-Friendly Way.
# Here Is An Example Of How To Use Slugs In Django URLs:
from django.http import HttpResponse
from django.urls import path
from . import views
urlpatterns = [
    path('article/<slug:article_slug>/', views.article_detail, name='article_detail'),
]
# Views.py File PYTHON CODE :
from django.http import HttpResponse
from django.shortcuts import render
def article_detail(request, article_slug):
    return HttpResponse(f"Displaying Article With Slug: {article_slug}")
# In This Example, The URL Pattern Captures A Slug Value From The URL And Passes It To The article_detail View Function As The article_slug Argument.
# When A User Visits A URL Like /article/my-first-article/, The article_detail Function Will Be Called With article_slug Set To my-first-article.
# This Allows You To Create User-Friendly URLs That Are Easy To Read And Understand, While Also Providing A Unique Identifier For Each Resource.
# Slugs Are Particularly Useful For Blog Posts, Articles, Products, Or Any Other Content Where A Readable URL Is Beneficial.
# To Generate Slugs From Strings, You Can Use Django's slugify Function:
from django.utils.text import slugify
title = "My First Article!"
article_slug = slugify(title)  # Output: "my-first-article"
# You Can Then Use This Slug In Your URLs To Represent The Article.
# In This Example, We Define Three URL Patterns: The Home Page, About Page, And Contact Page. Each Pattern Is Associated With A View Function That Returns A Simple HTTP Response.