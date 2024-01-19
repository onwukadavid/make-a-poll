from django.shortcuts import render
from Polls.models import Question

def create_poll():
    ...

def view_poll():
    ...

def all_polls(request):
    polls = Question.objects.all()[::-1]
    context = {'polls':polls}
    return render(request, 'Polls/home.html', context)

def delete_poll():
    ...