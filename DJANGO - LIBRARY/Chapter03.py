'''Returning HTML Content As Response In Django'''
from django.http import HttpResponse
from django.shortcuts import render
def html_response_view(request):
    html_content = """
    <html>
        <head><title>Sample HTML Response</title></head>
        <body>
            <h1>Welcome to Django HTML Response</h1>
            <p>This is a sample HTML content returned as a response.</p>
        </body>
    </html>
    """
    return HttpResponse(html_content)
# To Use This View, Map It To A URL In Your Django Project's urls.py File.
# Example:
from django.urls import path
from .views import html_response_view
urlpatterns = [
    path('html-response/', html_response_view, name='html_response'),
]

# Now, When You Navigate To /html-response/ In Your Browser, You Will See The HTML Content Rendered.

#------------------
""" NAMESPACE IN DJANGO URLS """
# In Django, A Namespace Is Used To Organize URL Names And Avoid Naming Conflicts Between Different Apps Within A Project. By Using Namespaces, You Can Refer To URLs Uniquely Even If Different Apps Have URL Patterns With The Same Name.

# Here Is An Example Of How To Use Namespaces In Django URLs:
# In The Main urls.py File Of Your Project:
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
    path('shop/', include(('shop.urls', 'shop'), namespace='shop')),
]
# In The blog/urls.py File:
from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog_home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]
# In The shop/urls.py File:
from django.urls import path
from . import views
urlpatterns = [
    path('', views.shop_home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]

# Views.py File PYTHON CODE :
from django.http import HttpResponse
from django.shortcuts import render
def blog_home(request):
    return HttpResponse("Welcome to the Blog Home Page!")
def post_detail(request, post_id):
    return HttpResponse(f"Blog Post Detail Page For Post ID: {post_id}")
def shop_home(request):
    return HttpResponse("Welcome to the Shop Home Page!")
def product_detail(request, product_id):
    return HttpResponse(f"Shop Product Detail Page For Product ID: {product_id}")
# In This Example, We Have Two Apps: blog And shop. Each App Has Its Own urls.py File With URL Patterns That Share The Same Name ('home'). By Using Namespaces, We Can Refer To Each URL Uniquely Without Any Conflicts.


# Now, To Refer To The blog Home URL, You Would Use The Namespace 'blog' Like This:
# blog/views.py (Or shop/views.py)
from django.http import HttpResponse
from django.urls import reverse  # Import here
from django.shortcuts import redirect

def some_view(request):
    # Example: Use reverse() To Generate A URL For Redirection
    blog_home_url = reverse('blog:home')  # Generates '/blog/'
    
    # Redirect to the blog home
    return redirect(blog_home_url)

# Similarly, To Refer To The shop Product Detail URL, You Would Use The Namespace 'shop' Like This:
shop_product_url = reverse('shop:product_detail', args=[42])  # Assuming 42 Is The Product ID
# By Using Namespaces, You Can Clearly Distinguish Between URLs From Different Apps, Even If They Share The Same Name. This Is Particularly Useful In Larger Projects With Multiple Apps.

#------------------
''' NAMED URLS IN DJANGO '''
# Named URLs In Django Allow You To Assign A Name To A Specific URL Pattern, Making It Easier To Refer To That URL Throughout Your Project. This Is Especially Useful When You Need To Change The URL Pattern Later, As You Only Need To Update It In One Place (The urls.py File) Instead Of Everywhere The URL Is Used.

# Using Named URLs In Templates:
# In Your HTML Templates, You Can Use The {% url %} Template Tag To Refer To
# Named URLs. This Is Helpful For Creating Links That Are Easy To Maintain.
# Example In A Template (e.g., base.html):
'''<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{% url 'home' %}">Home</a></li>
            <li><a href="{% url 'about' %}">About</a></li>
            <li><a href="{% url 'contact' %}">Contact</a></li>
        </ul>
    </nav>
    <div>
        {% block content %}
        <!-- Page-specific content will go here -->
        {% endblock %}
    </div>
</body>
</html>'''
# In This Example, The {% url %} Tag Generates The Correct URL Based On The Named URL Patterns Defined In urls.py. If You Later Change The URL Pattern For 'about' From 'about/' To 'about-us/', You Only Need To Update It In urls.py, And All Links Using {% url 'about' %} Will Automatically Reflect The Change.