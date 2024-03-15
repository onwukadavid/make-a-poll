from django.urls import path
from Accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('<str:usernam>/update/', views.update_user_details, name='update-user'),
    path('<str:username>/delete/', views.delete_user, name='delete-user')
]