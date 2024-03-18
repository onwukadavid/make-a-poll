from django import forms
from Accounts.models import Author
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


# Create Registeration form
class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    password = forms.PasswordInput()
    password2 = forms.PasswordInput()

    def clean_password2(self):
        password1 = self.cleaned_data['password'] 
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password2 != password1:
            raise ValidationError('Passwords do not match')
        return password2

# create Login form if necessary
class userLoginForm(forms.Form):
    email = forms.EmailField(max_length=50)
    password = forms.PasswordInput()

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
        
class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = Author
        fields = ["username", "email"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Author
        fields = ["username", "email", "password", "is_active", "is_admin"]