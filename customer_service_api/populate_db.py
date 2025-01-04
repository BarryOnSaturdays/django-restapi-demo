import os
import django
import random
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'customer_service_api.settings')
django.setup()

from customers.models import Customer, ServiceInteraction

def populate_db(num_customers=10, num_interactions_per_customer=5):
    genders = ['Male', 'Female', 'Other', 'Prefer not to say']
    for i in range(num_customers):
        customer = Customer.objects.create(
            name=f"Customer {i+1}",
            age=random.randint(18, 90),  # Random age between 18 and 90
            gender=random.choice(genders), # Random Gender option
        )

        for j in range(num_interactions_per_customer):
            random_days = random.randint(0, 30)
            interaction_date = datetime.now() - timedelta(days=random_days)
            ServiceInteraction.objects.create(
                customer=customer,
                text=f"This is interaction {j+1} with customer {i+1}. Some sample text.",
                sentiment=random.choice(["positive", "negative", "neutral"]),
                interaction_date = interaction_date
            )

if __name__ == "__main__":
    populate_db()
    print("Database populated with mock data.")