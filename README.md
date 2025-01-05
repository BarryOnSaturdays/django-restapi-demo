# django-restapi-demo
This demo project builds a RESTful API using Django, rendering with Swagger UI.
Also apply Unit test, Intergration test, authentication, authorization to the api.
## Django REST API Build up
- Environment Setup 
    - install Django Rest Framework
- Create Project and App 
- Create Models
- Create Serializers
- Create Views
    - Using class-based generics views
- Update URLs
    - both project level and app level
- Update Settings
    - Add `rest_framework` and `<model_name>` to INSTALLED_APPS
- Migrations
    - makemigrations and migrate
- Insert mock data into SQLite

## Swagger UI Build up
- Update Settings.py 
    - Add `drf_spectacular` to INSTALLED_APPS
    - REST_FRAMEWORK
    - SPECTACULAR_SETTINGS 
- Update URLs.py
    - both project level and app level

## Testing
### Unit test
- test serializer function
- write failed test cases to test out (missing field, wrong datatype, etc)
### Intergration test
- Views: Test the complete request-response cycle, including URL routing, view logic, serializer usage, and database interaction.
- API endpoints: authentication, permissions, and data handling.
