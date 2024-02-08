from django import forms
from django.forms import formset_factory


STATUS = {
    'published':'PUBLISHED',
    'draft':'DRAFT'
}


class ChoiceForm(forms.Form):
    text = forms.CharField(max_length=255, label='Choice')

class QuestionForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    thumbnail = forms.ImageField(required=False)
    question = forms.CharField(max_length=255)
    status = forms.ChoiceField(choices=STATUS, widget=forms.Select)