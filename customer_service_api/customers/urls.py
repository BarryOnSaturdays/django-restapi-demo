from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', views.CustomerRetrieveUpdateDestroy.as_view(), name='customer-retrieve-update-destroy'),
    path('interactions/', views.InteractionListCreate.as_view(), name='interaction-list-create'),
    path('interactions/<int:pk>/', views.InteractionRetrieveUpdateDestroy.as_view(), name='interaction-retrieve-update-destroy'),
]