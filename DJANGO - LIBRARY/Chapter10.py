# ============================================================================
# DJANGO ADMIN CUSTOMIZATION
# ============================================================================

'''
The Django Admin Interface Is A Powerful Built-in Feature That Provides
A Production-Ready Admin Panel. This Chapter Covers How To Customize It
To Fit Your Needs.
'''

# ============================================================================
# BASIC ADMIN REGISTRATION
# ============================================================================

from django.contrib import admin
from .models import Book, Author, Publisher

# Simple registration
admin.site.register(Book)

# Using Decorator
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

# Multiple Models At Once
admin.site.register([Publisher, Category, Tag])

# ============================================================================
# MODEL ADMIN CUSTOMIZATION
# ============================================================================

from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # List Display - Columns To Show
    list_display = ['title', 'author', 'published_date', 'price', 'is_available']
    
    # List Filter - Sidebar Filters
    list_filter = ['is_available', 'published_date', 'author']
    
    # Search Fields
    search_fields = ['title', 'author', 'isbn']
    
    # Fields To Display In Detail View
    fields = ['title', 'author', 'isbn', 'published_date', 'price', 'description']
    
    # Readonly Fields
    readonly_fields = ['isbn', 'created_at', 'updated_at']
    
    # Ordering
    ordering = ['-published_date', 'title']
    
    # Items Per Page
    list_per_page = 25
    
    # Date Hierarchy Navigation
    date_hierarchy = 'published_date'
    
    # Editable Fields In List View
    list_editable = ['price', 'is_available']
    
    # Display As Links In List View
    list_display_links = ['title']
    
    # Prepopulated Fields (for Slugs)
    prepopulated_fields = {'slug': ('title',)}
    
    # Auto-complete For Foreign Keys (Requires search_fields On Related Model)
    autocomplete_fields = ['author', 'publisher']
    
    # Raw ID Fields (Shows ID Input Instead Of Dropdown)
    raw_id_fields = ['author']  
    
    # Filter Horizontal (For ManyToMany)
    filter_horizontal = ['tags']
    
    # Filter Vertical (Alternative For ManyToMany)
    filter_vertical = ['categories']
    
    # Save As New Button
    save_as = True
    
    # Save On Top Of Page
    save_on_top = True
    
    # Preserve Filters After Saving
    preserve_filters = True

# ============================================================================
# CUSTOM LIST DISPLAY
# ============================================================================

from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title_with_link',
        'author_name',
        'price_display',
        'is_available_icon',
        'cover_thumbnail',
        'actions_column'
    ]
    
    # Custom Method For List Display
    def title_with_link(self, obj):
        """Display Title As Link"""
        url = reverse('book_detail', args=[obj.pk])
        return format_html('<a href="{}">{}</a>', url, obj.title)
    title_with_link.short_description = 'Title'
    title_with_link.admin_order_field = 'title'  # Enable Sorting
    
    def author_name(self, obj):
        """Display Author Name From Related Model """
        return obj.author.name if obj.author else '-'
    author_name.short_description = 'Author'
    author_name.admin_order_field = 'author__name'
    
    def price_display(self, obj):
        """Format Price With Currency"""
        return f'${obj.price:.2f}'
    price_display.short_description = 'Price'
    price_display.admin_order_field = 'price'
    
    def is_available_icon(self, obj):
        """Display Icon For Availability"""
        if obj.is_available:
            return format_html(
                '<span style="color: green;">✓</span>'
            )
        return format_html(
            '<span style="color: red;">✗</span>'
        )
    is_available_icon.short_description = 'Available'
    is_available_icon.admin_order_field = 'is_available'
    
    def cover_thumbnail(self, obj):
        """Display Cover Image Thumbnail"""
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 70px;" />',
                obj.cover_image.url
            )
        return '-'
    cover_thumbnail.short_description = 'Cover'
    
    def actions_column(self, obj):
        """Custom Action Buttons"""
        return format_html(
            '<a class="button" href="{}">View</a> '
            '<a class="button" href="{}">Edit</a>',
            reverse('book_detail', args=[obj.pk]),
            reverse('admin:myapp_book_change', args=[obj.pk])
        )
    actions_column.short_description = 'Actions'

# Coloring Rows Based On Condition
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'stock_status']
    
    def stock_status(self, obj):
        if obj.stock > 100:
            color = 'green'
            status = 'In Stock'
        elif obj.stock > 10:
            color = 'orange'
            status = 'Low Stock'
        else:
            color = 'red'
            status = 'Out Of Stock'
        
        return format_html(
            '<span style="color: {};">{}</span>',
            color,
            status
        )
    stock_status.short_description = 'Stock Status'

# ============================================================================
# FIELDSETS - ORGANIZING FIELDS
# ============================================================================

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'isbn')
        }),
        ('Publication Details', {
            'fields': ('publisher', 'published_date', 'edition'),
            'classes': ('collapse',)  # Collapsible Section
        }),
        ('Pricing & Availability', {
            'fields': ('price', 'discount', 'is_available', 'stock'),
        }),
        ('Additional Information', {
            'fields': ('description', 'cover_image'),
            'classes': ('wide',)  # Wide Layout
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']

# ============================================================================
# INLINE MODELS
# ============================================================================

from django.contrib import admin
from .models import Author, Book

# TabularInline - Compact Horizontal Layout
class BookInline(admin.TabularInline):
    model = Book
    extra = 1  # Number Of Empty Forms
    fields = ['title', 'published_date', 'price', 'is_available']
    readonly_fields = ['isbn']
    can_delete = True
    show_change_link = True  # Link To Full Edit Page
    
# StackedInline - Vertical Layout With More Space
class BookStackedInline(admin.StackedInline):
    model = Book
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('title', 'isbn', 'published_date')
        }),
        ('Details', {
            'fields': ('price', 'pages', 'description'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'book_count']
    inlines = [BookInline]
    
    def book_count(self, obj):
        return obj.book_set.count()
    book_count.short_description = 'Number of Books'

# Generic Inline (For Generic Relations)
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Comment

class CommentInline(GenericTabularInline):
    model = Comment
    extra = 1

# ============================================================================
# CUSTOM ACTIONS
# ============================================================================

from django.contrib import admin
from django.contrib import messages

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'is_available']
    actions = ['make_available', 'make_unavailable', 'apply_discount']
    
    def make_available(self, request, queryset):
        """Mark Selected Books As Available"""
        updated = queryset.update(is_available=True)
        self.message_user(
            request,
            f'{updated} Book(s) Marked As Available.',
            messages.SUCCESS
        )
    make_available.short_description = 'Mark Selected Books As Available'
    
    def make_unavailable(self, request, queryset):
        """Mark Selected Books As Unavailable"""
        updated = queryset.update(is_available=False)
        self.message_user(
            request,
            f'{updated} Book(s) Marked As Unavailable.',
            messages.WARNING
        )
    make_unavailable.short_description = 'Mark Selected Books As Unavailable'
    
    def apply_discount(self, request, queryset):
        """Apply 10% Discount To Selected Books"""
        from django.db.models import F
        updated = queryset.update(price=F('price') * 0.9)
        self.message_user(
            request,
            f'Applied 10% Discount To {updated} Book(s).',
            messages.SUCCESS
        )
    apply_discount.short_description = 'Apply 10% Discount'

# Action With Intermediate Page
from django import forms
from django.shortcuts import render

class DiscountForm(forms.Form):
    discount_percentage = forms.IntegerField(
        min_value=1,
        max_value=100,
        help_text='Enter Discount Percentage (1-100)'
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    actions = ['apply_custom_discount']
    
    def apply_custom_discount(self, request, queryset):
        form = None
        
        if 'apply' in request.POST:
            form = DiscountForm(request.POST)
            
            if form.is_valid():
                discount = form.cleaned_data['discount_percentage']
                from django.db.models import F
                
                updated = queryset.update(
                    price=F('price') * (100 - discount) / 100
                )
                
                self.message_user(
                    request,
                    f'Applied {discount}% Discount To {updated} Book(s).',
                    messages.SUCCESS
                )
                return
        
        if not form:
            form = DiscountForm(initial={
                '_selected_action': request.POST.getlist('_selected_action')
            })
        
        return render(
            request,
            'admin/apply_discount.html',
            {'form': form, 'books': queryset}
        )
    
    apply_custom_discount.short_description = 'Apply Custom Discount'

# ============================================================================
# CUSTOM FILTERS
# ============================================================================

from django.contrib import admin
from datetime import date, timedelta

# Simple list Filter
class PriceRangeFilter(admin.SimpleListFilter):
    title = 'Price Range'
    parameter_name = 'price_range'
    
    def lookups(self, request, model_admin):
        """Define Filter Options"""
        return (
            ('0-20', 'Under $20'),
            ('20-50', '$20 - $50'),
            ('50-100', '$50 - $100'),
            ('100+', 'Over $100'),
        )
    
    def queryset(self, request, queryset):
        """Filter Queryset Based On Selection"""
        if self.value() == '0-20':
            return queryset.filter(price__lt=20)
        elif self.value() == '20-50':
            return queryset.filter(price__gte=20, price__lt=50)
        elif self.value() == '50-100':
            return queryset.filter(price__gte=50, price__lt=100)
        elif self.value() == '100+':
            return queryset.filter(price__gte=100)

class PublishedDateFilter(admin.SimpleListFilter):
    title = 'Published Date'
    parameter_name = 'published'
    
    def lookups(self, request, model_admin):
        return (
            ('week', 'Past 7 Days'),
            ('month', 'Past Month'),
            ('year', 'Past Year'),
        )
    
    def queryset(self, request, queryset):
        today = date.today()
        if self.value() == 'week':
            return queryset.filter(
                published_date__gte=today - timedelta(days=7)
            )
        elif self.value() == 'month':
            return queryset.filter(
                published_date__gte=today - timedelta(days=30)
            )
        elif self.value() == 'year':
            return queryset.filter(
                published_date__gte=today - timedelta(days=365)
            )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_filter = [PriceRangeFilter, PublishedDateFilter, 'is_available']

# ============================================================================
# CUSTOM ADMIN FORMS
# ============================================================================

from django import forms
from django.contrib import admin

class BookAdminForm(forms.ModelForm):
    # Add Custom Fields
    send_notification = forms.BooleanField(
        required=False,
        help_text='Send Email Notification About This Book'
    )
    
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 10,
                'cols': 80
            }),
        }
    
    def clean_price(self):
        """Custom Validation"""
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Price Cannot Be Negative')
        if price > 10000:
            raise forms.ValidationError('Price Seems Too High')
        return price
    
    def save(self, commit=True):
        """Custom Save Logic"""
        book = super().save(commit=False)
        
        if self.cleaned_data.get('send_notification'):
            # Send Notification Email
            # send_book_notification(book)
            pass
        
        if commit:
            book.save()
        return book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm

# ============================================================================
# OVERRIDING ADMIN METHODS
# ============================================================================

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']
    
    def save_model(self, request, obj, form, change):
        """Called When Saving Object"""
        if not change:  # Creating New Object
            obj.created_by = request.user
        obj.modified_by = request.user
        super().save_model(request, obj, form, change)
    
    def delete_model(self, request, obj):
        """Called When Deleting Object"""
        # Log Deletion
        # log_deletion(request.user, obj)
        super().delete_model(request, obj)
    
    def delete_queryset(self, request, queryset):
        """Called When Deleting Multiple Objects"""
        # Log Bulk Deletion
        # log_bulk_deletion(request.user, queryset)
        super().delete_queryset(request, queryset)
    
    def get_queryset(self, request):
        """Modify Queryset"""
        qs = super().get_queryset(request)
        # Optimize With select_related
        return qs.select_related('author', 'publisher')
    
    def has_add_permission(self, request):
        """Control Who Can Add Objects"""
        return request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        """Control Who Can Change Objects"""
        if obj and obj.is_locked:
            return False
        return super().has_change_permission(request, obj)
    
    def has_delete_permission(self, request, obj=None):
        """Control Who Can Delete Objects"""
        return request.user.is_superuser
    
    def has_view_permission(self, request, obj=None):
        """Control Who Can View Objects"""
        return True
    
    def get_readonly_fields(self, request, obj=None):
        """Make Fields Readonly Conditionally"""
        if obj:  # Editing Existing Object
            return ['isbn', 'created_at']
        return []
    
    def get_list_display(self, request):
        """Customize List Display Per User"""
        list_display = ['title', 'author', 'price']
        if request.user.is_superuser:
            list_display.append('profit_margin')
        return list_display
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Filter Foreign Key Choices"""
        if db_field.name == 'author':
            kwargs['queryset'] = Author.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        """Filter Many-to-Many Choices"""
        if db_field.name == 'tags':
            kwargs['queryset'] = Tag.objects.filter(is_active=True)
        return super().formfield_for_manytomany(db_field, request, **kwargs)

# ============================================================================
# CUSTOMIZING ADMIN SITE
# ============================================================================

# In admin.py Or urls.py
from django.contrib import admin

# Change admin Site Header
admin.site.site_header = 'My Bookstore Administration'

# Change admin Site Title
admin.site.site_title = 'Bookstore Admin'

# Change index Title
admin.site.index_title = 'Welcome To Bookstore Admin Panel'

# Create custom admin Site
class MyAdminSite(admin.AdminSite):
    site_header = 'Custom Admin'
    site_title = 'My Admin Portal'
    index_title = 'Administration'
    
    def has_permission(self, request):
        """Custom Permission Logic"""
        return request.user.is_active and request.user.is_staff

# Create Instance
my_admin_site = MyAdminSite(name='myadmin')

# Register Models With Custom Site
my_admin_site.register(Book, BookAdmin)
my_admin_site.register(Author)

# In urls.py
from django.urls import path
from .admin import my_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myadmin/', my_admin_site.urls),
]

# ============================================================================
# ADMIN TEMPLATES CUSTOMIZATION
# ============================================================================

'''
Override Admin Templates By Creating Files In:
templates/admin/

Template Structure:
templates/
    admin/
        base_site.html           # Override admin Base
        index.html               # Override admin Index
        login.html               # Override login Page
        app_label/               # App-Specific Templates
            model_name/
                change_form.html # Override change Form
                change_list.html # Override list View

Example - Custom change_form.html:
{% extends "admin/change_form.html" %}

{% block after_field_sets %}
    {{ block.super }}
    <div class="custom-section">
        <h2>Additional Information</h2>
        <p>Custom Content Here</p>
    </div>
{% endblock %}
'''

# ============================================================================
# ADMIN WIDGETS AND MEDIA
# ============================================================================

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Add Custom CSS And JS
    class Media:
        css = {
            'all': ('css/admin-custom.css',)
        }
        js = ('js/admin-custom.js',)

# Custom Widget In admin
from django.forms import Textarea

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 10, 'cols': 80})},
    }

# ============================================================================
# BULK EDITING WITH ADMIN
# ============================================================================

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'is_available']
    list_editable = ['price', 'is_available']  # Edit Directly In List View
    
    # This Allows Editing Multiple Records At Once In The List View
    # Click "Save" To Apply Changes To All Edited Rows

# ============================================================================
# ADMIN SEARCH OPTIMIZATION
# ============================================================================

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = [
        'title',
        'isbn',
        'author__name',              # Search In Related Model
        'publisher__name',
        'description',
    ]
    
    # Use ^ For Starts-With Search (More Efficient)
    # search_fields = ['^title', '^isbn']
    
    # Use = For Exact Match
    # search_fields = ['=isbn']
    
    # Use @ For Full-Text Search (PostgreSQL Only)
    # search_fields = ['@description']

# ============================================================================
# ADMIN EXPORT TO CSV
# ============================================================================

import csv
from django.http import HttpResponse

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    actions = ['export_as_csv']
    
    def export_as_csv(self, request, queryset):
        """Export Selected Books As CSV"""
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        
        writer = csv.writer(response)
        writer.writerow(field_names)
        
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        
        return response
    
    export_as_csv.short_description = 'Export Selected As CSV'

# ============================================================================
# BEST PRACTICES
# ============================================================================

'''
1. Use list_display Wisely
   - Show Most Important Fields
   - Add Custom Methods For Computed Values
   - Keep It Under 10 Columns

2. Add Search And Filters
   - Makes Finding Records Easier
   - Improves Admin Usability
   - Use Appropriate Filter Types

3. Use readonly_fields
   - For Auto-Generated Fields
   - For Sensitive Data
   - For Calculated Values

4. Organize With Fieldsets
   - Group Related Fields
   - Use Collapse For Optional Sections
   - Improves Form Readability

5. Add Inline Editing
   - For Related Objects
   - Choose Appropriate Inline Type
   - Limit Number Of Inlines

6. Create Custom Actions
   - For Bulk Operations
   - Add Confirmation Steps
   - Show Appropriate Messages

7. Override Methods Carefully
   - Add Logging
   - Handle Permissions
   - Test Thoroughly

8. Optimize Queries
   - Use select_related
   - Use prefetch_related
   - Override get_queryset()

9. Secure The Admin
   - Use Strong Passwords
   - Limit Permissions
   - Enable 2FA If Possible
   - Monitor Admin Actions

10. Customize Thoughtfully
    - Don't Over-Customize
    - Keep It User-Friendly
    - Test With Actual Users
    - Document Customizations
'''