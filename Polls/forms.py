from django import forms


STATUS = {
    'published':'PUBLISHED',
    'draft':'DRAFT'
}


class QuestionForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    thumbnail = forms.ImageField(required=False)
    question = forms.CharField(max_length=255)
    status = forms.ChoiceField(choices=STATUS, widget=forms.Select)