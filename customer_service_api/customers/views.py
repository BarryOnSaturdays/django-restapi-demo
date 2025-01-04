from rest_framework import generics, permissions
from .models import Customer, ServiceInteraction
from .serializers import CustomerSerializer, ServiceInteractionSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InteractionListCreate(generics.ListCreateAPIView):
    queryset = ServiceInteraction.objects.all()
    serializer_class = ServiceInteractionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InteractionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceInteraction.objects.all()
    serializer_class = ServiceInteractionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]