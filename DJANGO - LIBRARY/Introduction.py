# Introduction to Django
'''Django Is A High-Level Python Web FrameWork That Encourages Rapid Development And Clean, Pragmatic Design. It Is Built By Experienced Developers To Take Care Of Much Of The Hassle Of Web Development, Allowing You To Focus On Writing Your App Without Needing To Reinvent The Wheel. It Has Pre-Built Batteries That Include User Authentication, Content Administration, Site Maps, RSS Feeds, And Many More Features Right Out Of The Box. Follows The Model-View-Template (MVT) Architectural Pattern, Which Is A Variant Of The Model-View-Controller (MVC) Pattern.'''

# Model - Handles The Data Layer
'''The Model Is Responsible For Defining The Data Structure Of The Application. It Interacts With The Database And Manages Data Retrieval, Storage, And Manipulation. In Django, Models Are Defined As Python Classes That Subclass django.db.models.Model. Each Attribute Of The Class Represents A Database Field.'''

#VIEW - Manages The Business Logic
'''The View Is Responsible For Processing User Requests, Interacting With The Model To Retrieve Or Modify Data, And Returning The Appropriate Response. In Django, Views Are Defined As Python Functions Or Classes That Take A Web Request And Return A Web Response.'''

# Template - Handles The Presentation Layer
'''The Template Is Responsible For Defining The Presentation Layer Of The Application. It Manages How Data Is Displayed To The User. In Django, Templates Are HTML Files That Contain Placeholder Variables And Template Tags To Dynamically Generate Content Based On The Data Passed From The View.'''

# iNSTALLATION OF DJANGO
'''To Install Django, You Can Use The Python Package Manager pip. Open Your Command Line Interface And Run The Following Command:'''
# pip install django
'''This Command Will Download And Install The Latest Version Of Django From The Python Package Index (PyPI). Once Installed, You Can Verify The Installation By Running:'''
# django-admin --version
'''This Will Display The Installed Version Of Django On Your System.'''
# CREATING A DJANGO PROJECT
'''To Create A New Django Project, Use The django-admin Command-Line Tool. Run The Following Command In Your Command Line Interface:'''
# django-admin startproject projectname
'''Replace projectname With The Desired Name For Your Project. This Command Will Create A New Directory Named projectname Containing The Basic Structure And Files Needed For A Django Project.'''
# RUNNING THE DEVELOPMENT SERVER
'''To Run The Development Server, Navigate To The Project Directory Using The Command Line Interface And Execute The Following Command:'''
# python manage.py runserver
'''This Command Will Start The Django Development Server, Allowing You To Access Your Project In A Web Browser At http://127.0.0.1:8000/'''

# CREATING A DJANGO APP
'''To Create A New Django App Within Your Project, Use The Following Command:'''
# python manage.py startapp appname
'''Replace appname With The Desired Name For Your App. This Command Will Create A New Directory Named appname Containing The Basic Structure And Files Needed For A Django App.'''
# ADDING THE APP TO THE PROJECT
'''To Add The Newly Created App To Your Django Project, Open The settings.py File Located In The Project Directory And Add The App Name To The INSTALLED_APPS List. For Example:'''
# INSTALLED_APPS = [
#     ...
#     'appname',
#     ...
# ]
'''This Will Register The App With The Project, Allowing You To Use Its Functionality.'''
# MIGRATIONS
'''After Creating Models In Your App, You Need To Create And Apply Migrations To Update The Database Schema. Use The Following Commands:'''
# python manage.py makemigrations
'''This Command Creates New Migration Files Based On The Changes Made To The Models.'''
# python manage.py migrate
'''This Command Applies The Migrations To The Database, Updating The Schema Accordingly.'''
# CREATING A SUPERUSER
'''To Create A Superuser Account For Accessing The Django Admin Interface, Use The Following Command:'''
# python manage.py createsuperuser
'''Follow The Prompts To Enter A Username, Email Address, And Password For The Superuser.'''
# ACCESSING THE ADMIN INTERFACE
'''To Access The Django Admin Interface, Start The Development Server And Navigate To http://127.0.0.1:8000/admin/ In Your Web Browser. Log In Using The Superuser Credentials You Created.'''
# This Interface Allows You To Manage Your Application's Data Through A User-Friendly Web Interface.

# CONCLUSION
'''Django Is A Powerful And Flexible Web Framework That Simplifies The Process Of Building Web Applications. By Following The Model-View-Template Architecture, It Promotes A Clean Separation Of Concerns, Making It Easier To Develop, Maintain, And Scale Your Applications. With Its Rich Set Of Built-In Features And Extensive Documentation, Django Is An Excellent Choice For Both Beginners And Experienced Developers Looking To Create Robust Web Applications Quickly.'''