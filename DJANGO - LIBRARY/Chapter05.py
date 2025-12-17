# ============================================================================
# DJANGO TEMPLATE LANGUAGE (DTL) - FILTERS AND TAGS
# ============================================================================

'''
Django Template Language (DTL) Provides A Set Of Built-in Filters And Tags
That Allow You To Manipulate Data And Control The Flow Of Your Templates.
This Chapter Covers All Commonly Used DTL Features.
'''

# ============================================================================
# TEMPLATE FILTERS
# ============================================================================

'''
Filters Are Used To Modify Variables In Templates.
Syntax: {{ variable|filter:argument }}
'''

# STRING FILTERS
'''
1. lower - Converts String To Lowercase
   {{ value|lower }}
   Example: {{ "HELLO"|lower }} → hello

2. upper - Converts String To Uppercase
   {{ value|upper }}
   Example: {{ "hello"|upper }} → HELLO

3. title - Converts String To Title Case
   {{ value|title }}
   Example: {{ "hello world"|title }} → Hello World

4. capfirst - Capitalizes First Character
   {{ value|capfirst }}
   Example: {{ "hello"|capfirst }} → Hello

5. truncatechars - Truncates String To Specified Characters
   {{ value|truncatechars:50 }}
   Example: {{ "Long text..."|truncatechars:10 }} → Long te...

6. truncatewords - Truncates To Specified Words
   {{ value|truncatewords:5 }}
   Example: {{ "This is a long sentence"|truncatewords:3 }} → This is a...

7. slice - Slices A List Or String
   {{ value|slice:"1:5" }}
   Example: {{ "12345"|slice:"1:3" }} → 23

8. join - Joins List Into String With Separator
   {{ value|join:", " }}
   Example: {{ my_list|join:" | " }}

9. wordcount - Returns Number Of Words
   {{ value|wordcount }}
   Example: {{ "Hello world"|wordcount }} → 2

10. linebreaks - Converts Newlines To HTML <p> And <br> Tags
    {{ value|linebreaks }}

11. linebreaksbr - Converts Newlines To <br> Tags
    {{ value|linebreaksbr }}

12. striptags - Removes HTML Tags
    {{ value|striptags }}
    Example: {{ "<p>Hello</p>"|striptags }} → Hello
'''

# NUMERIC FILTERS
'''
13. add - Adds Value To Number
    {{ value|add:10 }}
    {{ value|add:"10" }}  # For Strings
    {{ first_value|add:second_value }}  # For Variables
    Example: {{ 5|add:3 }} → 8

14. divisibleby - Returns True If Divisible By Argument
    {{ value|divisibleby:3 }}
    Example: {% if count|divisibleby:2 %}Even{% endif %}

15. floatformat - Formats Floating Point Number
    {{ value|floatformat }}
    {{ value|floatformat:2 }}  # 2 Decimal Places
    Example: {{ 3.14159|floatformat:2 }} → 3.14
'''

# DATE & TIME FILTERS
'''

16. date - Formats Date According To Format String
    {{ value|date:"Y-m-d" }}
    {{ value|date:"F j, Y" }}
    Common Formats:
    - Y: 4-Digit Year (2024)
    - y: 2-Digit Year (24)
    - m: Month Number (01-12)
    - d: Day Of Month (01-31)
    - F: Month Name (January)
    - M: Short Month (Jan)
    - D: Short Day (Mon)
    Example: {{ today|date:"F d, Y" }} → December 17, 2025

17. time - Formats Time
    {{ value|time:"H:i" }}
    Example: {{ now|time:"H:i:s" }} → 14:30:45

18. timesince - Time Since Given Date
    {{ value|timesince }}
    Example: {{ post.created_at|timesince }} → 2 hours ago

19. timeuntil - Time Until Given Date
    {{ value|timeuntil }}
    Example: {{ event.start_date|timeuntil }} → 3 days
'''

# LIST & COLLECTION FILTERS
'''
20. length - Returns Length Of List Or String
    {{ value|length }}
    Example: {{ my_list|length }} → 5

21. first - Returns First Item
    {{ value|first }}
    Example: {{ my_list|first }}

22. last - Returns Last Item
    {{ value|last }}
    Example: {{ my_list|last }}

23. dictsort - Sorts List Of Dicts By Key
    {{ value|dictsort:"key_name" }}

24. dictsortreversed - Sorts In Reverse
    {{ value|dictsortreversed:"key_name" }}
'''

# OTHER USEFUL FILTERS
'''
25. default - Provides Default Value If Variable Is None Or Empty
    {{ value|default:"No value" }}
    Example: {{ user.bio|default:"No bio available" }}

26. default_if_none - Default Only If None (Not Empty String)
    {{ value|default_if_none:"None" }}

27. safe - Marks String As Safe For HTML Output (Doesn't Escape)
    {{ value|safe }}
    Example: {{ html_content|safe }}

28. escape - Escapes HTML Characters
    {{ value|escape }}

29. escapejs - Escapes For Use In JavaScript
    {{ value|escapejs }}

30. urlencode - URL Encodes String
    {{ value|urlencode }}
    Example: {{ "hello world"|urlencode }} → hello%20world

31. slugify - Converts To Slug (URL-Friendly Format)
    {{ value|slugify }}
    Example: {{ "Hello World!"|slugify }} → hello-world

32. yesno - Converts Boolean To Custom Text
    {{ value|yesno:"Yes,No,Maybe" }}
    Example: {{ is_active|yesno:"Active,Inactive" }}

33. filesizeformat - Formats File Size
    {{ value|filesizeformat }}
    Example: {{ 123456789|filesizeformat }} → 117.7 MB

34. pluralize - Returns Plural Suffix
    {{ count }} item{{ count|pluralize }}
    {{ count }} box{{ count|pluralize:"es" }}
    Example: 1 item, 2 items
'''


# ============================================================================
# TEMPLATE TAGS
# ============================================================================

'''
Template Tags Provide Logic And Control Flow In Templates.
Syntax: {% tag_name arguments %}
'''

# CONDITIONAL TAGS
'''
1. if / elif / else - Conditional Rendering
   {% if condition %}
       Content If True
   {% elif other_condition %}
       Content If Other_Condition True
   {% else %}
       Content If All Conditions False
   {% endif %}
   
   Examples Of Conditions:
   {% if user.is_authenticated %}
   {% if age >= 18 %}
   {% if score > 90 and passed %}
   {% if name == "John" or name == "Jane" %}
   {% if not is_deleted %}
   {% if items %}  # True if not empty
   {% if value in list %}
   {% if "admin" in user.groups %}

2. ifchanged - Render Only If Value Changed From Last Iteration
   {% for item in items %}
       {% ifchanged item.category %}
           <h2>{{ item.category }}</h2>
       {% endifchanged %}
       <p>{{ item.name }}</p>
   {% endfor %}
'''

# LOOP TAGS
'''
3. for - Loop Through Iterable
   {% for item in list %}
       {{ item }}
   {% empty %}
       No Items Found
   {% endfor %}
   
   Loop Variables:
   - {{ forloop.counter }}      # 1-Indexed Counter
   - {{ forloop.counter0 }}     # 0-Indexed Counter
   - {{ forloop.revcounter }}   # Reverse Counter
   - {{ forloop.revcounter0 }}  # Reverse 0-Indexed
   - {{ forloop.first }}        # True On First Iteration
   - {{ forloop.last }}         # True On Last Iteration
   - {{ forloop.parentloop }}   # Parent Loop In Nested Loops
   
   Example:
   {% for item in items %}
       <tr class="{% if forloop.first %}first{% endif %}">
           <td>{{ forloop.counter }}. {{ item.name }}</td>
       </tr>
   {% endfor %}
'''

# TEMPLATE INHERITANCE TAGS
'''
4. extends - Inherit From Parent Template
   {% extends "base.html" %}
   {% extends parent_template_variable %}
   
   Must Be First Tag In Template.

5. block - Define Overridable Content Block
   {% block title %}Default Title{% endblock %}
   {% block content %}
       Default Content
   {% endblock %}
   
   Override In Child Template:
   {% extends "base.html" %}
   {% block title %}Page Title{% endblock %}
   {% block content %}
       <h1>Page Content</h1>
   {% endblock %}
   
   Use Parent Content:
   {% block content %}
       {{ block.super }}
       Additional Content
   {% endblock %}

6. include - Include Another Template
   {% include "header.html" %}
   {% include "nav.html" with active='home' %}
   {% include "snippet.html" with user=user only %}
   
   The 'only' Keyword Prevents Passing Current Context.
'''

# URL & STATIC TAGS
'''
7. url - Generate URL For Named View
   {% url 'view_name' %}
   {% url 'view_name' arg1 arg2 %}
   {% url 'namespace:view_name' %}
   {% url 'view_name' key=value %}
   
   Examples:
   <a href="{% url 'home' %}">Home</a>
   <a href="{% url 'article_detail' article.id %}">Read More</a>
   <a href="{% url 'blog:post_detail' slug=post.slug %}">View Post</a>

8. static - Generate URL For Static File
   {% load static %}
   <link rel="stylesheet" href="{% static 'css/style.css' %}">
   <img src="{% static 'images/logo.png' %}">
   <script src="{% static 'js/main.js' %}"></script>

9. get_static_prefix - Get Static URL Prefix
   {% load static %}
   {% get_static_prefix as STATIC_PREFIX %}
   <img src="{{ STATIC_PREFIX }}images/logo.png">

10. get_media_prefix - Get Media URL Prefix
    {% load static %}
    {% get_media_prefix as MEDIA_PREFIX %}
    <img src="{{ MEDIA_PREFIX }}{{ user.avatar }}">
'''

# VARIABLE MANIPULATION TAGS
'''
11. with - Create Temporary Variable
    {% with total=business.employees.count %}
        Total Employees: {{ total }}
        Active: {{ total|subtract:inactive }}
    {% endwith %}
    
    Multiple Variables:
    {% with alpha=1 beta=2 %}
        {{ alpha }} and {{ beta }}
    {% endwith %}

12. load - Load Custom Template Tags/Filters
    {% load static %}
    {% load custom_tags %}
    {% load i18n %}

13. csrf_token - Add CSRF Protection Token
    <form method="post">
        {% csrf_token %}
        <!-- Form Fields -->
    </form>
'''

# ITERATION & ORGANIZATION TAGS
'''
14. cycle - Cycle Through Values
    {% for row in rows %}
        <tr class="{% cycle 'odd' 'even' %}">
            <td>{{ row }}</td>
        </tr>
    {% endfor %}
    
    With Named Cycles:
    {% for item in items %}
        {% cycle 'row1' 'row2' as rowcolors %}
    {% endfor %}

15. regroup - Regroup List By Attribute
    {% regroup products by category as product_list %}
    {% for category in product_list %}
        <h2>{{ category.grouper }}</h2>
        <ul>
        {% for item in category.list %}
            <li>{{ item.name }}</li>
        {% endfor %}
        </ul>
    {% endfor %}

16. firstof - Output First Non-Empty Variable
    {% firstof var1 var2 var3 "default value" %}
    
    Example:
    {% firstof user.nickname user.first_name user.username %}

17. spaceless - Remove Whitespace Between HTML Tags
    {% spaceless %}
        <div>
            <p>Text</p>
        </div>
    {% endspaceless %}
    
    Output: <div><p>Text</p></div>
'''

# COMMENT TAGS
'''
18. comment - Multi-Line Comment
    {% comment %}
        This Is A Comment That Won't Be Rendered.
        Can Span Multiple Lines.
    {% endcomment %}
    
    Single-Line Comment:
    {# This Is A Single Line Comment #}
'''

# ADVANCED TAGS
'''
19. now - Display Current Date/Time
    {% now "Y-m-d H:i:s" %}
    {% now "F j, Y" %}
    
    Store In Variable:
    {% now "Y" as current_year %}
    Copyright {{ current_year }}

20. filter - Apply Filter To Block Content
    {% filter lower %}
        THIS WILL BE LOWERCASE
    {% endfilter %}
    
    {% filter linebreaksbr %}
        Line 1
        Line 2
    {% endfilter %}

21. autoescape - Control Automatic HTML Escaping
    {% autoescape off %}
        {{ html_content }}
    {% endautoescape %}
    
    {% autoescape on %}
        {{ user_input }}
    {% endautoescape %}

22. verbatim - Render Content Without Template Processing
    {% verbatim %}
        {{angular_variable}}
        {% django_tag %}
    {% endverbatim %}
    
    Useful For JavaScript Templates.

23. widthratio - Calculate Ratios For Scaling
    {% widthratio this_value max_value target_width %}

    Example - Progress Bar:
    <div style="width: {% widthratio score 100 200 %}px">
    
24. templatetag - Output Template Syntax Characters
    {% templatetag openblock %}  → {%
    {% templatetag closeblock %} → %}
    {% templatetag openvariable %} → {{
    {% templatetag closevariable %} → }}
    {% templatetag openbrace %} → {
    {% templatetag closebrace %} → }
    {% templatetag opencomment %} → {#
    {% templatetag closecomment %} → #}
'''

# LOCALIZATION TAGS
'''
25. localize - Control Localization
    {% load l10n %}
    {% localize on %}
        {{ value }}
    {% endlocalize %}

26. timezone - Control Timezone
    {% load tz %}
    {% timezone "America/New_York" %}
        {{ datetime }}
    {% endtimezone %}

27. localtime - Enable/Disable Conversion To Local Time
    {% load tz %}
    {% localtime on %}
        {{ datetime }}
    {% endlocaltime %}

28. trans - Translate Text
    {% load i18n %}
    {% trans "Hello" %}
    
29. blocktrans - Translate Block
    {% load i18n %}
    {% blocktrans %}
        This Is A Paragraph To Translate.
    {% endblocktrans %}
'''


# ============================================================================
# VARIABLE INJECTION AND OUTPUT ESCAPING
# ============================================================================

'''
Django Templates Automatically Escape Variables To Prevent Cross-Site Scripting (XSS) Attacks.
'''

# Injecting Variables
'''
Use Double Curly Braces To Inject Variables:
    <p>{{ variable_name }}</p>
    <p>{{ user.username }}</p>
    <p>{{ product.price }}</p>
    
Access Nested Attributes:
    {{ user.profile.bio }}
    {{ book.author.name }}
    
Access Dictionary Keys:
    {{ data.key }}
    {{ data.0 }}  # First item in list
    
Call Methods (No Parentheses):
    {{ user.get_full_name }}
    {{ article.get_absolute_url }}
'''

# Auto-Escaping
'''
Django Automatically Escapes HTML Special Characters:

Input:
    {{ "<script>alert('XSS')</script>" }}

Output:
    &lt;script&gt;alert(&#39;XSS&#39;)&lt;/script&gt;

This Prevents The Script From Being Executed In The Browser.
'''

# Disabling Auto-Escape (Use With Caution!)
'''
Method 1: safe Filter
    {{ user_input|safe }}
    {{ html_content|safe }}

Method 2: autoescape Tag
    {% autoescape off %}
        {{ html_content }}
    {% endautoescape %}

WARNING: Only Use Safe or Autoescape Off When You're Absolutely Sure 
The Content Doesn't Contain Malicious Code. Never Use With User-Generated Content!
'''

# When To Use Safe
'''
✓ Good Use Cases:
- Displaying Sanitized HTML From A WYSIWYG Editor
- Rendering Pre-Validated HTML From Database
- Displaying HTML You've Generated Yourself

✗ Never Use Safe With:
- User Input That Hasn't Been Sanitized
- Data From External Sources
- Form Submissions
'''

# Escaping Inside JavaScript
'''
Use Escapejs Filter For JavaScript Contexts:
    <script>
        var message = "{{ message|escapejs }}";
        var data = "{{ user_input|escapejs }}";
    </script>
'''

# ============================================================================
# CUSTOM TEMPLATE TAGS AND FILTERS
# ============================================================================

'''
Django allows you to create custom template Tags and Filters
To Extend Template Functionality.
'''

# Creating Custom Filters
'''
1. Create A Templatetags Directory In Your App:
    myapp/
        templatetags/
            __init__.py
            custom_filters.py

2. Define Your Filter In custom_filters.py:
'''

from django import template
register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiply The Value By The Argument"""
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''

@register.filter
def divide(value, arg):
    """Divide The Value By The Argument"""
    try:
        return value / arg
    except (ValueError, TypeError, ZeroDivisionError):
        return ''

@register.filter(name='currency')
def format_currency(value):
    """Format Value As Currency"""
    try:
        return f"${value:,.2f}"
    except (ValueError, TypeError):
        return value

'''
3. Use In Templates:
    {% load custom_filters %}
    
    {{ price|multiply:2 }}
    {{ total|divide:count }}
    {{ amount|currency }}
'''

# Creating Simple Tags
'''
1. In The Same custom_filters.py File:
'''

@register.simple_tag
def get_current_time(format_string):
    """Return Current Time Formatted"""
    from datetime import datetime
    return datetime.now().strftime(format_string)

@register.simple_tag
def multiply_values(a, b, c):
    """Multiply Three Values"""
    return a * b * c

'''
2. Use In Templates:
    {% load custom_filters %}
    
    Current Time: {% get_current_time "%Y-%m-d %H:%M:%S" %}
    Result: {% multiply_values 2 3 4 %}
'''

# Creating Inclusion Tags
'''
Inclusion Tags Render A Template With Context:

1. Define In custom_filters.py:
'''

@register.inclusion_tag('myapp/latest_posts.html')
def show_latest_posts(count=5):
    """Display Latest Posts"""
    from myapp.models import Post
    posts = Post.objects.order_by('-created_at')[:count]
    return {'posts': posts}

'''
2. Create Template myapp/templates/myapp/latest_posts.html:
    <ul>
    {% for post in posts %}
        <li>{{ post.title }}</li>
    {% endfor %}
    </ul>

3. Use In Templates:
    {% load custom_filters %}
    {% show_latest_posts 10 %}
'''

# ============================================================================
# TEMPLATE INHERITANCE AND ORGANIZATION
# ============================================================================

'''
Template Inheritance Promotes Code Reusability And Maintains
A Consistent Look Across Your Application.
'''

# Base Template Pattern
'''
Create A Base Template With Common Layout:

File: templates/base.html
'''
BASE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Website{% endblock %}</title>
    
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    
    {% block extra_css %}{% endblock %}
</head>
<body>
    <header>
        {% include "includes/navbar.html" %}
    </header>
    
    <main>
        {% if messages %}
        <div class="messages">
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                </div>
            {% endfor %}
        </div>
        {% endif %}
        
        {% block content %}
        <!-- Page content goes here -->
        {% endblock %}
    </main>
    
    <footer>
        {% include "includes/footer.html" %}
    </footer>
    
    <script src="{% static 'js/main.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
'''

# Child Template Pattern
'''
File: templates/myapp/page.html
'''
CHILD_TEMPLATE = '''{% extends "base.html" %}

{% load static %}

{% block title %}Page Title - {{ block.super }}{% endblock %}

{% block extra_css %}
<link rel="stylesheet" href="{% static 'css/page-specific.css' %}">
{% endblock %}

{% block content %}
<div class="container">
    <h1>Welcome to My Page</h1>
    <p>This is page-specific content.</p>
    
    {% for item in items %}
        <div class="item">{{ item.name }}</div>
    {% empty %}
        <p>No items available.</p>
    {% endfor %}
</div>
{% endblock %}

{% block extra_js %}
<script src="{% static 'js/page-specific.js' %}"></script>
{% endblock %}
'''

# Multi-Level Inheritance
'''
You Can Have Multiple Levels Of Inheritance:

base.html (Site-Wide Base)
    ↓
section_base.html (Section-Specific Base)
    ↓
page.html (Specific Page)
File: templates/blog/base_blog.html
'''
SECTION_BASE = '''{% extends "base.html" %}

{% block content %}
<div class="blog-layout">
    <aside class="sidebar">
        {% block sidebar %}
        {% include "blog/sidebar.html" %}
        {% endblock %}
    </aside>
    
    <article class="main-content">
        {% block blog_content %}
        {% endblock %}
    </article>
</div>
{% endblock %}
'''

'''
File: templates/blog/post_detail.html
'''
POST_TEMPLATE = '''{% extends "blog/base_blog.html" %}

{% block blog_content %}
<h1>{{ post.title }}</h1>
<p class="meta">By {{ post.author }} on {{ post.created_at|date:"F d, Y" }}</p>
<div class="content">
    {{ post.content|safe }}
</div>
{% endblock %}
'''

# ============================================================================
# CUSTOM 404 ERROR PAGE
# ============================================================================

'''
Create Custom Error Pages For Better User Experience.
'''

# 404 Template
'''
File: templates/404.html
'''
ERROR_404 = '''<!DOCTYPE html>
<html>
<head>
    <title>Page Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 50px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        h1 {
            font-size: 100px;
            margin: 0;
        }
        p {
            font-size: 24px;
            margin: 20px 0;
        }
        a {
            color: white;
            text-decoration: none;
            border: 2px solid white;
            padding: 10px 20px;
            border-radius: 5px;
            display: inline-block;
            margin-top: 20px;
            transition: all 0.3s;
        }
        a:hover {
            background: white;
            color: #667eea;
        }
    </style>
</head>
<body>
    <h1>404</h1>
    <p>Oops! The Page You're Looking For Doesn't Exist.</p>
    <p>{{ exception }}</p>
    <a href="{% url 'home' %}">Go Back Home</a>
</body>
</html>
'''

# Enable Custom 404 Page
'''
In settings.py:
    DEBUG = False
    ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']

In urls.py:
'''
URL_404_HANDLER = '''from django.conf.urls import handler404
from django.shortcuts import render

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404
'''

# Other Error Pages
'''
You Can Create Custom Pages For Other Errors:

- 400.html - Bad Request
- 403.html - Permission Denied
- 404.html - Page Not Found
- 500.html - Server Error

In urls.py:
    from django.conf.urls import handler400, handler403, handler404, handler500
    
    handler400 = 'myapp.views.custom_400'
    handler403 = 'myapp.views.custom_403'
    handler404 = 'myapp.views.custom_404'
    handler500 = 'myapp.views.custom_500'
'''

# ============================================================================
# BEST PRACTICES
# ============================================================================

'''
1. Keep Logic Out of Templates
   - Move Complex Logic To Views Or Model Methods
   - Templates Should Focus On Presentation
   
2. Use Template Inheritance
   - Create Base Templates For Common Layouts
   - Override Only Necessary Blocks
   
3. Organize Templates by App
   - templates/appname/template.html
   - Prevents Naming Conflicts
   
4. Use Includes for Reusable Components
   - Navbar, Footer, Sidebar, Etc.
   - Keep Templates DRY (Don't Repeat Yourself)
   
5. Be Careful with |safe Filter
   - Only Use With Trusted Content
   - Sanitize User Input Before Marking Safe
   
6. Use Meaningful Block Names
   - {% block content %} Instead Of {% block c %}
   - Makes Templates Self-Documenting
   
7. Comment Complex Template Logic
   - {# This Loop Displays Featured Products #}
   - Helps Future Maintainers
   
8. Load Static Files Properly
   - Always Use {% Load Static %} And {% Static %}
   - Don't Hardcode Static URLs
   
9. Use Context Processors Wisely
   - For Data Needed Across Many Templates
   - Add To TEMPLATES OPTIONS Context_processors
   
10. Test Your Templates
    - Test Template Rendering In Views
    - Verify Filter And Tag Behavior
'''

# ============================================================================
# QUICK TIPS
# ============================================================================

'''
- Use {% spaceless %} For HTML Email Templates
- Remember: Template Tags Use {% %}, Variables Use {{ }}
- Filters Can Be Chained: {{ Value|Lower|Truncatewords:5 }}
- Use {% lorem %} For Placeholder Text During Development
- {% debug %} Shows Available Context In DEBUG Mode
- {{ Variable|Pprint }} Pretty-Prints Complex Objects
- Use {% widthratio %} For Responsive Elements
- {% regroup %} Is Perfect For Categorized Lists
'''