from rest_framework import generics
from .models import Customer, ServiceInteraction
from .serializers import CustomerSerializer, ServiceInteractionSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class InteractionListCreate(generics.ListCreateAPIView):
    queryset = ServiceInteraction.objects.all()
    serializer_class = ServiceInteractionSerializer

class InteractionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceInteraction.objects.all()
    serializer_class = ServiceInteractionSerializer