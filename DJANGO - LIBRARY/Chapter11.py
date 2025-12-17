"""
====================================
CHAPTER 11: CLASS-BASED VIEWS (CBV)
====================================

Class-Based Views Provide An Object-Oriented Way To Organize View Logic. They Offer
Code Reusability Through Inheritance And Mixins, Making Complex Views Easier To Manage.

Topics Covered:
1. Introduction To Class-Based Views
2. Generic Display Views
3. Generic Editing Views
4. Mixins And Custom Views
5. Form Handling With CBVs
6. Advanced CBV Patterns
7. Method Flow And Hooks
8. Best Practices
"""

#==============================================================================
# 1. INTRODUCTION TO CLASS-BASED VIEWS
#==============================================================================

"""
Class-Based Views (CBVs) Allow You To Structure Your Views Using Classes Instead
Of Functions. They Provide Code Reuse Through Inheritance And Mixins.

FUNCTION-BASED VIEW vs CLASS-BASED VIEW
"""

# Function-Based View (FBV)
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book

def book_list(request):
    """Traditional Function-Based View."""
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_detail(request, pk):
    """Traditional Function-Based View With Parameter."""
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


# Class-Based View (CBV)
from django.views import View
from django.views.generic import ListView, DetailView

class BookListView(ListView):
    """Class-Based View For Listing Books."""
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    """Class-Based View For Book Details."""
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


# Base View class
class CustomView(View):
    """
    Most Basic CBV - All Other Generic Views Inherit From View.
    You Must Implement HTTP Method Handlers (Get, Post, Etc.)
    """
    
    def get(self, request, *args, **kwargs):
        """Handle GET Requests."""
        return HttpResponse('This is a GET request')
    
    def post(self, request, *args, **kwargs):
        """Handle POST Requests."""
        return HttpResponse('This is a POST request')


# URLs Configuration For CBVs
"""
# urls.py
from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    # Use .as_view() To Convert CBV To View Function
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
"""


#==============================================================================
# 2. GENERIC DISPLAY VIEWS
#==============================================================================

"""
Django Provides Several Generic Views For Common Display Patterns.
"""

# ListView - Display List Of Objects
from django.views.generic import ListView

class BookListView(ListView):
    """
    Display A List Of Books.
    
    Automatic Context Variable: 'object_list' or 'book_list'
    Default Template: 'app_name/book_list.html'
    """
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'  # Rename 'object_list' To 'books'
    paginate_by = 10  # Enable Pagination
    ordering = ['-created_at']  # Order By Newest First
    
    def get_queryset(self):
        """
        Override To Customize The Queryset.
        Useful For Filtering, Searching, Etc.
        """
        queryset = super().get_queryset()
        # Add Custom Filtering
        genre = self.request.GET.get('genre')
        if genre:
            queryset = queryset.filter(genre=genre)
        return queryset
    
    def get_context_data(self, **kwargs):
        """
        Add Extra Context To Template.
        """
        context = super().get_context_data(**kwargs)
        context['genres'] = Book.objects.values_list('genre', flat=True).distinct()
        context['total_books'] = self.get_queryset().count()
        return context


# DetailView - Display Single Object Details
from django.views.generic import DetailView

class BookDetailView(DetailView):
    """
    Display Details Of A Single Book.
    
    Automatic Context Variable: 'object' or 'book'
    Default Template: 'app_name/book_detail.html'
    """
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):
        """Add Related Data To Context."""
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['related_books'] = Book.objects.filter(
            author=book.author
        ).exclude(pk=book.pk)[:5]
        return context


# TemplateView - Render A Template With Context
from django.views.generic import TemplateView

class AboutView(TemplateView):
    """
    Simple Template Rendering View.
    Use When You Don't Need A Specific Model.
    """
    template_name = 'about.html'
    
    def get_context_data(self, **kwargs):
        """Add Context Data."""
        context = super().get_context_data(**kwargs)
        context['company_name'] = 'My Bookstore'
        context['year'] = 2024
        return context


# Template In 'books/book_list.html'
"""
{% extends "base.html" %}

{% block content %}
    <h1>Books ({{ total_books }})</h1>
    
    <!-- Filter form -->
    <form method="get">
        <select name="genre">
            <option value="">All Genres</option>
            {% for genre in genres %}
                <option value="{{ genre }}">{{ genre }}</option>
            {% endfor %}
        </select>
        <button type="submit">Filter</button>
    </form>
    
    <!-- Book List -->
    <ul>
        {% for book in books %}
            <li>
                <a href="{% url 'book_detail' book.pk %}">
                    {{ book.title }} by {{ book.author }}
                </a>
            </li>
        {% endfor %}
    </ul>
    
    <!-- Pagination -->
    {% if is_paginated %}
        <div class="pagination">
            {% if page_obj.has_previous %}
                <a href="?page=1">First</a>
                <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
            {% endif %}
            
            <span>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>
            
            {% if page_obj.has_next %}
                <a href="?page={{ page_obj.next_page_number }}">Next</a>
                <a href="?page={{ page_obj.paginator.num_pages }}">Last</a>
            {% endif %}
        </div>
    {% endif %}
{% endblock %}
"""


#==============================================================================
# 3. GENERIC EDITING VIEWS
#==============================================================================

"""
Generic Views For Creating, Updating, And Deleting Objects.
"""

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BookForm


# CreateView - Create New Object
class BookCreateView(LoginRequiredMixin, CreateView):
    """
    Create A New Book.
    
    Automatic Template: 'app_name/book_form.html'
    """
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')  # Redirect After Successful Creation
    
    def form_valid(self, form):
        """
        Called When Form Validation Succeeds.
        Useful For Setting Additional Fields.
        """
        form.instance.owner = self.request.user  # Set The Owner
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        """Add Extra Context."""
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Book'
        context['button_text'] = 'Create'
        return context


# UpdateView - Update Existing Object
class BookUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update An Existing Book.
    
    Automatic Template: 'app_name/book_form.html' (Same As CreateView)
    """
    model = Book
    form_class = BookForm
    template_name = 'books/book_form.html'
    
    def get_success_url(self):
        """Dynamic Redirect To Book Detail Page."""
        return reverse_lazy('book_detail', kwargs={'pk': self.object.pk})
    
    def get_context_data(self, **kwargs):
        """Add Extra Context."""
        context = super().get_context_data(**kwargs)
        context['title'] = f'Edit: {self.object.title}'
        context['button_text'] = 'Update'
        return context
    
    def get_queryset(self):
        """Ensure Users Can Only Edit Their Own Books."""
        return super().get_queryset().filter(owner=self.request.user)


# DeleteView - Delete Object
class BookDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete A Book.
    
    Automatic Template: 'app_name/book_confirm_delete.html'
    """
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
    
    def get_queryset(self):
        """Ensure Users Can Only Delete Their Own Books."""
        return super().get_queryset().filter(owner=self.request.user)


# Shared Form Template For Create And Update
"""
<!-- books/book_form.html -->
{% extends "base.html" %}

{% block content %}
    <h1>{{ title }}</h1>
    
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">{{ button_text }}</button>
        <a href="{% url 'book_list' %}">Cancel</a>
    </form>
{% endblock %}
"""

# Delete Confirmation Template
"""
<!-- books/book_confirm_delete.html -->
{% extends "base.html" %}

{% block content %}
    <h1>Delete Book</h1>
    
    <p>Are You Sure You Want To Delete "{{ book.title }}"?</p>
    
    <form method="post">
        {% csrf_token %}
        <button type="submit">Yes, Delete</button>
        <a href="{% url 'book_detail' book.pk %}">Cancel</a>
    </form>
{% endblock %}
"""


#==============================================================================
# 4. MIXINS AND CUSTOM VIEWS
#==============================================================================

"""
Mixins Are Reusable Components That Add Specific Functionality To Views.
"""

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import DetailView


# LoginRequiredMixin - Require Authentication
class ProtectedBookDetailView(LoginRequiredMixin, DetailView):
    """Only Authenticated Users Can View Book Details."""
    model = Book
    template_name = 'books/book_detail.html'
    login_url = '/login/'  # Where To Redirect If Not Authenticated
    redirect_field_name = 'next'  # Query Parameter Name


# PermissionRequiredMixin - Require Specific Permission
class BookManageView(PermissionRequiredMixin, UpdateView):
    """Only Users With 'books.change_book' Permission Can Edit."""
    model = Book
    form_class = BookForm
    permission_required = 'books.change_book'
    raise_exception = True  # Raise 403 Instead Of Redirect


# UserPassesTestMixin - Custom Test Condition
class BookOwnerUpdateView(UserPassesTestMixin, UpdateView):
    """Only The Book Owner Can Edit."""
    model = Book
    form_class = BookForm
    
    def test_func(self):
        """Test If Current User Is The Book Owner."""
        book = self.get_object()
        return book.owner == self.request.user


# Custom Mixin - Create Your Own Reusable Components
class SetOwnerMixin:
    """
    Automatically Set The Owner Field To Current User.
    Use With CreateView Or UpdateView.
    """
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class AddUserToContextMixin:
    """
    Add Current User To Template Context.
    """
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        return context


# Using Custom Mixins
class BookCreateWithOwnerView(SetOwnerMixin, AddUserToContextMixin, CreateView):
    """Create View Using Custom Mixins."""
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('book_list')


# FormView - Handle Forms Without a Model
from django.views.generic.edit import FormView
from django.core.mail import send_mail

class ContactFormView(FormView):
    """Handle Contact Form Submissions."""
    template_name = 'contact.html'
    form_class = ContactForm  # Your Form Class
    success_url = reverse_lazy('contact_success')
    
    def form_valid(self, form):
        """Process The Form Data."""
        # Send Email
        send_mail(
            subject=form.cleaned_data['subject'],
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@example.com'],
        )
        return super().form_valid(form)


#==============================================================================
# 5. FORM HANDLING WITH CBVs
#==============================================================================

"""
Advanced Form Handling Patterns With Class-Based Views.
"""

from django.views.generic.edit import FormView
from django.contrib import messages


class MultiStepFormView(FormView):
    """
    Example Of Multi-Step Form Handling.
    """
    template_name = 'forms/step.html'
    form_class = StepOneForm
    
    def get_form_class(self):
        """Return Different Form Based On Current Step."""
        step = self.request.session.get('step', 1)
        return {
            1: StepOneForm,
            2: StepTwoForm,
            3: StepThreeForm,
        }.get(step, StepOneForm)
    
    def form_valid(self, form):
        """Save Form Data To Session And Proceed To Next Step."""
        step = self.request.session.get('step', 1)
        
        # Save Form Data To Session
        self.request.session[f'step_{step}_data'] = form.cleaned_data
        
        if step < 3:
            # Move To Next Step
            self.request.session['step'] = step + 1
            return self.render_to_response(self.get_context_data())
        else:
            # Final Step - Process All Data
            self.process_complete_form()
            messages.success(self.request, 'Form Submitted Successfully!')
            return super().form_valid(form)
    
    def process_complete_form(self):
        """Process All Steps' Data."""
        step_1 = self.request.session.get('step_1_data', {})
        step_2 = self.request.session.get('step_2_data', {})
        step_3 = self.request.session.get('step_3_data', {})
        
        # Combine And Process Data
        # ...
        
        # Clear Session
        for key in ['step', 'step_1_data', 'step_2_data', 'step_3_data']:
            self.request.session.pop(key, None)


class AjaxFormView(FormView):
    """
    Handle AJAX Form Submissions.
    """
    template_name = 'forms/ajax_form.html'
    form_class = BookForm
    
    def form_valid(self, form):
        """Return JSON Response For AJAX Requests."""
        if self.request.is_ajax():
            form.save()
            return JsonResponse({
                'success': True,
                'message': 'Book Created Successfully!'
            })
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """Return JSON Errors For AJAX Requests."""
        if self.request.is_ajax():
            return JsonResponse({
                'success': False,
                'errors': form.errors
            }, status=400)
        return super().form_invalid(form)


#==============================================================================
# 6. ADVANCED CBV PATTERNS
#==============================================================================

"""
Complex Patterns And Real-World Examples.
"""

# Multiple Models In One View
class BookWithReviewsView(DetailView):
    """Display Book With Reviews And Review Form."""
    model = Book
    template_name = 'books/book_with_reviews.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['reviews'] = book.reviews.all()
        context['review_form'] = ReviewForm()
        return context
    
    def post(self, request, *args, **kwargs):
        """Handle Review Form Submission."""
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            review = form.save(commit=False)
            review.book = self.object
            review.user = request.user
            review.save()
            messages.success(request, 'Review Added Successfully!')
            return redirect('book_detail', pk=self.object.pk)
        
        # Form Invalid - Re-Render With Errors
        context = self.get_context_data(**kwargs)
        context['review_form'] = form
        return self.render_to_response(context)


# Search view
class BookSearchView(ListView):
    """Search Books By Title, Author, Or Genre."""
    model = Book
    template_name = 'books/search_results.html'
    context_object_name = 'books'
    paginate_by = 20
    
    def get_queryset(self):
        """Filter Books Based On Search Query."""
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '')
        
        if query:
            from django.db.models import Q
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(author__name__icontains=query) |
                Q(genre__icontains=query)
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


# Archive View By Date  
from django.views.generic.dates import YearArchiveView, MonthArchiveView

class BookYearArchiveView(YearArchiveView):
    """Display Books Published In A Specific Year."""
    model = Book
    date_field = 'publication_date'
    make_object_list = True
    allow_future = False


class BookMonthArchiveView(MonthArchiveView):
    """Display Books Published In A Specific Month."""
    model = Book
    date_field = 'publication_date'
    month_format = '%m'


# Export View
import csv
from django.http import HttpResponse

class BookExportView(View):
    """Export Books To CSV."""
    
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="books.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Title', 'Author', 'Price', 'Genre'])
        
        books = Book.objects.all()
        for book in books:
            writer.writerow([
                book.title,
                book.author.name,
                book.price,
                book.genre
            ])
        
        return response


#==============================================================================
# 7. METHOD FLOW AND HOOKS
#==============================================================================

"""
Understanding The Method Flow In CBVs Helps You Know Where To Customize Behavior.

DETAILVIEW METHOD FLOW:
1. dispatch() - Entry Point, Checks HTTP Method
2. get() - Handles GET Requests
3. get_object() - Retrieves The Object
4. get_context_data() - Builds Template Context
5. render_to_response() - Renders Template
CREATEVIEW METHOD FLOW:
1. dispatch()
2. get() or post()
3. get_form_class()
4. get_form()
5. form_valid() or form_invalid()
6. get_success_url()
"""

class DetailedBookDetailView(DetailView):
    """Example Showing All Customizable Hooks."""
    model = Book
    
    def dispatch(self, request, *args, **kwargs):
        """
        Called First. Determines HTTP Method Handling.
        Use For: Early Validation, Logging
        """
        print(f"User {request.user} accessing book detail")
        return super().dispatch(request, *args, **kwargs)
    
    def get_object(self, queryset=None):
        """
        Retrieve The Object To Display.
        Use For: Custom Object Lookup, Access Control
        """
        obj = super().get_object(queryset)
        # Track view count
        obj.view_count += 1
        obj.save(update_fields=['view_count'])
        return obj
    
    def get_queryset(self):
        """
        Get The Base Queryset.
        Use For: Filtering, Optimization (select_related)
        """
        return super().get_queryset().select_related('author')
    
    def get_context_data(self, **kwargs):
        """
        Add Extra Data To Template Context.
        Use For: Adding Related Data, Calculations
        """
        context = super().get_context_data(**kwargs)
        context['related_books'] = Book.objects.filter(
            author=self.object.author
        )[:5]
        return context
    
    def get_template_names(self):
        """
        Determine Which Template To Use.
        Use For: Dynamic Template Selection
        """
        if self.request.user.is_authenticated:
            return ['books/book_detail_auth.html']
        return ['books/book_detail.html']


#==============================================================================
# 8. BEST PRACTICES
#==============================================================================

"""
WHEN TO USE CBVs vs FBVs:

Use CBVs When:
- You Need Standard CRUD Operations
- You Want To Reuse Code Through Inheritance
- The View Logic Is Complex And Benefits From Organization
- You're Building REST APIs (With DRF)

Use FBVs When:
- The View Logic Is Simple And Straightforward
- You Need Maximum Flexibility
- The View Doesn't Fit Standard Patterns
- You're More Comfortable With Functions

CBV BEST PRACTICES:

1. Keep Views Simple - Move Complex Logic To Models, Managers, Or Services
2. Use Mixins For Reusable Functionality
3. Override Methods, Don't Duplicate Code
4. Use Meaningful Names For Context Variables
5. Document Custom Behavior
6. Consider Using get_queryset() For Filtering Instead Of Modifying Queryset Attribute
""" 

# Good Example - Clean And Focused
class BookListView(LoginRequiredMixin, ListView):
    """Display List Of Available Books."""
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'books'
    paginate_by = 20
    
    def get_queryset(self):
        return Book.objects.available().select_related('author')


# Bad Example - Too Much Logic In View
class BadBookListView(ListView):
    """Don't Do This - Too Much Logic In View."""
    model = Book
    
    def get_queryset(self):
        # Complex Business Logic Belongs In Model Manager
        queryset = Book.objects.all()
        for book in queryset:
            if book.stock > 0:
                book.status = 'Available'
            else:
                book.status = 'Out Of Stock'
            # This Should Be In Save() Method Or Signal
            if book.price < 10:
                book.discount = 0.1
            book.save()
        return queryset


# URLs.py Example For All Views
"""
from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    # List And Detail
    path('', views.BookListView.as_view(), name='list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='detail'),
    
    # CRUD Operations
    path('create/', views.BookCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='delete'),
    
    # Search And Filter
    path('search/', views.BookSearchView.as_view(), name='search'),
    
    # Archives
    path('archive/<int:year>/', views.BookYearArchiveView.as_view(), name='year_archive'),
    path('archive/<int:year>/<int:month>/', views.BookMonthArchiveView.as_view(), name='month_archive'),
    
    # Export
    path('export/', views.BookExportView.as_view(), name='export'),
]
"""

"""
SUMMARY:

Class-Based Views Provide:
✅ Code Reusability Through Inheritance
✅ Organized Structure For Complex Views
✅ Built-In Handling For Common Patterns
✅ Mixins For Composable Functionality
✅ Less Boilerplate Code

Remember:
- Start With Generic Views (ListView, DetailView, etc.)
- Use Mixins For Cross-Cutting Concerns (Auth, Permissions)
- Override Specific Methods For Customization
- Keep Business Logic In Models/Managers
- Choose CBVs Or FBVs Based On The Use Case
"""

# End of Chapter 11: Class-Based Views