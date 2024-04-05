from django import forms
from Accounts.models import Author
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


# Create Registeration form
class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(help_text='Passowrd must be long enough')
    password2 = forms.CharField()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = Author.objects.filter(username=username)

        if user.exists():
            raise ValidationError('This username has been taken')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data['password'] 
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password2 != password1:
            raise ValidationError('Passwords do not match')
        return password2

# create Login form if necessary
class userLoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    # username = forms.CharField(max_length=50)
    password = forms.CharField()

# create update form if necessary
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        user = Author.objects.filter(username=username)

        if user.exists():
            raise ValidationError('This username has been taken')
        
    def clean_email(self):
        email = self.cleaned_data['email']
        user = Author.objects.filter(email=email)

        if user.exists():
            raise ValidationError('This email already exists')
        
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Author
        # fields = ["email", "username"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Author
        fields = ["email", "username"]