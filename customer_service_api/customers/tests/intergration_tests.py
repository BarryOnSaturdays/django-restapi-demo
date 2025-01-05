import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from customers.models import Customer
from rest_framework import status

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user(django_user_model):
    user = django_user_model.objects.create_user(username='testuser', password='testpassword')
    return user

@pytest.mark.django_db
def test_create_customer(api_client, test_user):
    api_client.force_authenticate(user=test_user)
    data = {'name': 'Test Customer', 'age': 30, 'gender': 'Male'}
    response = api_client.post('/api/customers/', data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Customer.objects.count() == 1
    customer = Customer.objects.get()
    assert customer.name == 'Test Customer'
    assert customer.age == 30
    assert customer.gender == 'Male'

@pytest.mark.django_db
def test_create_customer_unauthenticated(api_client):
    data = {'name': 'Test Customer', 'age': 30, 'gender': 'Male'}
    response = api_client.post('/api/customers/', data, format='json')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

@pytest.mark.django_db
def test_get_customer(api_client, test_user):
    customer = Customer.objects.create(name='Existing Customer', age = 25, gender = 'Female') #setup
    api_client.force_authenticate(user=test_user)
    response = api_client.get(f'/api/customers/{customer.pk}/', format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Existing Customer'