from django.urls import path
from .views import get_info, test_redirect

urlpatterns = [
    path('', get_info),
    path('<str>/', test_redirect, name='test_redirect'),
]
