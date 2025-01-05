import pytest
from customers.serializers import CustomerSerializer

"""
Test that the CustomerSerializer correctly serializes and deserializes customer data.

This test verifies that:
    * The serializer validates provided data successfully (`assert serializer.is_valid()`)
    * The saved customer object has the expected attributes (`assert customer.name == ...`)
"""
@pytest.mark.django_db
def test_customer_serializer():
    data = {'name': 'Test Customer', 'age': 30, 'gender': 'Male'}
    serializer = CustomerSerializer(data=data)
    assert serializer.is_valid()
    customer = serializer.save()
    assert customer.name == 'Test Customer'
    assert customer.age == 30
    assert customer.gender == 'Male'