# What Is Model In Django : 
'In Django, A Model Is A Python Class That Represents a Database Table. It Defines The Structure Of The Data, Including The Fields And Their Types, As Well As Any Behaviors Associated With The Data. Models Are Used To Interact With The Database, Allowing You To Create, Read, Update, And Delete Records In A Structured Way.'

# How To Create Model In Django
from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13)
    pages = models.IntegerField()
    cover_image = models.URLField()
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.title
# This Code Defines A Book Model With Various Fields To Store Information About Books In A Library.
# After Defining The Model, You Need To Run Migrations To Create The Corresponding Database Table:

# python manage.py makemigrations
# python manage.py migrate

# This Will Create The Necessary Database Table Based On The Model Definition.

#------------------------------------------------------------------------------

# How To Create A Username And Password In Django :

from django.contrib.auth.models import User
# Create A New User
user = User.objects.create_user('UserName', password='Password123')
user.save()

# This Code Creates A New User With The Specified Username And Password.
# You Can Also Create A Superuser (Admin) Using The Command Line:
# python manage.py createsuperuser
# Follow The Prompts To Set The Username, Email, And Password For The Superuser.
# This Superuser Can Access The Django Admin Interface To Manage The Application.
# Make Sure To Import The Necessary Modules And Run The Code In The Appropriate Context (e.g., Django Shell Or Views).
# You Can Access The Django Shell Using:
# python manage.py shell
# This Will Open An Interactive Python Shell With Django Context.


#------------------------------------------------------------------------------

'How To Register Model In Django Admin :'
# admin.py
from django.contrib import admin
from .models import Book

admin.site.register(Book)

# This Code Registers The Book Model With The Django Admin Site, Allowing You To Manage Book Records Through The Admin Interface.
# After Registering The Model, You Can Access The Admin Interface By Running The Development Server:
# python manage.py runserver