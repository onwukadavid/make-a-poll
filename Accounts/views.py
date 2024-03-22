from django.shortcuts import render, redirect
from Accounts.forms import UserRegistrationForm, userLoginForm, UserUpdateForm
from Accounts.models import Author
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required


def register_user(request):
    context = {}
    if request.method == 'POST':
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
            request.session["user"] = author.email
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
    context = {}
    if request.method == 'POST':
        form = userLoginForm(request.POST)
        context['form'] = form

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                request.session["user"] = user.id
                # set session expiry age
                # request.session.set_expiry(10)

                return redirect('polls:all-polls')
            else:
                error = 'Username/Password does not match'
                context['error'] = error
    else:
        user = request.session.get("user", False)
        print(user)
        if user:
            return redirect('polls:all-polls')
        
        form = userLoginForm()

    context['form'] = form
    return render(request, 'Accounts/user-login-form.html', context)

def update_user_details(request, email):
    context = {}
    author = Author.objects.get(email=email)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=author)
        context['form'] = form
        if form.is_valid():
            author['username'] = request.POST.get('username')
            author['email'] = request.POST.get('email')
            author.save()
        else:
            context['form'] = form
        return render('Accounts/user-update-form.html', context=context)
    else:
        initial_data = {
            'usernme':author.username,
            'email':email
        }
        form = UserUpdateForm(initial=initial_data)
        context['form'] = form
        return render('Accounts/user-update-form.html', context=context)

@permission_required('can_ban_user')
def delete_user(request, email):
    author = Author.objects.get(email=email)
    author.is_active = False
    author.save()
    return redirect('polls:all-polls')

def logout_user(request):
    print(request.session['user'])
    try:
        # request.session.flush()
        del request.session['user']
        print(request.session['user'])

    except KeyError:
        pass
    return redirect('polls:all-polls')
    # return redirect('accounts:login')
