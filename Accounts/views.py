from django.shortcuts import render, redirect
from Accounts.forms import UserRegistrationForm, userLoginForm
from Accounts.models import Author
from django.contrib.auth import authenticate, login


def register_user(request):
    context = []
    if request.method == 'post':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            author = Author.objects.create(
                username=username,
                email = email
            )
            author.set_password(password)
            author.is_active=True
            author.save()

            login(request, author)
            request.session["user"] = author
            # set session expiry age
            
            return redirect('polls:all-polls')
            
    else:
        user = request.session.get("user", False)
        if user:
            return redirect('polls:all-polls')
        
        request.session.set_test_cookie()
        form = UserRegistrationForm()

    context['form'] = form
    return render(request, 'Accounts/user-registration-form.html', context)


def login_user(request):
    context = []
    if request.method == 'POST':
        form = userLoginForm(request.POST)
        context['form'] = form

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                request.session["user"] = user
                # set session expiry age

                return redirect('polls:all-polls')
            else:
                form.add_error('Username/Password does not match')
        else:
            return render(request, 'Accounts/user-registration-form.html', context)
    else:
        user = request.session.get("user", False)
        if user:
            return redirect('polls:all-polls')
        
        form = userLoginForm(request.POST)
        context['form'] = form

        return render(request, 'Accounts/user-registration-form.html', context)

def update_user_details():
    ...

def delete_user():
    ...