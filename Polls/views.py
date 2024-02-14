from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, redirect, render
from django.urls import reverse
from Polls.models import Choice, Question
from django.shortcuts import get_object_or_404
from Polls.forms import ChoiceForm, QuestionForm

def create_poll(request):
    context = {}
    ChoiceFormset = formset_factory(ChoiceForm, extra=3)

    if request.method == 'POST':
        formset = ChoiceFormset(request.POST)
        poll_form = QuestionForm(request.POST, request.FILES)
        if poll_form.is_valid() and formset.is_valid():
            question = Question(
                user = request.user,
                title = poll_form.cleaned_data.get('title'),
                description = poll_form.cleaned_data.get('description'),
                thumbnail = poll_form.cleaned_data.get('thumbnail'),
                question = poll_form.cleaned_data.get('question'),
                status = poll_form.cleaned_data.get('status'),
            )
            question.save()
            # pass
            for i in range(len(formset)):
                Choice.objects.create(
                    question=question,
                    text = formset.cleaned_data[i].get('text')
                )
            return HttpResponseRedirect(reverse('polls:all-polls'))#work on this
        else:
            context['error'] = "Form contains errors"
    else:
        poll_form = QuestionForm()
        formset = ChoiceFormset()
    
    # context = {'poll_form':poll_form, 'formset':formset}
    context['poll_form'] = poll_form
    context['formset'] = formset

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

def vote(request, username, slug):
    poll = get_object_or_404(Question, user__username=username, slug=slug)
    try:
        choice_id = request.POST.get('choice')
        selected_choice = poll.choices.get(pk=choice_id)
    except (KeyError,  Choice.DoesNotExist):
        context = {'poll':poll, 'error_message':'You did not select a choice'}
        return render(request, 'Polls/detail_poll.html', context)
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=[username, slug]))


def result(request, username, slug):
    poll = get_object_or_404(Question, user__username=username, slug=slug)
    choices = get_list_or_404(Choice, question=poll)

    context = {'choices':choices, 'poll':poll}
    return render(request, 'Polls/result.html', context)