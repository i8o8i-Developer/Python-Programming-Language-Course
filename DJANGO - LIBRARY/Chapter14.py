"""
====================================
CHAPTER 14: ADVANCED VALIDATION
====================================

Comprehensive Guide To Data Validation In Django At All Levels - Models, Forms,
Serializers, And Custom Validators. Learn To Ensure Data Integrity And Security.

Topics Covered:
1. Model-Level Validation
2. Form Validation Deep Dive
3. Custom Validators
4. Serializer Validation (DRF)
5. Database Constraints
6. Cross-Field Validation
7. Async Validation
8. Best Practices And Patterns
"""

#==============================================================================
# 1. MODEL-LEVEL VALIDATION
#==============================================================================

"""
Model Validation Ensures Data Integrity At The Model Layer Before Saving To Database.
"""

from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
    EmailValidator,
    URLValidator,
    RegexValidator,
    FileExtensionValidator
)
from django.utils.translation import gettext_lazy as _
import re


# Basic Model With Field Validators
class Book(models.Model):
    """Book Model With Comprehensive Validation."""
    
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(3, 'Title Must Be At Least 3 Characters')]
    )
    
    isbn = models.CharField(
        max_length=13,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^\d{13}$',
                message='ISBN Must Be Exactly 13 Digits',
                code='invalid_isbn'
            )
        ]
    )
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01, 'Price Must Be At Least $0.01'),
            MaxValueValidator(9999.99, 'Price Cannot Exceed $9999.99')
        ]
    )
    
    publication_year = models.IntegerField(
        validators=[
            MinValueValidator(1450, 'Books Before 1450 Are Not Supported'),
            MaxValueValidator(2100, 'Future Publication Year Is Too Far')
        ]
    )
    
    pages = models.PositiveIntegerField(
        validators=[MinValueValidator(1, 'Book Must Have At Least 1 Page')]
    )
    
    email = models.EmailField(
        validators=[EmailValidator(message='Enter A Valid Email Address')]
    )
    
    website = models.URLField(
        blank=True,
        validators=[URLValidator(message='Enter A Valid URL')]
    )
    
    cover_image = models.ImageField(
        upload_to='covers/',
        validators=[
            FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png'],
                message='Only JPG, JPEG, and PNG Files Are Allowed'
            )
        ]
    )
    
    rating = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ]
    )
    
    def clean(self):
        """
        Model-Level Validation For Complex Business Logic.
        Called When Calling full_clean() Or When Saving Through ModelForm.
        """
        # Cross-Field Validation
        if self.publication_year:
            from datetime import datetime
            current_year = datetime.now().year
            
            if self.publication_year > current_year:
                raise ValidationError({
                    'publication_year': 'Publication Year Cannot Be In The Future'
                })
        
        # Title And ISBN Relationship
        if self.title and 'test' in self.title.lower() and not self.isbn.startswith('000'):
            raise ValidationError({
                'isbn': 'Test Books Must Have ISBN Starting With 000'
            })
        
        # Price And Pages Relationship
        if self.price and self.pages:
            price_per_page = self.price / self.pages
            if price_per_page > 10:
                raise ValidationError(
                    'Price Per Page ($%.2f) Exceeds Maximum Allowed ($10.00)' % price_per_page
                )
    
    def clean_fields(self, exclude=None):
        """
        Validate Individual Fields.
        Called Before clean().
        """
        super().clean_fields(exclude=exclude)
        
        # Additional Field-Specific Validation
        if 'title' not in exclude and self.title:
            # Remove Extra Whitespace
            self.title = ' '.join(self.title.split())
            
            # Check For Profanity (Example)
            profanity_list = ['badword1', 'badword2']
            if any(word in self.title.lower() for word in profanity_list):
                raise ValidationError({
                    'title': 'Title Contains Inappropriate Language'
                })
    
    def save(self, *args, **kwargs):
        """
        Override Save To Ensure Validation.
        Note: save() Does NOT Call full_clean() By Default!
        """
        # Explicitly Call full_clean() To Validate
        self.full_clean()
        super().save(*args, **kwargs)


# Model With Custom Validation Methods
class Order(models.Model):
    """Order Model With Custom Validation."""
    
    customer_email = models.EmailField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_code = models.CharField(max_length=20, blank=True)
    items_count = models.PositiveIntegerField()
    
    def clean(self):
        """Complex Business Rule Validation."""
        super().clean()
        
        errors = {}
        
        # Validate Discount Code
        if self.discount_code:
            if not self.is_valid_discount_code(self.discount_code):
                errors['discount_code'] = 'Invalid discount code'
        
        # Validate Minimum Order Amount
        if self.total_amount < 10:
            errors['total_amount'] = 'Minimum Order Amount Is $10.00'
        
        # Validate Items Count Matches Total
        if self.items_count == 0 and self.total_amount > 0:
            errors['items_count'] = 'Order With Amount Must Have Items'
        
        if errors:
            raise ValidationError(errors)
    
    @staticmethod
    def is_valid_discount_code(code):
        """Check If Discount Code Is Valid."""
        valid_codes = ['SAVE10', 'SAVE20', 'FREESHIP']
        return code.upper() in valid_codes


#==============================================================================
# 2. FORM VALIDATION DEEP DIVE
#==============================================================================

"""
Forms Provide Multiple Levels Of Validation With Different Hooks.
For Basic Form Validation Examples, See Chapter 09 (Django Forms).
This Section Focuses On Advanced Validation Patterns.

Note: Basic Form Validation Is Covered In Chapter 09. Here We Focus On
Advanced Patterns Like Complex Business Rules And Security Validation.
"""

from django import forms


# Advanced Validation Example - Complex Business Rules
class AdvancedOrderForm(forms.Form):
    """
    Advanced Validation With Complex Business Logic.
    """
    product_quantity = forms.IntegerField(min_value=1)
    unit_price = forms.DecimalField(max_digits=10, decimal_places=2)
    discount_code = forms.CharField(max_length=20, required=False)
    customer_tier = forms.ChoiceField(choices=[('bronze', 'Bronze'), ('silver', 'Silver'), ('gold', 'Gold')])
    
    def clean(self):
        """Complex Cross-Field Business Rule Validation."""
        cleaned_data = super().clean()
        
        quantity = cleaned_data.get('quantity')
        price = cleaned_data.get('unit_price')
        discount = cleaned_data.get('discount_code')
        tier = cleaned_data.get('customer_tier')
        
        # Business Rule: Gold Tier Gets Automatic Discount
        if tier == 'gold' and discount and not discount.startswith('GOLD'):
            raise forms.ValidationError(
                'Gold Tier Members Should Use GOLD Discount Codes'
            )
        
        # Business Rule: Bulk Orders Have Minimum Value
        if quantity and quantity > 100 and price:
            total = quantity * price
            if total < 1000:
                raise forms.ValidationError(
                    'Bulk Orders (>100 Items) Must Have Minimum Value Of $1000'
                )
        
        return cleaned_data


#==============================================================================
# 3. CUSTOM VALIDATORS
#==============================================================================

"""
Create Reusable Validators For Specific Validation Logic.
"""

from django.core.validators import BaseValidator


# Function-Based Validators
def validate_no_special_chars(value):
    """
    Validate That Value Contains Only Alphanumeric Characters.
    """
    if not value.isalnum():
        raise ValidationError(
            _('%(value)s Contains Special Characters'),
            params={'value': value},
            code='special_chars'
        )


def validate_phone_number(value):
    """
    Validate Phone Number Format.
    """
    phone_regex = re.compile(r'^\+?1?\d{9,15}$')
    if not phone_regex.match(value):
        raise ValidationError(
            'Phone Number Must Be 9-15 Digits. Can Optionally Start With + Or Country Code.',
            code='invalid_phone'
        )


def validate_future_date(value):
    """
    Validate That Date Is In The Future.
    """
    from datetime import date
    if value <= date.today():
        raise ValidationError(
            'Date Must Be In The Future',
            code='past_date'
        )


def validate_file_size(max_size_mb):
    """
    Validator Factory For File Size.
    """
    def validator(file):
        if file.size > max_size_mb * 1024 * 1024:
            raise ValidationError(
                f'File Size Cannot Exceed {max_size_mb}MB',
                code='file_too_large'
            )
    return validator


# Class-Based Validators
class AlphabeticValidator:
    """
    Validate That Value Contains Only Letters.
    """
    message = 'Enter Only Letters (A-Z, a-z)'
    code = 'non_alphabetic'
    
    def __call__(self, value):
        if not value.isalpha():
            raise ValidationError(self.message, code=self.code)


class ProhibitedWordsValidator:
    """
    Validate That Value Doesn't Contain Prohibited Words.
    """
    def __init__(self, prohibited_words=None):
        self.prohibited_words = prohibited_words or []
    
    def __call__(self, value):
        for word in self.prohibited_words:
            if word.lower() in value.lower():
                raise ValidationError(
                    f'Text Contains Prohibited Word: "{word}"',
                    code='prohibited_word'
                )
    
    def __eq__(self, other):
        return (
            isinstance(other, ProhibitedWordsValidator) and
            self.prohibited_words == other.prohibited_words
        )


class StrongPasswordValidator:
    """
    Validate Password Strength.
    """
    def __init__(self, min_length=8):
        self.min_length = min_length
    
    def validate(self, password, user=None):
        """Validate The Password."""
        errors = []
        
        if len(password) < self.min_length:
            errors.append(
                f'Password Must Be At Least {self.min_length} Characters Long'
            )
        
        if not re.search(r'[A-Z]', password):
            errors.append('Password Must Contain At Least One Uppercase Letter')
        
        if not re.search(r'[a-z]', password):
            errors.append('Password Must Contain At Least One Lowercase Letter')
        
        if not re.search(r'\d', password):
            errors.append('Password Must Contain At Least One Digit')
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append('Password Must Contain At Least One Special Character')
        
        if errors:
            raise ValidationError(errors, code='password_too_weak')
    
    def get_help_text(self):
        """Help Text For The Validator."""
        return (
            f'Your Password Must Be At Least {self.min_length} Characters Long '
            'And Contain Uppercase, Lowercase, Digit, And Special Character.'
        )


# Using Custom Validators In Models
class UserProfile(models.Model):
    """Model Using Custom Validators."""
    
    username = models.CharField(
        max_length=50,
        validators=[
            validate_no_special_chars,
            AlphabeticValidator(),
        ]
    )
    
    phone = models.CharField(
        max_length=15,
        validators=[validate_phone_number]
    )
    
    bio = models.TextField(
        validators=[
            ProhibitedWordsValidator(['spam', 'offensive', 'inappropriate'])
        ]
    )
    
    avatar = models.ImageField(
        upload_to='avatars/',
        validators=[validate_file_size(2)]  # 2MB max
    )


#==============================================================================
# 4. SERIALIZER VALIDATION (Django REST Framework)
#==============================================================================

"""
Validation In Django REST Framework Serializers.
"""

from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator


class BookSerializer(serializers.ModelSerializer):
    """
    DRF Serializer With Comprehensive Validation.
    """
    
    # Field-Level Validation
    title = serializers.CharField(
        max_length=200,
        min_length=3,
        validators=[
            UniqueValidator(
                queryset=Book.objects.all(),
                message='A Book With This Title Already Exists'
            )
        ]
    )
    
    isbn = serializers.CharField(
        max_length=13,
        min_length=13,
        validators=[
            RegexValidator(
                regex=r'^\d{13}$',
                message='ISBN Must Be Exactly 13 Digits'
            )
        ]
    )
    
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=0.01,
        max_value=9999.99
    )
    
    publication_year = serializers.IntegerField(
        min_value=1450,
        max_value=2100
    )
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'price', 'publication_year', 'pages']
        
        # Unique Together Validation
        validators = [
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=['title', 'publication_year'],
                message='A Book With This Title And Year Already Exists'
            )
        ]
    
    def validate_title(self, value):
        """
        Field-Level Validation Method.
        """
        # Clean Whitespace
        value = ' '.join(value.split())
        
        # Check For Profanity
        profanity_list = ['badword1', 'badword2']
        if any(word in value.lower() for word in profanity_list):
            raise serializers.ValidationError(
                'Title Contains Inappropriate Language'
            )
        
        return value
    
    def validate_isbn(self, value):
        """Validate ISBN Format."""
        # Remove Hyphens
        value = value.replace('-', '')
        
        # Validate Checksum
        if not self.validate_isbn_checksum(value):
            raise serializers.ValidationError('Invalid ISBN Checksum')
        
        return value
    
    @staticmethod
    def validate_isbn_checksum(isbn):
        """Validate ISBN-13 Checksum."""
        digits = [int(d) for d in isbn]
        checksum = sum(d if i % 2 == 0 else d * 3 for i, d in enumerate(digits[:-1]))
        return (10 - (checksum % 10)) % 10 == digits[-1]
    
    def validate(self, attrs):
        """
        Object-Level Validation (Cross-Field).
        """
        price = attrs.get('price')
        pages = attrs.get('pages')
        publication_year = attrs.get('publication_year')
        
        # Price Per Page Validation
        if price and pages:
            price_per_page = price / pages
            if price_per_page > 10:
                raise serializers.ValidationError({
                    'price': f'Price Per Page (${price_per_page:.2f}) Exceeds Maximum ($10.00)'
                })
        
        # Publication Year Validation
        if publication_year:
            from datetime import datetime
            current_year = datetime.now().year
            if publication_year > current_year:
                raise serializers.ValidationError({
                    'publication_year': 'Publication Year Cannot Be In The Future'
                })
        
        return attrs
    
    def create(self, validated_data):
        """
        Custom Create Logic With Additional Validation.
        """
        # Additional Business Logic Validation
        if validated_data.get('price') < 5 and validated_data.get('pages') > 1000:
            raise serializers.ValidationError(
                'Books With More Than 1000 Pages Cannot Be Priced Under $5'
            )
        
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        """
        Custom Update Logic With Validation.
        """
        # Prevent Price Decrease By More Than 50%
        new_price = validated_data.get('price', instance.price)
        if new_price < instance.price * 0.5:
            raise serializers.ValidationError({
                'price': 'Price Cannot Be Decreased By More Than 50%'
            })
        
        return super().update(instance, validated_data)


# Custom serializer Field With Validation
class ISBNField(serializers.CharField):
    """
    Custom Serializer Field For ISBN Validation.
    """
    def __init__(self, **kwargs):
        kwargs['max_length'] = 13
        kwargs['min_length'] = 13
        super().__init__(**kwargs)
    
    def to_internal_value(self, data):
        # Remove Hyphens And Spaces
        data = re.sub(r'[-\s]', '', data)
        
        # Validate Format
        if not re.match(r'^\d{13}$', data):
            raise serializers.ValidationError('ISBN Must Be 13 Digits')
        
        # Validate Checksum
        if not self.validate_checksum(data):
            raise serializers.ValidationError('Invalid ISBN Checksum')
        
        return data
    
    @staticmethod
    def validate_checksum(isbn):
        digits = [int(d) for d in isbn]
        checksum = sum(d if i % 2 == 0 else d * 3 for i, d in enumerate(digits[:-1]))
        return (10 - (checksum % 10)) % 10 == digits[-1]


#==============================================================================
# 5. DATABASE CONSTRAINTS
#==============================================================================

"""
Use Database-Level Constraints For Data Integrity.
"""

from django.db.models import Q, CheckConstraint, UniqueConstraint


class Product(models.Model):
    """Model With Database Constraints."""
    
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    stock = models.IntegerField()
    category = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        constraints = [
            # Ensure Sale Price Is Less Than Regular Price
            CheckConstraint(
                check=Q(sale_price__lt=models.F('price')) | Q(sale_price__isnull=True),
                name='sale_price_less_than_price'
            ),
            
            # Ensure Price Is Positive
            CheckConstraint(
                check=Q(price__gt=0),
                name='price_positive'
            ),
            
            # Ensure Stock Is Non-Negative
            CheckConstraint(
                check=Q(stock__gte=0),
                name='stock_non_negative'
            ),
            
            # Unique SKU Per Category
            UniqueConstraint(
                fields=['sku', 'category'],
                name='unique_sku_per_category'
            ),
            
            # Conditional Unique Constraint
            UniqueConstraint(
                fields=['name'],
                condition=Q(is_active=True),
                name='unique_active_product_name'
            ),
        ]


#==============================================================================
# 6. CROSS-FIELD VALIDATION
#==============================================================================

"""
Validate Relationships Between Multiple Fields.
"""

class EventRegistration(models.Model):
    """Event Registration With Complex Validation."""
    
    event_date = models.DateField()
    registration_date = models.DateField(auto_now_add=True)
    early_bird_deadline = models.DateField()
    ticket_type = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    attendee_age = models.IntegerField()
    
    def clean(self):
        """Cross-Field Validation."""
        super().clean()
        
        errors = {}
        
        # Event Date Must Be After Registration Date
        if self.event_date and self.registration_date:
            if self.event_date <= self.registration_date:
                errors['event_date'] = 'Event Date Must Be After Registration Date'
        
        # Early Bird Deadline Must Be Before Event Date
        if self.early_bird_deadline and self.event_date:
            if self.early_bird_deadline >= self.event_date:
                errors['early_bird_deadline'] = 'Early Bird Deadline Must Be Before Event Date'
        
        # Validate Ticket Type And Price Relationship
        if self.ticket_type and self.price:
            expected_prices = {
                'regular': (50, 100),
                'vip': (100, 200),
                'student': (25, 50),
            }
            
            if self.ticket_type in expected_prices:
                min_price, max_price = expected_prices[self.ticket_type]
                if not (min_price <= self.price <= max_price):
                    errors['price'] = f'{self.ticket_type} Tickets Must Be Between ${min_price} And ${max_price}'
        
        # Age Validation For Ticket Type
        if self.attendee_age and self.ticket_type:
            if self.ticket_type == 'student' and self.attendee_age > 25:
                errors['ticket_type'] = 'Student Tickets Are Only Available For Ages 25 And Under'
            
            if self.ticket_type == 'senior' and self.attendee_age < 65:
                errors['attendee_age'] = 'Senior Tickets Require Age 65 Or Older'
        
        if errors:
            raise ValidationError(errors)


#==============================================================================
# 7. ASYNC VALIDATION
#==============================================================================

"""
Asynchronous Validation For External API Calls Or Heavy Operations.
"""

# Using Celery For Async Validation
from celery import shared_task
from django.core.cache import cache


@shared_task
def validate_email_deliverability(email):
    """
    Validate Email Deliverability Asynchronously.
    """
    import requests
    
    # Call Email Verification API
    response = requests.get(
        f'https://api.emailvalidation.com/verify?email={email}'
    )
    
    result = response.json()
    
    # Cache Result For 24 Hours
    cache.set(f'email_valid_{email}', result['is_valid'], 86400)
    
    return result['is_valid']


class AsyncValidatedForm(forms.Form):
    """Form With Async Validation."""
    
    email = forms.EmailField()
    
    def clean_email(self):
        """Validate Email With Caching."""
        email = self.cleaned_data['email']
        
        # Check Cache First
        cached_result = cache.get(f'email_valid_{email}')
        
        if cached_result is None:
            # Trigger Async Validation
            validate_email_deliverability.delay(email)
            
            # For Now, Allow The Email (Will Be Validated Async)
            # You Could Also Make User Wait With Synchronous Validation
            pass
        elif not cached_result:
            raise forms.ValidationError(
                'This Email Address Appears To Be Invalid Or Non-Deliverable'
            )
        
        return email


#==============================================================================
# 8. BEST PRACTICES AND PATTERNS
#==============================================================================

"""
VALIDATION BEST PRACTICES:

1. Validate At Multiple Levels
   - Client-Side (UX)
   - Form/Serializer (Business Logic)
   - Model (Data Integrity)
   - Database (Constraints)

2. Use Appropriate Validation Level
   - Simple Format Checks: Field Validators
   - Business Rules: clean() Method
   - Cross-Field: clean() Or validate()
   - Database Integrity: Constraints

3. Provide Clear Error Messages
   - Be Specific About What's Wrong
   - Suggest How To Fix It
   - Use Proper Field Association

4. Handle Edge Cases
   - Null/blank Values
   - Very Large/Small Numbers
   - Special Characters
   - Unicode

5. Performance Considerations
   - Cache Expensive Validations
   - Use Database Constraints When Possible
   - Avoid N+1 Queries In Validation
   - Consider Async For External APIs

6. Security
   - Sanitize Input
   - Validate File Uploads Carefully
   - Check File Extensions And Content
   - Limit File Sizes

7. Testing
   - Test Valid Data
   - Test Invalid Data
   - Test Edge Cases
   - Test Cross-Field Validation
"""

# Complete Validation Example
class ComprehensiveBookForm(forms.ModelForm):
    """
    Example Combining All Best Practices.
    """
    
    class Meta:
        model = Book
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Custom Attributes To Form Fields
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter Book Title'
        })
    
    def clean_title(self):
        """Field-Level Validation."""
        title = self.cleaned_data.get('title')
        if title:
            title = ' '.join(title.split())
            if len(title) < 3:
                raise forms.ValidationError('Title Too Short')
        return title
    
    def clean(self):
        """Cross-Field Validation."""
        cleaned_data = super().clean()
        # Validation Logic
        return cleaned_data
    
    def save(self, commit=True):
        """Custom Save With Additional Processing."""
        instance = super().save(commit=False)
        # Additional Processing
        if commit:
            instance.save()
        return instance


"""
SUMMARY:

Validation Ensures:
✅ Data Integrity
✅ Business Rule Enforcement
✅ Security
✅ User Experience
✅ Database Consistency

Remember:
- Validate At Appropriate Levels
- Provide Clear Error Messages
- Handle Edge Cases
- Consider Performance
- Test Thoroughly
- Keep It Maintainable
"""

# End of Chapter 14: Advanced Validation