from django.urls import path, include
from .views import asosiy

urlpatterns = [
    path('', asosiy, name='contact')
]