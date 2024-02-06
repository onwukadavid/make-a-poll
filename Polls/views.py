from django.shortcuts import render
from Polls.models import Question
from django.shortcuts import get_object_or_404
from Polls.forms import QuestionForm

def create_poll(request):
    context = {}

    if request.method == 'POST':
        poll_form = QuestionForm(request.POST, request.FILES)
        if poll_form.is_valid():
            Question.objects.create(
                user = request.user,
                title = poll_form.cleaned_data.get('title'),
                description = poll_form.cleaned_data.get('description'),
                thumbnail = poll_form.cleaned_data.get('thumbnail'),
                question = poll_form.cleaned_data.get('question'),
                status = poll_form.cleaned_data.get('status'),
            )
        else:
            context['error'] = "Form contains errors"
    else:
        poll_form = QuestionForm()
    
    context['poll_form'] = poll_form

    return render(request, 'Polls/create_poll.html', context)

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