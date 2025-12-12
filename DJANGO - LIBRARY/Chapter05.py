# Django Template Language (DTL) Filters And Tags :
'''Django Template Language (DTL) Provides A Set Of Built-In Filters And Tags That Allow You To Manipulate Data And Control The Flow Of Your Templates. Here'S An Overview Of Some Commonly Used DTL Filters And Tags:'''


# Commonly Used DTL Filters :
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
    Usage : {{ value|truncatechars:50 }}'''

# Commonly Used DTL Tags :
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
{% load custom_filters %}

'''{{ some_value|multiply:5 }}'''
# This Will Multiply some_value By 5 And Render The Result.
#-------------------------------