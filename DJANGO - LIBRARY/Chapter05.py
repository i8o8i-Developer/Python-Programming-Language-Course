# Django Template Language (DTL) Filters And Tags :
'''Django Template Language (DTL) Provides A Set Of Built-In Filters And Tags That Allow You To Manipulate Data And Control The Flow Of Your Templates. Here'S An Overview Of Some Commonly Used DTL Filters And Tags:'''


# All Used DTL Filters :
'''1. Lower : Converts A String To Lowercase.
   Usage : {{ value|lower }}

2. Upper : Converts A String To Uppercase.
    Usage : {{ value|upper }}

3. Title : Converts A String To Title Case.
    Usage : {{ value|title }}

4. Length : Returns The Length Of A String Or List.
    Usage : {{ value|length }}

5. Default : Provides A Default Value If The Variable Is None Or Empty.
    Usage : {{ value|default:"Default Value" }}

6. Date : Formats A Date According To The Given Format String.
    Usage : {{ value|date:"F j, Y" }}

7. Join : Joins A List Into A String With A Given Separator.
    Usage : {{ value|join:", " }}

8. Slice : Slices A List Or String.
    Usage : {{ value|slice:"1:5" }}

9. Safe : Marks A String As Safe For HTML Output.
    Usage : {{ value|safe }}

10. Truncatechars : Truncates A String To A Specified Number Of Characters.
    Usage : {{ value|truncatechars:50 }}

11. Add : Adds A Value To A Number.
    Usage : {{ value|add:10 }}
    Usage : {{ value|add:"10" }}  # For Strings
    Usage : {{ First_Value|add:Second_Value }}  # For Variables'''

# All Used DTL Tags :
'''
1. If : Conditional Statement To Render Content Based On A Condition.
    Usage :
    {% if condition %}
        Content To Render If Condition Is True
    {% else %}
        Content To Render If Condition Is False
    {% endif %}

2. For : Loop Through A List Or Queryset.
    Usage :
    {% for item in list %}
        {{ item }}
    {% endfor %}

3. Block : Defines A Block Of Content That Can Be Overridden In Child Templates.
    Usage :
    {% block block_name %}
        Default Content
    {% endblock %}

4. Extends : Inherits From A Parent Template.
    Usage :
    {% extends "base.html" %}

5. Include : Includes Another Template Within The Current Template.
    Usage :
    {% include "header.html" %}
    - Passes The Current Context To The Included Template.
        Usage With Context :
        {% include "header.html" with user=user %}
        Usage Without Context :
        {% include "header.html" only %}

6. Comment : Adds Comments That Are Not Rendered In The Output.
    Usage :
    {% comment %}
        This Is A Comment
    {% endcomment %}

7. With : Creates A New Context Variable For Use Within A Block.
    Usage :
    {% with total=business.employees.count %}
        Total Employees: {{ total }}
    {% endwith %}

8. Url : Generates A URL For A Given View Name.
    Usage :
    {% url 'view_name' arg1 arg2 %}

9. Load : Loads Custom Template Tags And Filters From A Specified Module.
    Usage :
    {% load custom_tags %}

10. Cycle : Cycles Through A List Of Values.
    Usage :
    {% cycle 'odd' 'even' %}

11. Spaceless : Removes Whitespace Between HTML Tags.
    Usage :
    {% spaceless %}
        <div>
            <p>Some Text</p>
        </div>
    {% endspaceless %}

12. Firstof : Outputs The First Non-Empty Variable From A List.
    Usage :
    {% firstof var1 var2 var3 "Default Value" %}

13. Regroup : Regroups A List Of Objects By A Common Attribute.
    Usage :
    {% regroup list by attribute as grouped_list %}
    {% for group in grouped_list %}
        <h2>{{ group.grouper }}</h2>
        <ul>
        {% for item in group.list %}
            <li>{{ item }}</li>
        {% endfor %}
        </ul>
    {% endfor %}

14. Filter : Filters A List Based On A Condition.
    Usage :
    {% filter force_escape %}
        {{ variable }}
    {% endfilter %}

15. Widthratio : Calculates The Width Ratio Of Two Values.
    Usage :
    {% widthratio this_value max_value 100 %}
    This Will Calculate (this_value / max_value) * 100 And Output The Result.

16. Now : Outputs The Current Date And Time.
    Usage :
    {% now "Y-m-d H:i" %}

17. Verbose : Outputs A Variable In A More Readable Format.
    Usage :
    {% verbose variable %}

18. Time : Formats A Time According To The Given Format String.
    Usage :
    {% time "H:i:s" %}
19. Localtime : Converts A DateTime To The Current Time Zone.
    Usage :
    {% localtime on %}
        {{ datetime_variable }}
    {% endlocaltime %}
20. Static : Generates The URL For A Static File.
    Usage :
    {% static "Path/To/File.css" %}
'''

#-------------------------------
'''Variable Injection And Output Escaping :
Django Templates Automatically Escape Variables To Prevent Cross-Site Scripting (XSS) Attacks. You Can Use The Safe Filter To Mark A Variable As Safe If You Are Sure It Does Not Contain Malicious Content. '''

# For Example:   
{{ user_input|safe }}
'''This Will Render The user_input Variable Without Escaping HTML Characters.
Remember To Use The Safe Filter Cautiously, As It Can Introduce Security Risks If The Content Is Not Properly Sanitized.'''

'''Also, You Can Use Double Curly Braces To Inject Variables Into Your Template.'''
# For Example:
<p>{{ variable_name }}</p>
'''This Will Output The Value Of variable_name In The Rendered HTML.'''

'''Output Escaping Is Enabled By Default In Django Templates, So Any HTML Special Characters In The Variable Will Be Converted To Their Corresponding HTML Entities. '''
# For Example:
{{ "<script>alert('XSS')</script>" }}
'''Will Be Rendered As :
[  &lt;script&gt;alert(&#39;XSS&#39;)&lt;/script&gt;  ]
This Prevents The Script From Being Executed In The Browser.
If You Want To Disable Escaping For A Specific Variable, You Can Use The Safe Filter As Shown Above.'''

#-------------------------------
'''Custom Template Tags And Filters :
Django Allows You To Create Custom Template Tags And Filters To Extend The Functionality Of The Template Language. You Can Define Your Own Logic And Reuse It Across Multiple Templates.
To Create A Custom Filter, You Need To Create A templatetags Directory Inside Your App, Create A Python Module, And Define Your Filter Using The register.filter Decorator.'''
# For Example:
from django import template
register = template.Library()
@register.filter
def multiply(value, arg):
    return value * arg


# This Custom Filter Can Be Used In Templates As Follows:
''' {% load custom_filters %} '''

'''{{ some_value|multiply:5 }}'''
# This Will Multiply some_value By 5 And Render The Result.
#-------------------------------

'''Inheritance And Template Organization :
Django Templates Support Template Inheritance, Allowing You To Create A Base Template With Common Layouts And Extend It In Child Templates. This Promotes Code Reusability And Maintains A Consistent Look Across Your Application.
To Use Template Inheritance, You Define A Base Template With Block Tags That Child Templates Can Override.'''

# For Example, In base.html:
'''<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>
        {% include "header.html" %}
    </header>
    <main>
        {% block content %}
        <!-- Default Content -->
        {% endblock %}
    </main>
    <footer>
        {% include "footer.html" %}
    </footer>
</body>
</html>'''
# In child_template.html:
'''{% extends "base.html" %}

{% block title %}Child Page Title{% endblock %}

{% block content %}
    <h1>Welcome to the Child Page</h1>
    <p>This is the content of the child page.</p>
{% endblock %}'''
'''This Will Render The Child Template Within The Structure Defined In base.html, Replacing The title And content Blocks With The Child Template'S Content.'''
#-------------------------------

# 404 Template : Not Found

'''To Create A Custom 404 Error Page In Django, You Need To Create A Template Named 404.html In Your Templates Directory. Django Will Automatically Use This Template When A Page Is Not Found.'''
# For Example, In 404.html:
'''<!DOCTYPE html>
<html>
<head>
    <title>Page Not Found</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
        h1 { font-size: 50px; }
        p { font-size: 20px; }
        a { color: #007BFF; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>404</h1>
    <p>Sorry, The Page You Are Looking For Does Not Exist.</p>
    <a href="{% url 'home' %}">Go Back Home</a>
</body>
</html>'''

'''This Template Will Be Rendered Whenever A User Tries To Access A Page That Does Not Exist On Your Website. You Can Customize The Content And Styling As Needed.'''
# How To Connect 404 Template :
'''To Ensure That Django Uses Your Custom 404.html Template, Make Sure You Have The Following Settings In Your settings.py File:'''
# In settings.py:
DEBUG = False
ALLOWED_HOSTS = ['YourDomain.com', 'localhost', '']

'''When DEBUG Is Set To False, Django Will Use The 404.html Template For Not Found Errors. Make Sure To Test Your 404 Page By Accessing A Non-Existent URL On Your Site.'''

from django.http import Http404
from django.shortcuts import render
def my_view(request):
    # Some Logic Here
    if not item_exists:
        raise Http404("Item Not Found")
    return render(request, 'My_Template.html', context)
"Automatically Renders The 404.html Template When An Http404 Exception Is Raised."

#-------------------------------