import pytest
from customers.serializers import CustomerSerializer


def test_customer_serializer():
    data = {'name': 'Test Customer', 'age': 30, 'gender': 'Male'}
    serializer = CustomerSerializer(data=data)
    assert serializer.is_valid()
    customer = serializer.save()
    assert customer.name == 'Test Customer'
    assert customer.age == 30
    assert customer.gender == 'Male'