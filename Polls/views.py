from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, redirect, render
from django.urls import reverse
from Polls.models import Choice, Question
from django.shortcuts import get_object_or_404
from Polls.forms import ChoiceForm, QuestionForm, ChoiceFormFormSet, EditChoiceFormSet

def create_poll(request):
    context = {}
    user=request.user

    if request.method == 'POST':
        formset = ChoiceFormFormSet.ChoiceFormset(request.POST)
        poll_form = QuestionForm( request.POST, request.FILES, instance=None, user=user)
        if poll_form.is_valid() and formset.is_valid():
            question = Question(
                user = user,
                title = poll_form.cleaned_data.get('title'),
                description = poll_form.cleaned_data.get('description'),
                thumbnail = poll_form.cleaned_data.get('thumbnail'),
                question = poll_form.cleaned_data.get('question'),
                status = poll_form.cleaned_data.get('status'),
            )
            question.save()
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
        formset = ChoiceFormFormSet.ChoiceFormset()
    
    context['poll_form'] = poll_form
    context['formset'] = formset

    return render(request, 'Polls/create_poll.html', context)

def view_poll(request, username, slug):
    
    poll = get_object_or_404(Question, user__username=username, slug=slug)
    context = {'poll':poll}
    return render(request, 'Polls/detail_poll.html', context)

def all_polls(request):
    # polls = Question.objects.all().filter(status='published')[::1]
    polls = Question.objects.all()[::1]
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


# Form creates new poll rather than update existing poll
def edit_poll(request, username, slug):
    # get the object
    context = {}
    poll = get_object_or_404(Question, user__username=username, slug=slug)
    choices = get_list_or_404(Choice, question=poll)
    user = request.user
    

    # check if the post or get method
    if request.method == 'POST':

        # populate the poll form and choice formset
        poll_form = QuestionForm(request.POST, instance=poll)
        # print(poll)
        formset = EditChoiceFormSet.EditChoiceFormset(request.POST)

        # check if the forms are valid
        if poll_form.is_valid() and formset.is_valid():

            poll.user = user
            poll.title = poll_form.cleaned_data.get('title')
            poll.description = poll_form.cleaned_data.get('description')
            poll.thumbnail = poll_form.cleaned_data.get('thumbnail')
            poll.question = poll_form.cleaned_data.get('question')
            poll.status = poll_form.cleaned_data.get('status')
            poll.save()

            # Fix this. ChoiceFormset should return just 3 forms and should be updated

            # check if choice exists on question i.e question.choices
            # print(len(formset.forms))
            for i in range(len(choices)):
            # iterate over form and choice list and assign their values
                choices[i].text = formset[i].cleaned_data.get('text')
                choices[i].save()
                continue

            # redirect on success
            return HttpResponseRedirect(redirect_to=reverse('polls:all-polls'))
        else:

            # return error on fail
            context['error'] = 'An error occurred'
    else:
        initial_data = {
                'user':request.user,
                'title':poll.title,
                'description':poll.description,
                'thumbnail':poll.thumbnail,
                'question':poll.question,
                'status':poll.status,
            }
        initial_formset_data = [{'text':c.text} for c in poll.choices.all()]

        # This should be in forms.py
        # extra = 3 - len(initial_formset_data)
        # EditChoiceFormset = formset_factory(ChoiceForm, extra=extra)7

        # fix choice formset to save
        poll_form = QuestionForm(initial=initial_data)
        formset = EditChoiceFormSet.EditChoiceFormset(initial=initial_formset_data)

    context['poll_form'] = poll_form
    context['formset'] = formset
    context['poll'] = poll

    # render on get request
    return render(request, 'Polls/edit_poll.html', context=context)