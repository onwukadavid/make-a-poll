from django.urls import path
from Polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.all_polls, name='all-polls'),
    path('create-poll/', views.create_poll, name='create-poll'),
    path('polls/<str:username>/<slug:slug>', views.view_poll, name='view-poll'),
    path('polls/<str:username>/<slug:slug>', views.delete_poll, name='delete-poll'),
]