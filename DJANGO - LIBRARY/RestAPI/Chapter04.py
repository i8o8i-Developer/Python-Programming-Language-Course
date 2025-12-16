'Setting An Authentication System In Django REST Framework'

# Why We Need Authentication ?
"Authentication Is The Process Of Verifying The Identity Of A User Or System. In Web Applications, It Is Crucial To Ensure That Only Authorized Users Can Access Certain Resources Or Perform Specific Actions. Without Authentication, Anyone Could Access Sensitive Data Or Functionalities, Leading To Security Vulnerabilities And Potential Data Breaches."

# Types Of Authentication In Django REST Framework
"Django REST Framework Provides Several Built-In Authentication Classes To Handle Different Authentication Mechanisms. Some Of The Common Types Include :"

# 1. Basic Authentication: This Is A Simple Authentication Scheme That Transmits Credentials As User ID/Password Pairs Encoded Using Base64. It Is Not Secure Over Unencrypted Connections (HTTP) And Should Be Used With HTTPS.

"2. Token Authentication: This Method Uses Tokens To Authenticate Users. A Token Is Generated When A User Logs In, And This Token Is Sent With Each Subsequent Request To Verify The User's Identity."

# 3. Session Authentication: This Method Uses Django's Built-In Session Framework To Authenticate Users. It Is Suitable For Web Applications Where Users Log In Via A Web Interface.

"4. OAuth And OAuth2: These Are More Advanced Authentication Protocols That Allow Third-Party Applications To Access User Data Without Sharing Credentials. Django REST Framework Supports OAuth2 Through Third-Party Packages Like Django OAuth Toolkit."

# Setting Up Token Authentication In Django REST Framework
"To Set Up Token Authentication In Django REST Framework, Follow These Steps :

# 1. Install Django REST Framework And The Token Authentication Package:
pip install djangorestframework
pip install djangorestframework.authtoken

# 2. Add 'rest_framework' And 'rest_framework.authtoken' To Your INSTALLED_APPS In settings.py:
    
INSTALLED_APPS = [  
    ...
    'rest_framework',
    'rest_framework.authtoken',
]

#3. Run Migrations To Create The Necessary Database Tables:

python manage.py migrate

# 4. Configure Django REST Framework To Use Token Authentication In settings.py:

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [ 
        'rest_framework.authentication.TokenAuthentication',
    ],
}
# 5. Create A View To Generate Tokens For Users. You Can Use The Built-In ObtainAuthToken View :
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})
        
# 6. Add A URL Pattern For The Token Generation View In urls.py:
from django.urls import path
from .views import CustomAuthToken

urlpatterns = [
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
]

# 7. Now, Users Can Obtain A Token By Sending A POST Request With Their Username And Password To The /api-token-auth/ Endpoint. They Can Use This Token In The Authorization Header For Subsequent Requests To Access Protected Resources.
Authorization: Token <token_value>

'By Following These Steps, You Can Successfully Set Up Token Authentication In Your Django REST Framework Application, Ensuring That Only Authorized Users Can Access Protected Endpoints.'

#------------------------------------------------------------------------

# Basic Overview Of Authentication In Django REST Framework [ Browsable API ]

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# How To View The Authenticated Content In Above Case :

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),  # For Browsable API Login
    path('', include(router.urls)), 
]

# Run Server , Complete Login In Browsable API And Access The Content.
    
#-------------------------------------------------------------------------

'Implementing Permissions In Django REST Framework'
# What Are Permissions ?
"Permissions Are A Way To Control Access To Resources In Your Application Based On The User's Role Or Attributes. They Determine What Actions A User Can Perform On A Given Resource, Such As Viewing, Creating, Updating, Or Deleting Data. Implementing Permissions Is Essential For Ensuring That Users Only Have Access To The Data And Functionalities They Are Authorized To Use."

# Types Of Permissions In Django REST Framework
"Django REST Framework Provides Several Built-In Permission Classes To Handle Different Access Control Scenarios. Some Of The Common Types Include :"

# 1. AllowAny: This Permission Class Allows Unrestricted Access To The View, Meaning Any User (Authenticated Or Not) Can Access The Resource.

"2. IsAuthenticated: This Permission Class Restricts Access To Authenticated Users Only. Unauthenticated Users Will Be Denied Access."

# 3. IsAdminUser: This Permission Class Grants Access Only To Users With Admin Privileges (IsStaff=True).

"4. IsAuthenticatedOrReadOnly: This Permission Class Allows Authenticated Users To Perform Any Actions, While Unauthenticated Users Can Only Perform Read-Only Operations (GET, HEAD, OPTIONS)."

# Setting Up Permissions In Django REST Framework
"To Set Up Permissions In Django REST Framework, Follow These Steps :"

# 1. Import The Necessary Permission Classes In Your views.py:
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
# 2. Apply The Desired Permission Classes To Your Views Or ViewSets:
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Example Permission
# 3. You Can Also Set Default Permissions Globally In settings.py:
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
# 4. Customize Permissions By Creating Your Own Permission Classes If Needed:
from rest_framework.permissions import BasePermission
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.owner == request.user
# 5. Apply Custom Permission Classes To Your Views As Needed:
class CustomBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]
'By Following These Steps, You Can Effectively Implement Permissions In Your Django REST Framework Application, Ensuring That Users Have Appropriate Access To Resources Based On Their Roles And Attributes.'

Option 2 : By Creating A permission.py File
# permission.py
from rest_framework.permissions import BasePermission
class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.owner == request.user
# views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from .permission import IsOwnerOrReadOnly
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsOwnerOrReadOnly]


#-----------------------------------------------------------------------

'Implementing Throttling In Django REST Framework'
# What Is Throttling ?
"Throttling Is A Mechanism Used To Limit The Number Of Requests A User Can Make To An API Within A Specified Time Frame. It Helps Prevent Abuse, Overuse, And Denial-Of-Service (DoS) Attacks By Controlling The Rate At Which Clients Can Access The API. Throttling Ensures Fair Usage Of Resources And Maintains The Performance And Availability Of The Service."

# Types Of Throttling In Django REST Framework
"Django REST Framework Provides Several Built-In Throttling Classes To Handle Different Rate Limiting Scenarios. Some Of The Common Types Include :"

# 1. AnonRateThrottle: This Throttle Class Limits The Rate Of Requests From Unauthenticated Users (Anonymous Users).
"2. UserRateThrottle: This Throttle Class Limits The Rate Of Requests From Authenticated Users Based On Their User Account."
# 3. ScopedRateThrottle: This Throttle Class Allows You To Define Different Throttling Rates For Different Views Or ViewSets Using Scopes.

# Setting Up Throttling In Django REST Framework
"To Set Up Throttling In Django REST Framework, Follow These Steps :"

# 1. Import The Necessary Throttling Classes In Your views.py:
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
# 2. Apply The Desired Throttling Classes To Your Views Or ViewSets:
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]  # Example Throttling
# 3. You Can Also Set Default Throttling Globally In settings.py:
REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',  # 100 Requests Per Day For Anonymous Users
        'user': '1000/day'   # 1000 Requests Per Day For Authenticated Users
    }
}
# 4. Customize Throttling By Creating Your Own Throttling Classes If Needed:
from rest_framework.throttling import SimpleRateThrottle
class CustomRateThrottle(SimpleRateThrottle):
    scope = 'custom'
    
    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            return self.cache_format % {
                'scope': self.scope,
                'ident': request.user.pk
            }
        return None
# 5. Apply Custom Throttling Classes To Your Views As Needed:
class CustomBookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    throttle_classes = [CustomRateThrottle]
'By Following These Steps, You Can Effectively Implement Throttling In Your Django REST Framework Application, Ensuring Fair Usage Of Resources And Protecting Your API From Abuse.'
#-------------------------------------------------------------------------