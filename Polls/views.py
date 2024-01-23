from django.shortcuts import render
from Polls.models import Question
from django.shortcuts import get_object_or_404

def create_poll():
    ...

def view_poll(request, username, slug):
    
    poll = get_object_or_404(Question, user__username=username, slug=slug)
    context = {'poll':poll}
    return render(request, 'Polls/detail_poll.html', context)

def all_polls(request):
    polls = Question.objects.all().filter(status='published')[::1]
    context = {'polls':polls}
    return render(request, 'Polls/home.html', context)

def delete_poll():
    ...