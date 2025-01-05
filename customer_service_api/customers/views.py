from rest_framework import generics, permissions
from .models import Customer, ServiceInteraction
from .serializers import CustomerSerializer, ServiceInteractionSerializer

# API views for handling Customer objects
class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Read access (GET requests) is allowed to anyone, but write access (POST, PUT, PATCH, DELETE) requires authentication.

# API views for handling ServiceInteraction objects
class InteractionListCreate(generics.ListCreateAPIView):
    queryset = ServiceInteraction.objects.all()
    serializer_class = ServiceInteractionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class InteractionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceInteraction.objects.all()
    serializer_class = ServiceInteractionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Read access (GET requests) is allowed to anyone, but write access (POST, PUT, PATCH, DELETE) requires authentication.