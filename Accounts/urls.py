from django.urls import path
from Accounts import views

app_name = 'accounts'

urls = [
    path('register/', views.register_user(), name='register'),
    path('login/', views.login_user(), name='login'),
]