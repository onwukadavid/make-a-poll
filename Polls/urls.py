from django.urls import path
from Polls import views

app_name = 'polls'

urlpatterns = [
    path('', views.all_polls, name='all-polls'),
    path('create-poll/', views.create_poll, name='create-poll'),
    path('<str:username>/<slug:slug>', views.view_poll, name='view-poll'),
    path('<str:username>/<slug:slug>', views.delete_poll, name='delete-poll'),
    path('<str:username>/<slug:slug>/vote', views.vote, name='vote'),
    path('<str:username>/<slug:slug>/result', views.result, name='result'),
    path('<str:username>/<slug:slug>/edit', views.edit_poll, name="edit-poll")
]