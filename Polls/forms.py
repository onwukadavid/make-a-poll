from django import forms

class QuestionForm(forms.Forms):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)
    thumbnail = forms.ImageField()
    question = forms.CharField(max_length=255)
    status = forms.CharField()