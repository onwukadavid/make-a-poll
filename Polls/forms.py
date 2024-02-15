from django import forms
from django.forms import formset_factory


STATUS = {
    'published':'PUBLISHED',
    'draft':'DRAFT'
}


class ChoiceForm(forms.Form):
    text = forms.CharField(max_length=255, label='Choice')

# This formset is used to generate and handle multiple Choice Form
class ChoiceFormFormSet():
    ChoiceFormset = formset_factory(ChoiceForm, extra=3)

    # Override Formset clean method to check if each form is valid.
    # The formset  is always value because it passes an empty string or a None value. So if any of the form should return this value. raise an error.

class QuestionForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    thumbnail = forms.ImageField(required=False)
    question = forms.CharField(max_length=255)
    status = forms.ChoiceField(choices=STATUS, widget=forms.Select)