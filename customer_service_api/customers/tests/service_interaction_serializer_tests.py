import pytest
from customers.serializers import ServiceInteractionSerializer
from customers.models import ServiceInteraction, Customer
from datetime import datetime

# Fixture to create a test customer object for the tests
@pytest.fixture
def test_customer(db): # db fixture is provided by pytest-django
    return Customer.objects.create(name="Test Customer", age=30, gender="Male")

# Test ServiceInteractionSerializer correctly validates and saves valid data
def test_service_interaction_serializer_valid(test_customer):
    data = {
        'customer': test_customer.pk,  # Use the primary key
        'text': 'Test interaction text.',
        'sentiment': 'positive',
        'interaction_date': datetime.now().isoformat()
    }
    serializer = ServiceInteractionSerializer(data=data)
    assert serializer.is_valid()
    interaction = serializer.save()
    assert interaction.customer == test_customer
    assert interaction.text == 'Test interaction text.'
    assert interaction.sentiment == 'positive'

# Test ServiceInteractionSerializer handles missing required fields
def test_service_interaction_serializer_invalid(test_customer):
    # Missing required field 'text'
    data = {
        'customer': test_customer.pk,
        'sentiment': 'positive',
        'interaction_date': datetime.now().isoformat()
    }
    serializer = ServiceInteractionSerializer(data=data)
    assert not serializer.is_valid()
    assert 'text' in serializer.errors


# Test ServiceInteractionSerializer handles non-existent customer references
def test_service_interaction_serializer_invalid_customer(db):
    data = {
        'customer': 999,  # Non-existent customer pk
        'text': 'Test interaction text.',
        'sentiment': 'positive',
        'interaction_date': datetime.now().isoformat()
    }
    serializer = ServiceInteractionSerializer(data=data)
    assert not serializer.is_valid()
    assert 'customer' in serializer.errors