from django import forms
from django.forms import ValidationError, formset_factory, inlineformset_factory
from django.forms import BaseFormSet, BaseInlineFormSet
from Polls.models import Question, Choice


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
    ChoiceFormset = formset_factory(ChoiceForm, BaseChoiceFormSet, extra=3, max_num=3)

# switch to model form so as to pass the model instance to the form
class QuestionForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    thumbnail = forms.ImageField(required=False)
    question = forms.CharField(max_length=255, required=True)
    status = forms.ChoiceField(choices=STATUS, widget=forms.Select, required=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Retrieve user object from kwargs
        super(QuestionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Question
        fields = ['title', 'description', 'thumbnail', 'question', 'status']

    # Check if title exists for a particular user. if it does return error
    def clean_title(self):
        
        title = self.cleaned_data['title']
        try:
            user = self.instance.user # if instance is passed, grab the user from the instance
        except Question.user.RelatedObjectDoesNotExist:
            user = self.user # grab the user from the kwargs, if instance isn't passed
        get_title = Question.objects.filter(title=title, user=user)
        
        if str(self.instance) is '':
            if get_title.exists():
                print('Hi1')
                raise ValidationError('Title already exists')
        else:
            if get_title.exists() and not(self.instance):
                print('Hi2')
                raise ValidationError('Title already exists')
        return title
    

class EditChoiceFormSet(forms.Form):
    EditChoiceFormset = formset_factory(ChoiceForm, BaseChoiceFormSet, extra=0) # check if poll has choice if not extra should not be 0

# class EditChoiceInlineFormset():
#     EditChoiceFormset = inlineformset_factory(Question, Choice, fields=['text'], max_num=3)