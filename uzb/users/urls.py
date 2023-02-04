from django.urls import path, include
from .views import *

urlpatterns = [
    path('login', log, name='log'),
    path('register', reg, name='reg'),
    path('profile', prof, name='prof'),
    path('logout', log, name='lout')
]
