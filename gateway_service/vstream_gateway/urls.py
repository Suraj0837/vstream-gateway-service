from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.gateway_login, name='gateway_login'),
    path('register/', views.gateway_register, name='gateway_register'),
    path('authorize_user/', views.gateway_authorize_user, name='gateway_authorize_user'),
]
