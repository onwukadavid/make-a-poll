from django import forms
from django.forms import ValidationError, formset_factory
from django.forms import BaseFormSet
from Polls.models import Question


STATUS = {
    'published':'PUBLISHED',
    'draft':'DRAFT'
}


class ChoiceForm(forms.Form):
    text = forms.CharField(max_length=255, label='Choice')


# This class inherits from BaseFormSet. This is use to override the validation behaviour of a formset.
# The formset.is_valid is always True because it passes an empty string or a None value as default value. 
#So if any of the form should return the default value. raise a validation error.
class BaseChoiceFormSet(BaseFormSet):
    def clean(self):
        if any(self.errors):
            return
        
        for form in self.forms:
            choice_text = form.cleaned_data.get('text')
            if choice_text == None or choice_text == "":
                form.add_error('text',  "Please provide a text for this choice.")
                # raise ValidationError("Please provide a text for all choice fields.")
            

# This formset is used to generate and handle multiple Choice Form
class ChoiceFormFormSet:
    ChoiceFormset = formset_factory(ChoiceForm, BaseChoiceFormSet, extra=3)

class QuestionForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    thumbnail = forms.ImageField(required=False)
    question = forms.CharField(max_length=255)
    status = forms.ChoiceField(choices=STATUS, widget=forms.Select)

    def clean_title(self):
        title = self.cleaned_data['title']
        get_title = Question.objects.filter(title=title)
        if get_title.exists():
            raise ValidationError('Title already exists.')
        return title
    

class EditChoiceFormSet(forms.Form):
    EditChoiceFormset = formset_factory(ChoiceForm, BaseChoiceFormSet, extra=0) # check if poll has choice if not extra should not be 0