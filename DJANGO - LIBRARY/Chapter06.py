# Adding Static Folder And Files That Contains Our Assests , CSS  , JS

'''In Your settings.py File, Ensure You Have The Following Configurations To Serve Static Files Correctly:'''
# In settings.py:
'''import os
Option 1 : Direct Path
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]'''

'''Option 2 : Using pathlib
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']'''

'''This Configuration Tells Django Where To Find Your Static Files During Development. Make Sure To Create A Folder Named static In Your Project Directory And Place Your CSS, JS, And Image Files There.'''

# In Your Templates, You Can Load And Use Static Files As Follows:
'''{% load static %}
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
    <script src="{% static 'js/scripts.js' %}"></script>
</head>
<body>
    # Adding Images To Static Folder And Using In Template
    <img src="{% static 'images/logo.png' %}" alt="Logo">
</body>
</html>'''
'''This Will Load The Static Files From The static Folder And Include Them In Your HTML Template.'''


#-------------------------------

"Global Static Files Configuration For Production"

'''For Production Environments, You Need To Collect All Static Files Into A Single Directory Using The collectstatic Command. First, Set The STATIC_ROOT In Your settings.py File:'''
# In settings.py:

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

"When to Use Which Configuration"

'''STATICFILES_DIRS: This Setting Is Used During Development To Tell Django Where To Find Static Files In Your Project Directory. It Allows Django's Development Server To Serve Static Files Directly From Multiple Directories.'''

'''STATIC_ROOT: This Setting Is Used In Production Environments. It Specifies The Directory Where Django Will Collect All Static Files From Your Apps And STATICFILES_DIRS Using The collectstatic Command. This Single Directory Can Then Be Served By Your Web Server.'''

'''When To Use Each:
- Use STATICFILES_DIRS In Development Settings
- Use STATIC_ROOT In Production Settings'''

'''Then, Run The Following Command In Your Terminal :'''
python manage.py collectstatic

'''This Command Gathers All Static Files From Your Apps And The STATICFILES_DIRS Into The STATIC_ROOT Directory, Which Can Then Be Served By Your Web Server.'''

#-------------------------------