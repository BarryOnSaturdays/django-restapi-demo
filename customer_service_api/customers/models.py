from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(blank=True, null=True)  # Age field
    gender = models.CharField(max_length=20, blank=True, null=True, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say'),
    ])  # Gender field with choices
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ServiceInteraction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='interactions')
    interaction_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    sentiment = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Interaction with {self.customer} on {self.interaction_date}"