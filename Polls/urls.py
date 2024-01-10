from django.urls import path
from Polls import views

app_name = 'polls'

urlpatterns = [
    path('create-poll/', views.create_poll, name='create-poll'),
    path('polls/', views.all_polls, name='all-polls'),
    path('polls/<slug:slug>', views.view_poll, name='view-poll'),
    path('polls/<slug:slug>', views.delete_poll, name='delete-poll'),
]