"""
====================================
CHAPTER 12: MIDDLEWARE
====================================

Middleware Is A Framework Of Hooks Into Django's Request/Response Processing. It's A
Lightweight Plugin System For Globally Altering Django's Input Or Output.

Topics Covered:
1. Understanding Middleware
2. Built-In Middleware
3. Creating Custom Middleware
4. Middleware Order And Best Practices
5. Common Use Cases
6. Exception Handling
7. Performance Considerations
"""

#==============================================================================
# 1. UNDERSTANDING MIDDLEWARE
#==============================================================================

"""
WHAT IS MIDDLEWARE?

Middleware Is Code That Runs During The Request/Response Cycle:
- BEFORE The View Is Called (Request Phase)
- AFTER The View Is Called (Response Phase)

REQUEST/RESPONSE FLOW:
Browser → Middleware 1 → Middleware 2 → Middleware 3 → View
                                                          ↓
Browser ← Middleware 1 ← Middleware 2 ← Middleware 3 ← Response

Each Middleware Can:
- Modify The Request Before It Reaches The View
- Modify The Response Before It Reaches The Browser
- Short-Circuit The Process And Return Early
- Handle Exceptions
"""

# Middleware Structure
class SimpleMiddleware:
    """
    Basic Middleware Structure Using __call__ Method.
    """
    
    def __init__(self, get_response):
        """
        One-Time Configuration And Initialization.
        Called Once When The Server Starts.
        """
        self.get_response = get_response
    
    def __call__(self, request):
        """
        Called On Each Request, Before The View.
        """
        # Code Executed For Each Request BEFORE The View Is Called
        print(f"Before View: {request.path}")
        
        # Get Response From Next Middleware Or View
        response = self.get_response(request)
        
        # Code Executed For Each Request AFTER The View Is Called
        print(f"After View: {response.status_code}")
        
        return response


# Middleware With Additional Hooks
class AdvancedMiddleware:
    """
    Middleware With All Optional Hooks.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Request Phase
        response = self.get_response(request)
        # Response Phase
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Called Just Before Django Calls The View.
        
        Return None To Continue Processing
        Return HttpResponse To Short-Circuit
        """
        print(f"About To Call View: {view_func.__name__}")
        return None
    
    def process_exception(self, request, exception):
        """
        Called If The View Raises An Exception.
        
        Return None To Continue With Default Exception Handling
        Return HttpResponse To Handle The Exception
        """
        print(f"Exception Occurred: {exception}")
        return None
    
    def process_template_response(self, request, response):
        """
        Called Just After The View Finishes Executing.
        Only If The Response Has A render() Method (TemplateResponse).
        """
        return response


#==============================================================================
# 2. BUILT-IN MIDDLEWARE
#==============================================================================

"""
Django Comes With Several Built-In Middleware Components.
Configure In settings.py MIDDLEWARE List.
"""

# settings.py
MIDDLEWARE = [
    # Security
    'django.middleware.security.SecurityMiddleware',
    # Session Management
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Common Utilities (APPEND_SLASH, Etc.)
    'django.middleware.common.CommonMiddleware',
    # CSRF Protection
    'django.middleware.csrf.CsrfViewMiddleware',
    # Authentication
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Messages Framework
    'django.contrib.messages.middleware.MessageMiddleware',
    # Clickjacking Protection
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


"""
BUILT-IN MIDDLEWARE DETAILS:

1. SecurityMiddleware
   - Provides Security Enhancements
   - HTTPS Redirect, Strict-Transport-Security
   - X-Content-Type-Options

2. SessionMiddleware
   - Enables Session Support
   - Required For User Authentication

3. CommonMiddleware
   - URL Normalization (APPEND_SLASH)
   - Etag Generation
   - Content-Length Header

4. CsrfViewMiddleware
   - Cross-Site Request Forgery Protection
   - Validates CSRF Tokens On POST Requests

5. AuthenticationMiddleware
   - Associates Users With Requests
   - Adds request.user Attribute

6. MessageMiddleware
   - Cookie And Session-Based Message Support
   - For Temporary Messages (Success, Error, Etc.)

7. XFrameOptionsMiddleware
   - Clickjacking Protection
   - Controls Whether Site Can Be Embedded In Iframe
"""


#==============================================================================
# 3. CREATING CUSTOM MIDDLEWARE
#==============================================================================

"""
Custom Middleware For Specific Application Needs.
"""

# 1. Request Logging Middleware
import logging
import time
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """
    Log All Requests With Timing Information.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Start Timer
        start_time = time.time()
        
        # Log Request
        logger.info(f"Request: {request.method} {request.path}")
        
        # Process Request
        response = self.get_response(request)
        
        # Calculate Duration
        duration = time.time() - start_time
        
        # Log Response
        logger.info(
            f"Response: {response.status_code} "
            f"({duration:.2f}s) {request.path}"
        )
        
        return response


# 2. User Activity Tracking Middleware
from django.contrib.auth.models import User
from django.utils import timezone


class UserActivityMiddleware:
    """
    Track Last Activity Time For Authenticated Users.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # Update Last_Activity For Authenticated Users
        if request.user.is_authenticated:
            # Use update() To Avoid Triggering Signals
            User.objects.filter(pk=request.user.pk).update(
                last_activity=timezone.now()
            )
        
        return response


# 3. Custom Header Middleware
class CustomHeaderMiddleware:
    """
    Add Custom Headers To All Responses.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # Add Custom Headers
        response['X-Custom-Header'] = 'MyApp 1.0'
        response['X-Request-ID'] = str(request.META.get('REQUEST_ID', ''))
        
        return response


# 4. IP Blocking Middleware
from django.http import HttpResponseForbidden
from django.core.cache import cache


class IPBlockingMiddleware:
    """
    Block Requests From Blacklisted IP Addresses.
    """
    
    BLACKLIST_CACHE_KEY = 'blocked_ips'
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Get Client IP
        ip_address = self.get_client_ip(request)
        
        # Check If IP Is Blacklisted
        blocked_ips = cache.get(self.BLACKLIST_CACHE_KEY, set())
        if ip_address in blocked_ips:
            return HttpResponseForbidden('Your IP Address Has Been Blocked')
        
        response = self.get_response(request)
        return response
    
    def get_client_ip(self, request):
        """Extract Client IP From Request."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


# 5. Rate Limiting Middleware
from django.http import HttpResponse


class RateLimitMiddleware:
    """
    Simple Rate Limiting Based On IP Address.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = 100  # Requests Per Minute
        self.window = 60  # seconds
    
    def __call__(self, request):
        # Get Client IP
        ip = self.get_client_ip(request)
        
        # Create Cache Key
        cache_key = f'Rate_Limit_{ip}'
        
        # Get Current Request Count
        request_count = cache.get(cache_key, 0)
        
        if request_count >= self.rate_limit:
            return HttpResponse(
                'Rate Limit Exceeded. Try Again Later.',
                status=429
            )
        
        # Increment Counter
        if request_count == 0:
            # First Request In Window
            cache.set(cache_key, 1, self.window)
        else:
            cache.incr(cache_key)
        
        response = self.get_response(request)
        
        # Add Rate Limit Headers
        response['X-RateLimit-Limit'] = str(self.rate_limit)
        response['X-RateLimit-Remaining'] = str(self.rate_limit - request_count - 1)
        
        return response
    
    def get_client_ip(self, request):
        """Extract Client IP From Request."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


# 6. CORS Middleware (Simple Version)
class SimpleCORSMiddleware:
    """
    Add CORS Headers To Responses.
    For Production, Use django-cors-headers Package.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # Add CORS Headers
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        
        return response


# 7. JSON Error Response Middleware
import json
from django.http import JsonResponse


class JSONErrorMiddleware:
    """
    Return JSON Responses For Errors In API Endpoints.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception):
        """
        Convert Exceptions To JSON Responses For API Requests.
        """
        # Only For API Endpoints
        if request.path.startswith('/api/'):
            return JsonResponse({
                'error': str(exception),
                'type': exception.__class__.__name__,
            }, status=500)
        
        return None


# 8. Request/Response Timing Middleware
class TimingMiddleware:
    """
    Add Server Timing Information To Response Headers.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Record Start Time
        request.start_time = time.time()
        
        # Process Request
        response = self.get_response(request)
        
        # Calculate Duration
        duration = (time.time() - request.start_time) * 1000  # ms
        
        # Add Timing Header
        response['X-Response-Time'] = f"{duration:.2f}ms"
        
        return response


#==============================================================================
# 4. MIDDLEWARE ORDER AND BEST PRACTICES
#==============================================================================

"""
MIDDLEWARE ORDER MATTERS!

Middleware Is Processed In Order During Request Phase,
And In REVERSE Order During Response Phase.

Request:  Top → Bottom
Response: Bottom → Top

RECOMMENDED ORDER:
"""

MIDDLEWARE = [
    # 1. Security (Should Be First)
    'django.middleware.security.SecurityMiddleware',
    
    # 2. Session (Needed For Auth)
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    # 3. CORS (If Using)
    'corsheaders.middleware.CorsMiddleware',
    
    # 4. Common Utilities
    'django.middleware.common.CommonMiddleware',
    
    # 5. CSRF (After Sessions)
    'django.middleware.csrf.CsrfViewMiddleware',
    
    # 6. Authentication (After Sessions And CSRF)
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
    # 7. Messages (After Sessions And Auth)
    'django.contrib.messages.middleware.MessageMiddleware',
    
    # 8. Clickjacking Protection
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # 9. Custom Middleware (Usually At The End)
    'myapp.middleware.RequestLoggingMiddleware',
    'myapp.middleware.UserActivityMiddleware',
]


"""
BEST PRACTICES:

1. Keep Middleware Lightweight
   - Heavy Operations Slow Down ALL Requests
   - Use Caching When Appropriate
   - Consider Async Operations

2. Be Aware Of Order Dependencies
   - Auth Middleware Requires Session Middleware
   - Your Middleware Might Need Request.User

3. Handle Exceptions Gracefully
   - Don't Let Middleware Crash
   - Log Errors Appropriately

4. Use Caching To Avoid Repeated Work
   - Cache Lookups That Don't Change Often
   - Be Careful With Cache Invalidation

5. Consider Performance Impact
   - Middleware Runs On EVERY Request
   - Profile And Optimize
   - Use Conditional Execution When Possible

6. Document Your Middleware
   - Explain What It Does
   - Note Any Dependencies
   - Specify Required Settings
"""


#==============================================================================
# 5. COMMON USE CASES
#==============================================================================

"""
Real-World Middleware Examples.
"""

# Maintenance Mode Middleware
from django.shortcuts import render
from django.conf import settings


class MaintenanceModeMiddleware:
    """
    Display Maintenance Page When Site Is Under Maintenance.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Check If Maintenance Mode Is Enabled
        if getattr(settings, 'MAINTENANCE_MODE', False):
            # Allow Staff Users
            if request.user.is_authenticated and request.user.is_staff:
                return self.get_response(request)
            
            # Show Maintenance Page To Others
            return render(request, 'maintenance.html', status=503)
        
        return self.get_response(request)


# Language Detection Middleware
from django.utils import translation


class LanguageDetectionMiddleware:
    """
    Detect And Set User's Preferred Language.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Check Session
        language = request.session.get('language')
        
        # Check Cookie
        if not language:
            language = request.COOKIES.get('language')
        
        # Check Accept-Language Header
        if not language:
            language = request.META.get('HTTP_ACCEPT_LANGUAGE', '').split(',')[0]
        
        # Activate Language
        if language:
            translation.activate(language)
        
        response = self.get_response(request)
        
        # Deactivate After Request
        translation.deactivate()
        
        return response


# Database Router Middleware (for multi-tenant)
class TenantMiddleware:
    """
    Set Database Based On Subdomain (Multi-Tenant).
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Extract Tenant From Subdomain
        host = request.get_host().split(':')[0]  # Remove Port
        parts = host.split('.')
        
        if len(parts) > 2:
            tenant = parts[0]
            # Store Tenant In Thread-Local Storage
            request.tenant = tenant
        
        response = self.get_response(request)
        return response


# Request ID Middleware
import uuid


class RequestIDMiddleware:
    """
    Add Unique ID To Each Request For Tracking.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Generate Unique Request ID
        request_id = str(uuid.uuid4())
        request.id = request_id
        
        # Process Request
        response = self.get_response(request)
        
        # Add ID To Response Header
        response['X-Request-ID'] = request_id
        
        return response


# Cache Control Middleware
class CacheControlMiddleware:
    """
    Add Cache Control Headers To Responses.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        
        # Add Cache Headers For Static Content
        if request.path.startswith('/static/'):
            response['Cache-Control'] = 'public, max-age=31536000'  # 1 year
        # No Cache For Authenticated Users
        elif request.user.is_authenticated:
            response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        # Default Cache For Public Pages
        else:
            response['Cache-Control'] = 'public, max-age=3600'  # 1 hour
        
        return response


#==============================================================================
# 6. EXCEPTION HANDLING
#==============================================================================

"""
Handle Exceptions Gracefully In Middleware.
"""

class ExceptionHandlingMiddleware:
    """
    Centralized Exception Handling With Logging And Notifications.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        return self.get_response(request)
    
    def process_exception(self, request, exception):
        """
        Handle Exceptions That Occur During Request Processing.
        """
        # Log The Exception
        logger.error(
            f"Exception on {request.path}",
            exc_info=True,
            extra={
                'request': request,
                'user': request.user if hasattr(request, 'user') else None,
            }
        )
        
        # Send Notification For Critical Errors
        if isinstance(exception, CriticalError):
            self.notify_admins(request, exception)
        
        # Return Custom Error Page For Specific Exceptions
        if isinstance(exception, CustomException):
            return render(request, 'errors/custom.html', {
                'error': str(exception)
            }, status=400)
        
        # Let Django Handle Other Exceptions
        return None
    
    def notify_admins(self, request, exception):
        """Send Email Notification To Admins."""
        from django.core.mail import mail_admins
        
        mail_admins(
            subject=f'Critical Error: {exception.__class__.__name__}',
            message=f'Error on {request.path}\n\n{str(exception)}',
            fail_silently=True
        )


#==============================================================================
# 7. PERFORMANCE CONSIDERATIONS
#==============================================================================

"""
Optimizing Middleware Performance.
"""

# Conditional Middleware Execution
class ConditionalMiddleware:
    """
    Only Execute Middleware Logic For Specific Paths.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        self.enabled_paths = ['/api/', '/admin/']
    
    def __call__(self, request):
        # Check If Middleware Should Run For This Path
        should_run = any(
            request.path.startswith(path)
            for path in self.enabled_paths
        )
        
        if should_run:
            # Expensive Operation
            self.do_expensive_operation(request)
        
        return self.get_response(request)
    
    def do_expensive_operation(self, request):
        """Perform Expensive Operation."""
        pass


# Caching in Middleware
class CachingMiddleware:
    """
    Cache Expensive Operations.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Try To Get From Cache
        cache_key = f'middleware_data_{request.path}'
        data = cache.get(cache_key)
        
        if data is None:
            # Expensive Operation
            data = self.expensive_operation()
            # Cache For 5 Minutes
            cache.set(cache_key, data, 300)
        
        # Attach To Request
        request.cached_data = data
        
        return self.get_response(request)
    
    def expensive_operation(self):
        """Simulate Expensive Operation."""
        return {'result': 'data'}


# Async Middleware (Django 3.1+)
"""
For I/O-Bound Operations, Use Async Middleware.
"""

class AsyncMiddleware:
    """
    Async Middleware For Better Performance.
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    async def __call__(self, request):
        # Async Operations
        # await self.do_async_operation()
        
        response = await self.get_response(request)
        return response


"""
PERFORMANCE TIPS:

1. Minimize Database Queries
   - Use select_related And prefetch_related
   - Cache Query Results
   - Avoid N+1 Queries

2. Use Caching Effectively
   - Cache Expensive Computations
   - Set Appropriate TTL
   - Use Cache Invalidation

3. Conditional Execution
   - Only Run Middleware When Needed
   - Check Paths Early
   - Skip For Static Files

4. Profile Your Middleware
   - Measure Execution Time
   - Identify Bottlenecks
   - Optimize Hot Paths

5. Consider Async For I/O Operations
   - Network Requests
   - File Operations
   - External APIs
""" 


# Configuration In settings.py
"""
# Add Your Middleware To settings.py
MIDDLEWARE = [
    # Built-In Middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Custom Middleware
    'myapp.middleware.RequestLoggingMiddleware',
    'myapp.middleware.UserActivityMiddleware',
    'myapp.middleware.RateLimitMiddleware',
]

# Middleware-Specific Settings
MAINTENANCE_MODE = False
RATE_LIMIT_PER_MINUTE = 100
"""


"""
SUMMARY:

Middleware Provides:
✅ Request/Response Processing Hooks
✅ Global Application Behavior
✅ Code Reuse Across Views
✅ Security And Monitoring
✅ Performance Optimization Opportunities
Remember:
- Middleware Runs On EVERY Request
- Order Matters
- Keep It Lightweight
- Use Caching When Appropriate
- Handle Exceptions Gracefully
- Document Dependencies And Settings
"""

# End of Chapter 12: Middleware