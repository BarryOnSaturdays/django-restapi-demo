from rest_framework import serializers
from .models import Customer, ServiceInteraction

class CustomerSerializer(serializers.ModelSerializer):
    interactions = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'

class ServiceInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceInteraction
        fields = '__all__'