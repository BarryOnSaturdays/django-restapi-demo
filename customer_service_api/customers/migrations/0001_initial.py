# Generated by Django 5.1.4 on 2025-01-04 13:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Prefer not to say', 'Prefer not to say')], max_length=20, null=True)),
                ('signup_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceInteraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction_date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('sentiment', models.CharField(blank=True, max_length=50, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interactions', to='customers.customer')),
            ],
        ),
    ]
