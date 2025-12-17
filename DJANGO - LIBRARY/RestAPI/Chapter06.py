"""
====================================
CHAPTER 06: TESTING REST APIs
====================================

Testing Is Essential For Ensuring Your REST API Works Correctly And Remains Stable 
As You Make Changes. This Chapter Covers Comprehensive Testing Strategies For Django 
REST Framework Applications.

Topics Covered:
1. API Test Cases
2. Testing Authentication
3. Testing Permissions
4. Testing ViewSets
5. Testing Serializers
6. Test Fixtures And Factories
7. API Client Testing
8. Coverage And Best Practices
"""

#==============================================================================
# 1. BASIC API TEST CASES
#==============================================================================

"""
Django REST Framework Provides The `APITestCase` Class Which Extends Django's 
`TestCase` With Additional Methods For Testing APIs.
"""

# tests.py
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author
from django.urls import reverse


class BookAPITestCase(APITestCase):
    """
    Test Cases For Book API Endpoints.
    """
    
    def setUp(self):
        """
        Set Up Test Data That Will Be Used Across Multiple Tests.
        This Method Runs Before Each Test Method.
        """
        # Create Test User
        self.user = User.objects.create_user(
            username='TestUser',
            email='Test@example.com',
            password='TestPass123'
        )
        
        # Create Test Author
        self.author = Author.objects.create(
            name='Test Author',
            country='USA',
            birth_date='1980-01-01'
        )
        
        # Create Test Books
        self.book1 = Book.objects.create(
            title='Test Book 1',
            author=self.author,
            publication_year=2020,
            genre='Fiction',
            price=29.99,
            owner=self.user
        )
        
        self.book2 = Book.objects.create(
            title='Test Book 2',
            author=self.author,
            publication_year=2021,
            genre='Science Fiction',
            price=34.99,
            owner=self.user
        )
        
        # Set Up API Client
        self.client = APIClient()
    
    def tearDown(self):
        """
        Clean Up After Tests. Runs After Each Test Method.
        """
        User.objects.all().delete()
        Author.objects.all().delete()
        Book.objects.all().delete()
    
    
    #--------------------------------------------------------------------------
    # Test GET requests
    #--------------------------------------------------------------------------
    
    def test_get_all_books(self):
        """
        Test Retrieving All Books From The API.
        """
        url = reverse('book-list')  # Assumes You're Using ViewSet With Router
        response = self.client.get(url)
        
        # Assert Status Code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert Response Data
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')
    
    def test_get_single_book(self):
        """
        Test Retrieving A Single Book By ID.
        """
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book 1')
        self.assertEqual(response.data['author'], self.author.pk)
    
    def test_get_nonexistent_book(self):
        """
        Test Retrieving A Book That Doesn't Exist.
        """
        url = reverse('book-detail', kwargs={'pk': 9999})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    
    #--------------------------------------------------------------------------
    # Test POST requests
    #--------------------------------------------------------------------------
    
    def test_create_book(self):
        """
        Test Creating A New Book Via API.
        """
        url = reverse('book-list')
        data = {
            'title': 'New Test Book',
            'author': self.author.pk,
            'publication_year': 2023,
            'genre': 'Mystery',
            'price': 39.99
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], 'New Test Book')
    
    def test_create_book_invalid_data(self):
        """
        Test Creating A Book With Invalid Data.
        """
        url = reverse('book-list')
        data = {
            'title': '',  # Empty Title Should Fail Validation
            'author': self.author.pk,
            'publication_year': 2023,
            'genre': 'Mystery',
            'price': -10.00  # Negative Price Should Fail Validation
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)
        self.assertIn('price', response.data)
    
    def test_create_book_missing_fields(self):
        """
        Test Creating A Book With Missing Required Fields.
        """
        url = reverse('book-list')
        data = {
            'title': 'Incomplete Book'
            # Missing Required Fields
        }
        
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    
    #--------------------------------------------------------------------------
    # Test PUT/PATCH requests
    #--------------------------------------------------------------------------
    
    def test_update_book(self):
        """
        Test Updating A Book Via PUT Request.
        """
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        data = {
            'title': 'Updated Test Book',
            'author': self.author.pk,
            'publication_year': 2022,
            'genre': 'Updated Genre',
            'price': 44.99
        }
        
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Test Book')
        self.assertEqual(self.book1.price, 44.99)
    
    def test_partial_update_book(self):
        """
        Test Partially Updating A Book Via PATCH Request.
        """
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        data = {
            'price': 49.99
        }
        
        response = self.client.patch(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.price, 49.99)
        self.assertEqual(self.book1.title, 'Test Book 1')  # Should Remain Unchanged
    
    
    #--------------------------------------------------------------------------
    # Test DELETE requests
    #--------------------------------------------------------------------------
    
    def test_delete_book(self):
        """
        Test Deleting A Book Via API.
        """
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())


#==============================================================================
# 2. TESTING AUTHENTICATION
#==============================================================================

"""
Testing Authentication Ensures That Your API Properly Authenticates Users And 
Protects Resources.
"""

class AuthenticationTestCase(APITestCase):
    """
    Test Cases For API Authentication.
    """
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='TestUser',
            password='TestPass123'
        )
        
        self.author = Author.objects.create(
            name='Test Author',
            country='USA'
        )
        
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            publication_year=2020,
            genre='Fiction',
            price=29.99,
            owner=self.user
        )
        
        self.client = APIClient()
    
    def test_unauthenticated_access(self):
        """
        Test That Unauthenticated Users Cannot Access Protected Endpoints.
        """
        url = reverse('book-list')
        response = self.client.get(url)
        
        # Assuming Your View Requires Authentication
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_authenticated_access(self):
        """
        Test That Authenticated Users Can Access Protected Endpoints.
        """
        # Authenticate The Client
        self.client.force_authenticate(user=self.user)
        
        url = reverse('book-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_token_authentication(self):
        """
        Test Authentication Using Tokens (If Using TokenAuthentication).
        """
        from rest_framework.authtoken.models import Token
        
        # Create token For User
        token = Token.objects.create(user=self.user)
        
        # Add token To Request Header
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
        
        url = reverse('book-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_invalid_token(self):
        """
        Test That Invalid Tokens Are Rejected.
        """
        # Use invalid token
        self.client.credentials(HTTP_AUTHORIZATION='Token Invalid_Token_Here')
        
        url = reverse('book-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_jwt_authentication(self):
        """
        Test JWT Token Authentication (If Using JWT).
        """
        from rest_framework_simplejwt.tokens import RefreshToken
        
        # Get JWT token
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        
        # Add token To Request Header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        
        url = reverse('book-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)


#==============================================================================
# 3. TESTING PERMISSIONS
#==============================================================================

"""
Test That Your Permission Classes Work Correctly And Enforce Access Controls.
"""

class PermissionTestCase(APITestCase):
    """
    Test Cases For API Permissions.
    """
    
    def setUp(self):
        # Create users
        self.owner = User.objects.create_user(
            username='Owner',
            password='Pass123'
        )
        
        self.other_user = User.objects.create_user(
            username='Other',
            password='Pass123'
        )
        
        self.admin_user = User.objects.create_superuser(
            username='Admin',
            password='Pass123',
            email='admin@example.com'
        )
        
        # Create test data
        self.author = Author.objects.create(
            name='Test Author',
            country='USA'
        )
        
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            publication_year=2020,
            genre='Fiction',
            price=29.99,
            owner=self.owner
        )
        
        self.client = APIClient()
    
    def test_owner_can_edit(self):
        """
        Test That The Owner Of A Resource Can Edit It.
        """
        self.client.force_authenticate(user=self.owner)
        
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        data = {'price': 39.99}
        response = self.client.patch(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_non_owner_cannot_edit(self):
        """
        Test That Non-Owners Cannot Edit Resources They Don't Own.
        """
        self.client.force_authenticate(user=self.other_user)
        
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        data = {'price': 39.99}
        response = self.client.patch(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_owner_can_delete(self):
        """
        Test That The Owner Can Delete Their Resource.
        """
        self.client.force_authenticate(user=self.owner)
        
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_non_owner_cannot_delete(self):
        """
        Test That Non-Owners Cannot Delete Resources They Don't Own.
        """
        self.client.force_authenticate(user=self.other_user)
        
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_admin_can_access_all(self):
        """
        Test That Admin Users Can Access And Modify All Resources.
        """
        self.client.force_authenticate(user=self.admin_user)
        
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        data = {'price': 39.99}
        response = self.client.patch(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_read_only_for_non_authenticated(self):
        """
        Test That Unauthenticated Users Have Read-Only Access.
        """
        # Don't authenticate
        url = reverse('book-list')
        response = self.client.get(url)
        
        # Should Be Able To Read
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # But Not Create
        data = {
            'title': 'New Book',
            'author': self.author.pk,
            'publication_year': 2023,
            'genre': 'Fiction',
            'price': 29.99
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


#==============================================================================
# 4. TESTING VIEWSETS
#==============================================================================

"""
Test ViewSet Actions And Custom Methods.
"""

class ViewSetTestCase(APITestCase):
    """
    Test Cases For ViewSet Functionality.
    """
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='TestUser',
            password='TestPass123'
        )
        
        self.author = Author.objects.create(
            name='Test Author',
            country='USA'
        )
        
        # Create Multiple Books For Testing List Actions
        for i in range(15):
            Book.objects.create(
                title=f'Test Book {i}',
                author=self.author,
                publication_year=2020 + (i % 5),
                genre='Fiction' if i % 2 == 0 else 'Science Fiction',
                price=20 + i,
                owner=self.user
            )
        
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    
    def test_list_action(self):
        """
        Test The List Action Of A ViewSet.
        """
        url = reverse('book-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 15)
    
    def test_pagination(self):
        """
        Test That Pagination Works Correctly.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'page': 1, 'page_size': 10})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assuming You Have Pagination Configured
        # self.assertEqual(len(response.data['results']), 10)
    
    def test_filtering(self):
        """
        Test Filtering Query Parameters.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'genre': 'Fiction'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # All Results Should Be Fiction
        for book in response.data:
            self.assertEqual(book['genre'], 'Fiction')
    
    def test_ordering(self):
        """
        Test Ordering Query Parameters.
        """
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': '-price'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Results Should Be Ordered By Price Descending
        prices = [book['price'] for book in response.data]
        self.assertEqual(prices, sorted(prices, reverse=True))
    
    def test_custom_action(self):
        """
        Test A Custom Action On A ViewSet.
        
        Example: @action(detail=False, methods=['get'])
                 def recent(self, request):
                     ...
        """
        url = reverse('book-recent')  # Assuming You Have A 'recent' Action
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Add Assertions Based On Your Custom Action

#==============================================================================
# 5. TESTING SERIALIZERS
#==============================================================================

"""
Test Serializer Validation, Transformation, And Custom Methods.
"""

from django.test import TestCase
from .serializers import BookSerializer, AuthorSerializer


class SerializerTestCase(TestCase):
    """
    Test Cases For Serializers.
    """
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='TestUser',
            password='TestPass123'
        )
        
        self.author = Author.objects.create(
            name='Test Author',
            country='USA'
        )
        
        self.book = Book.objects.create(
            title='Test Book',
            author=self.author,
            publication_year=2020,
            genre='Fiction',
            price=29.99,
            owner=self.user
        )
    
    def test_serializer_contains_expected_fields(self):
        """
        Test That The Serializer Contains All Expected Fields.
        """
        serializer = BookSerializer(instance=self.book)
        data = serializer.data
        
        self.assertEqual(set(data.keys()), {
            'id', 'title', 'author', 'publication_year', 
            'genre', 'price', 'owner'
        })
    
    def test_serializer_field_content(self):
        """
        Test The Content Of Serializer Fields.
        """
        serializer = BookSerializer(instance=self.book)
        data = serializer.data
        
        self.assertEqual(data['title'], 'Test Book')
        self.assertEqual(data['genre'], 'Fiction')
        self.assertEqual(float(data['price']), 29.99)
    
    def test_serializer_validation(self):
        """
        Test That Serializer Validation Works Correctly.
        """
        # Invalid Data
        invalid_data = {
            'title': '',  # Empty Itle Should Fail
            'author': self.author.pk,
            'publication_year': 2020,
            'genre': 'Fiction',
            'price': -10.00  # Negative Price Should Fail
        }
        
        serializer = BookSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('title', serializer.errors)
        self.assertIn('price', serializer.errors)
    
    def test_serializer_create(self):
        """
        Test Creating An Object Through The Serializer.
        """
        valid_data = {
            'title': 'New Book',
            'author': self.author.pk,
            'publication_year': 2023,
            'genre': 'Mystery',
            'price': 34.99,
            'owner': self.user.pk
        }
        
        serializer = BookSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())
        book = serializer.save()
        
        self.assertEqual(book.title, 'New Book')
        self.assertEqual(book.price, 34.99)
    
    def test_serializer_update(self):
        """
        Test Updating An Object Through The Serializer.
        """
        update_data = {
            'title': 'Updated Book',
            'author': self.author.pk,
            'publication_year': 2021,
            'genre': 'Updated Genre',
            'price': 39.99,
            'owner': self.user.pk
        }
        
        serializer = BookSerializer(instance=self.book, data=update_data)
        self.assertTrue(serializer.is_valid())
        book = serializer.save()
        
        self.assertEqual(book.title, 'Updated Book')
        self.assertEqual(book.price, 39.99)
    
    def test_nested_serializer(self):
        """
        Test Nested Serializer Relationships.
        """
        # Assuming BookSerializer includes nested AuthorSerializer
        serializer = BookSerializer(instance=self.book)
        data = serializer.data
        
        # Check That Author Data Is Nested
        self.assertIn('author', data)
        # self.assertEqual(data['author']['name'], 'Test Author')


#==============================================================================
# 6. TEST FIXTURES AND FACTORIES
#==============================================================================

"""
Using Fixtures And Factories For Cleaner Test Data Management.
"""

# Using Django fixtures
class FixtureTestCase(APITestCase):
    """
    Test case using Django fixtures.
    """
    fixtures = ['test_data.json']  # Load Data From Fixtures File
    
    def test_with_fixture_data(self):
        """
        Test Using Data Loaded From Fixtures.
        """
        # The Fixture Should Have Loaded Some Books
        self.assertTrue(Book.objects.exists())
        
        url = reverse('book-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Using Factory Boy For Test Data
"""
Install: pip install factory-boy

# factories.py
import factory
from django.contrib.auth.models import User
from .models import Book, Author


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'TestPass123')


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author
    
    name = factory.Faker('name')
    country = factory.Faker('country')
    birth_date = factory.Faker('date_of_birth')


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    
    title = factory.Faker('sentence', nb_words=4)
    author = factory.SubFactory(AuthorFactory)
    publication_year = factory.Faker('year')
    genre = factory.Faker('random_element', elements=['Fiction', 'Science Fiction', 'Mystery'])
    price = factory.Faker('pydecimal', left_digits=2, right_digits=2, positive=True)
    owner = factory.SubFactory(UserFactory)


# Usage In Tests
class FactoryTestCase(APITestCase):
    def setUp(self):
        # Create test data using factories
        self.user = UserFactory()
        self.author = AuthorFactory()
        self.books = BookFactory.create_batch(10, owner=self.user)
        
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    
    def test_with_factory_data(self):
        url = reverse('book-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 10)
"""


#==============================================================================
# 7. API CLIENT TESTING
#==============================================================================

"""
Testing Using the RequestsClient for more realistic HTTP testing.
"""

from rest_framework.test import RequestsClient


class LiveServerTestCase(APITestCase):
    """
    Test Cases Using RequestsClient For Live Server Testing.
    """
    
    def setUp(self):
        self.client = RequestsClient()
        
        self.user = User.objects.create_user(
            username='TestUser',
            password='TestPass123'
        )
        
        self.author = Author.objects.create(
            name='Test Author',
            country='USA'
        )
    
    def test_live_server_request(self):
        """
        Test Making Actual HTTP Requests To The Live Server.
        """
        # Login To Get Auth Token
        response = self.client.post(
            'http://testserver/api/token/',
            json={'username': 'TestUser', 'password': 'TestPass123'}
        )
        
        self.assertEqual(response.status_code, 200)
        token = response.json()['token']
        
        # Make Authenticated Request
        response = self.client.get(
            'http://testserver/api/books/',
            headers={'Authorization': f'Token {token}'}
        )
        
        self.assertEqual(response.status_code, 200)


#==============================================================================
# 8. COVERAGE AND BEST PRACTICES
#==============================================================================

"""
RUNNING TESTS
=============

1. Run All Tests:
   python manage.py test

2. Run Specific Test Case:
   python manage.py test myapp.tests.BookAPITestCase

3. Run Specific Test Method:
   python manage.py test myapp.tests.BookAPITestCase.test_create_book

4. Run Tests With Coverage:
   pip install coverage
   coverage run --source='.' manage.py test
   coverage report
   coverage html  # Generate HTML report


COVERAGE CONFIGURATION
======================

Create .coveragerc file:

[run]
source = .
omit = 
    */migrations/*
    */tests/*
    */venv/*
    */virtualenv/*
    manage.py
    */wsgi.py
    */asgi.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
    if __name__ == .__main__.:


BEST PRACTICES FOR API TESTING
================================

1. Test All HTTP Methods (GET, POST, PUT, PATCH, DELETE)
2. Test Authentication And Permissions
3. Test Input Validation And Error Handling
4. Test Edge Cases And Boundary Conditions
5. Use Descriptive Test Method Names
6. Keep Tests Isolated And Independent
7. Use setUp And tearDown For Test Data
8. Mock External Dependencies
9. Test Both Success And Failure Scenarios
10. Aim For High Test Coverage (>80%)


EXAMPLE: TESTING WITH MOCKING
==============================
"""

from unittest.mock import patch, Mock


class MockingTestCase(APITestCase):
    """
    Test Cases Demonstrating Mocking External Services.
    """
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='TestUser',
            password='TestPass123'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
    
    @patch('myapp.services.external_api_call')
    def test_external_api_integration(self, mock_api):
        """
        Test Integration With External API Using Mocks.
        """
        # Configure Mock
        mock_api.return_value = {'status': 'success', 'data': 'test data'}
        
        # Make Request That Calls External API
        url = reverse('book-list')
        response = self.client.get(url)
        
        # Assert Mock Was Called
        mock_api.assert_called_once()
        
        # Assert Response
        self.assertEqual(response.status_code, status.HTTP_200_OK)


"""
CONTINUOUS INTEGRATION SETUP
=============================

Example GitHub Actions Workflow (.github/workflows/tests.yml):

name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:13
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set Up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run Tests
      run: |
        python manage.py test
      env:
        DATABASE_URL: postgres://postgres:postgres@localhost:5432/test_db
    
    - name: Generate Coverage Report
      run: |
        coverage run --source='.' manage.py test
        coverage report
        coverage xml
    
    - name: Upload Coverage to Codecov
      uses: codecov/codecov-action@v2


TESTING CHECKLIST
=================

□ All CRUD Operations Tested
□ Authentication Tested
□ Permissions Tested
□ Input Validation Tested
□ Edge Cases Covered
□ Error Handling Tested
□ Custom Actions Tested
□ Filtering and Ordering Tested
□ Pagination Tested
□ Serializers Tested
□ Rate Limiting Tested
□ Coverage Above 80%
□ CI/CD Pipeline Configured
"""

# End of Chapter 06: Testing REST APIs