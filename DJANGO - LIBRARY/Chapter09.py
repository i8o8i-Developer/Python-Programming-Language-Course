# ============================================================================
# DJANGO FORMS
# ============================================================================

'''
Django Forms Provide A Powerful Way To Handle User Input, Validate Data,
And Render HTML Forms. This Chapter Covers Everything From Basic Forms
To Advanced Form Customization.
'''

# ============================================================================
# WHY USE DJANGO FORMS?
# ============================================================================

'''
Benefits of Django Forms:
- Automatic HTML Generation
- Data Validation (Server-Side)
- Security (CSRF Protection, XSS Prevention)
- Error Handling
- Data Cleaning And Conversion
- Reusability
- Integration With Models

Django Forms Handle The Entire Form Lifecycle:
1. Display The Form (GET Request)
2. Receive Form Data (POST Request)
3. Validate The Data
4. Clean The Data
5. Save Or Process The Data
6. Display Errors If Validation Fails
'''

# ============================================================================
# CREATING A BASIC FORM
# ============================================================================

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Your Name',
        help_text='Enter Your Full Name'
    )
    email = forms.EmailField(
        label='Email Address',
        help_text='We Will Never Share Your Email'
    )
    subject = forms.CharField(
        max_length=200,
        label='Subject'
    )
    message = forms.CharField(
        widget=forms.Textarea,
        label='Message',
        help_text='Enter Your Message Here'
    )
    cc_myself = forms.BooleanField(
        required=False,
        label='Send Me A Copy'
    )

'''
Form Field Types:
- CharField - Text input
- EmailField - Email Input With Validation
- IntegerField - Integer Numbers
- FloatField - Floating Point Numbers
- DecimalField - Precise Decimal Numbers
- BooleanField - Checkbox
- ChoiceField - Select Dropdown
- MultipleChoiceField - Multiple Checkboxes
- DateField - Date Input
- TimeField - Time Input
- DateTimeField - Date And Time Input
- FileField - File Upload
- ImageField - Image Upload
- URLField - URL Input With Validation
- SlugField - Slug Input
'''

# ============================================================================
# USING FORMS IN VIEWS
# ============================================================================

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Function-Based View
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Access Cleaned Data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Process The Data (Send Email, Save To DB, Etc.)
            # send_email(email, subject, message)
            
            messages.success(request, 'Your Message Has Been Sent!')
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})

# Class-Based View
from django.views.generic.edit import FormView

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/contact/success/'
    
    def form_valid(self, form):
        # Process form Data
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        # Send email, save data, etc.
        messages.success(self.request, 'Message Sent Successfully!')
        return super().form_valid(form)

# ============================================================================
# RENDERING FORMS IN TEMPLATES
# ============================================================================

'''
Basic Form Rendering:

<!-- templates/contact.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    
    <form method="post">
        {% csrf_token %}
        
        <!-- Method 1: Render Entire Form At Once -->
        {{ form.as_p }}  <!-- As Paragraphs -->
        <!-- {{ form.as_table }} -->  <!-- As Table Rows -->
        <!-- {{ form.as_ul }} -->     <!-- As List Items -->
        
        <button type="submit">Send Message</button>
    </form>
</body>
</html>
'''

'''
Manual Field Rendering For More Control:

<form method="post">
    {% csrf_token %}
    
    <!-- Display Non-Field Errors -->
    {% if form.non_field_errors %}
        <div class="alert alert-danger">
            {{ form.non_field_errors }}
        </div>
    {% endif %}
    
   <!-- Render Each Field Manually -->
    <div class="form-group">
        {{ form.name.label_tag }}
        {{ form.name }}
        {% if form.name.errors %}
            <div class="error">{{ form.name.errors }}</div>
        {% endif %}
        {% if form.name.help_text %}
            <small>{{ form.name.help_text }}</small>
        {% endif %}
    </div>
    
    <div class="form-group">
        {{ form.email.label_tag }}
        {{ form.email }}
        {% if form.email.errors %}
            <div class="error">{{ form.email.errors }}</div>
        {% endif %}
    </div>
    
    <div class="form-group">
        {{ form.message.label_tag }}
        {{ form.message }}
        {% if form.message.errors %}
            <div class="error">{{ form.message.errors }}</div>
        {% endif %}
    </div>
    
    <div class="form-check">
        {{ form.cc_myself }}
        {{ form.cc_myself.label_tag }}
    </div>
    
    <button type="submit" class="btn btn-primary">Send</button>
</form>
'''

'''
Loop Through All Fields:

<form method="post">
    {% csrf_token %}
    
    {% for field in form %}
        <div class="form-group">
            {{ field.label_tag }}
            {{ field }}
            
            {% if field.errors %}
                <div class="error">
                    {{ field.errors }}
                </div>
            {% endif %}
            
            {% if field.help_text %}
                <small class="form-text text-muted">
                    {{ field.help_text }}
                </small>
            {% endif %}
        </div>
    {% endfor %}
    
    <button type="submit">Submit</button>
</form>
'''

# ============================================================================
# FORM VALIDATION
# ============================================================================
# NOTE: Basic Validation Is Already Covered At The Beginning Of This Chapter.
# See ContactForm Example At Line 40 For Field-Level And Form-Level Validation.
# For Advanced Validation Patterns, See Chapter14.py

# Custom Validators
from django.core.exceptions import ValidationError

def validate_even(value):
    """Custom Validator Function"""
    if value % 2 != 0:
        raise ValidationError(
            f'{value} Is Not An Even Number',
            code='not_even'
        )

class MyForm(forms.Form):
    even_number = forms.IntegerField(
        validators=[validate_even]
    )

# ============================================================================
# MODEL FORMS
# ============================================================================

'''
ModelForms Automatically Create Forms From Django Models,
Handling Field Types, Validation, And Saving To Database.
''' 

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

# Create ModelForm
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'  # Include All Fields
        # OR Specify Fields
        # fields = ['title', 'author', 'isbn', 'published_date']
        # OR Exclude Fields
        # exclude = ['is_available']
        
        # Custom labels
        labels = {
            'isbn': 'ISBN Number',
            'published_date': 'Publication Date',
        }
        
        # Help Text
        help_texts = {
            'isbn': 'Enter 13-Digit ISBN',
            'pages': 'Total Number Of Pages',
        }
        
        # Error Messages
        error_messages = {
            'title': {
                'required': 'Please Enter A Book Title',
                'max_length': 'Title Is Too Long',
            },
        }
        
        # Widgets For Custom Rendering
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 5,
                'cols': 40,
                'placeholder': 'Enter Book Description'
            }),
            'published_date': forms.DateInput(attrs={
                'type': 'date'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Book Title'
            }),
        }

# Using ModelForm in Views
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create View
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()  # Save To Database
            messages.success(request, f'Book "{book.title}" created!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    
    return render(request, 'books/form.html', {'form': form})

# Update View
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            messages.success(request, f'Book "{book.title}" updated!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    
    return render(request, 'books/form.html', {
        'form': form,
        'book': book
    })

# Save Without Committing (For Additional Processing)
def book_create_advanced(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)  # Don't Save Yet
            book.created_by = request.user  # Add Extra Data
            book.slug = slugify(book.title)
            book.save()  # Now Save
            messages.success(request, 'Book Created Successfully!')
            return redirect('book_list')
    else:
        form = BookForm()
    
    return render(request, 'books/form.html', {'form': form})

# ============================================================================
# FORMSETS
# ============================================================================

'''
Formsets Allow You To Work With Multiple Forms On The Same Page.
'''

from django.forms import formset_factory, modelformset_factory, inlineformset_factory

# Basic Formset
class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)

# Create Formset
ArticleFormSet = formset_factory(ArticleForm, extra=3)

# In View
def manage_articles(request):
    if request.method == 'POST':
        formset = ArticleFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    title = form.cleaned_data['title']
                    content = form.cleaned_data['content']
                    # Save Or Process Data
            return redirect('success')
    else:
        formset = ArticleFormSet()
    
    return render(request, 'articles.html', {'formset': formset})

# ModelFormSet
from .models import Book

BookFormSet = modelformset_factory(
    Book,
    fields=['title', 'author', 'price'],
    extra=1,  # Number of Empty Forms
    can_delete=True  # Allow Deletion
)

def manage_books(request):
    if request.method == 'POST':
        formset = BookFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Books Updated!')
            return redirect('book_list')
    else:
        formset = BookFormSet(queryset=Book.objects.all())
    
    return render(request, 'books/manage.html', {'formset': formset})

# Inline Formset (For Related Models)
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

# Create Inline Formset
BookInlineFormSet = inlineformset_factory(
    Author,  # Parent Model
    Book,    # Child Model
    fields=['title', 'published_date'],
    extra=2,
    can_delete=True
)

def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)
    
    if request.method == 'POST':
        formset = BookInlineFormSet(request.POST, instance=author)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Author and Books Updated!')
            return redirect('author_detail', pk=author.pk)
    else:
        formset = BookInlineFormSet(instance=author)
    
    return render(request, 'author_edit.html', {
        'author': author,
        'formset': formset
    })

# Render Formset In Template
'''
<form method="post">
    {% csrf_token %}
    
    {{ formset.management_form }}
    
    {% for form in formset %}
        <div class="formset-form">
            {{ form.as_p }}
        </div>
    {% endfor %}
    
    <button type="submit">Save All</button>
</form>
'''

# ============================================================================
# FORM WIDGETS
# ============================================================================

'''
Widgets Control How Form Fields Are Rendered In HTML.
'''

from django import forms
from django.forms import widgets

class CustomForm(forms.Form):
    # Text Inputs
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Name',
        'maxlength': 100
    }))
    
    # Textarea
    description = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 5,
        'cols': 40,
        'class': 'form-control'
    }))
    
    # Select dropdown
    CATEGORY_CHOICES = [
        ('tech', 'Technology'),
        ('science', 'Science'),
        ('art', 'Art'),
    ]
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Radio Buttons
    gender = forms.ChoiceField(
        choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')],
        widget=forms.RadioSelect
    )
    
    # Checkboxes
    HOBBY_CHOICES = [
        ('reading', 'Reading'),
        ('sports', 'Sports'),
        ('music', 'Music'),
    ]
    hobbies = forms.MultipleChoiceField(
        choices=HOBBY_CHOICES,
        widget=forms.CheckboxSelectMultiple
    )
    
    # Date Picker
    birth_date = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date',
        'class': 'form-control'
    }))
    
    # Time Picker
    appointment_time = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'time'
    }))
    
    # DateTime Picker
    event_datetime = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'type': 'datetime-local'
    }))
    
    # Number Input
    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'min': 0,
        'max': 120,
        'step': 1
    }))
    
    # Password Input
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Password'
    }))
    
    # Hidden Input
    user_id = forms.IntegerField(widget=forms.HiddenInput())
    
    # Email Input
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'email@example.com'
    }))
    
    # URL Input
    website = forms.URLField(widget=forms.URLInput(attrs={
        'placeholder': 'https://example.com'
    }))
    
    # File Upload
    document = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'accept': '.pdf,.doc,.docx'
    }))
    
    # Image Upload
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        'accept': 'image/*'
    }))

# ============================================================================
# FILE UPLOADS
# ============================================================================

from django.core.files.storage import FileSystemStorage

# Form With File Upload
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

# View Handling File Upload
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            
            # Save Using FileSystemStorage
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_url = fs.url(filename)
            
            return render(request, 'upload_success.html', {
                'file_url': file_url
            })
    else:
        form = UploadFileForm()
    
    return render(request, 'upload.html', {'form': form})

# ModelForm With File Upload
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file', 'description']
        widgets = {
            'file': forms.FileInput(attrs={
                'accept': '.pdf,.doc,.docx,.txt'
            })
        }

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.uploaded_by = request.user
            document.save()
            messages.success(request, 'Document Uploaded Successfully!')
            return redirect('document_list')
    else:
        form = DocumentForm()
    
    return render(request, 'upload_document.html', {'form': form})

# Multiple File Upload
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class MultipleFileUploadForm(forms.Form):
    files = MultipleFileField()

# ============================================================================
# FORM CUSTOMIZATION
# ============================================================================

# Dynamic Form Fields
class DynamicForm(forms.Form):
    def __init__(self, *args, **kwargs):
        categories = kwargs.pop('categories', [])
        super().__init__(*args, **kwargs)
        
        # Add Dynamic Field
        if categories:
            self.fields['category'] = forms.ChoiceField(
                choices=[(c.id, c.name) for c in categories]
            )

# In View
def my_view(request):
    categories = Category.objects.all()
    form = DynamicForm(categories=categories)
    return render(request, 'form.html', {'form': form})

# Form With Initial Data
form = ContactForm(initial={
    'name': 'John Doe',
    'email': 'john@example.com'
})

# Readonly Fields
class ReadOnlyForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make Fields Readonly
        for field in self.fields:
            self.fields[field].widget.attrs['readonly'] = True
            self.fields[field].widget.attrs['disabled'] = True

# ============================================================================
# BEST PRACTICES
# ============================================================================

'''
1. Always Use CSRF pPotection
   - Include {% csrf_token %} In Forms
   
2. Validate On Server-Side
   - Never Trust Client-Side Validation Alone
   
3. Use ModelForms When Possible
   - Less Code, Automatic Validation
   
4. Clean Data In Clean_ Methods
   - Use clean_fieldname() For Field Validation
   - Use clean() For Cross-Field Validation
   
5. Provide Helpful Error Messages
   - Custom Error Messages In Meta Class
   - User-Friendly Validation Errors
   
6. Use Widgets For Better UX
   - Add CSS Classes
   - Use Appropriate HTML5 Input Types
   
7. Handle Files Properly
   - Check File Size
   - Validate File Types
   - Use Secure File Storage
   
8. Use Form Prefixes For Multiple Forms
   - Prevents Field Name Conflicts
   - form1 = Form1(prefix='form1')
   
9. Test Forms Thoroughly
   - Test Validation Logic
   - Test Edge Cases
   - Test Security
   
10. Keep Forms Simple
    - One Form Per Purpose
    - Split Complex Forms Into Steps
''' 

# ============================================================================
# COMMON FORM PATTERNS
# ============================================================================

# Form With AJAX Submission
'''
<form id="contactForm" method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>

<script>
document.getElementById('contactForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    
    fetch('{% url "contact" %}', {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Form Submitted Successfully!');
        } else {
            alert('Error: ' + data.errors);
        }
    });
});
</script>
'''

# Multi-Step Form
class Step1Form(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

class Step2Form(forms.Form):
    address = forms.CharField()
    phone = forms.CharField()

def multi_step_form(request):
    if request.method == 'POST':
        step = request.POST.get('step', '1')
        
        if step == '1':
            form = Step1Form(request.POST)
            if form.is_valid():
                # Save To Session
                request.session['step1_data'] = form.cleaned_data
                return render(request, 'step2.html', {
                    'form': Step2Form()
                })
        elif step == '2':
            form = Step2Form(request.POST)
            if form.is_valid():
                # Combine Data From Both Steps
                step1_data = request.session.get('step1_data', {})
                step2_data = form.cleaned_data
                
                # Process Complete Data
                # save_data(step1_data, step2_data)
                
                return redirect('success')
    else:
        form = Step1Form()
    
    return render(request, 'step1.html', {'form': form})