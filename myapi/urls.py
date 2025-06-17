# myapi/urls.py
from django.urls import path
from .views import register, public_view, protected_view

urlpatterns = [
    path('public/', public_view),
    path('protected/', protected_view),
    path('register/', register, name='register'),
]
