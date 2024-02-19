from django.test import SimpleTestCase, TestCase
from Polls.forms import QuestionForm


class TestQuestionForm(TestCase):
    def test_question_form_labels(self):
        question_form = QuestionForm()

        self.assertTrue(question_form.fields['title'].label is None or question_form.fields['title'].label == 'Title')
        self.assertTrue(question_form.fields['description'].label is None or question_form.fields['description'].label == 'Description')
        self.assertTrue(question_form.fields['thumbnail'].label is None or question_form.fields['thumbnail'].label == 'Thumbnail')
        self.assertTrue(question_form.fields['question'].label is None or question_form.fields['question'].label == 'Question')
        self.assertTrue(question_form.fields['status'].label is None or question_form.fields['status'].label == 'Status')

    def test_question_form_is_vaid_for_valid_data(self):
        data={
            'title':'Valid data test', 
            'description':'This is to test for is valid with valid data',
            'question':'Is it working?',
            'status':'published'
            }
        question_form = QuestionForm(data=data)
        self.assertTrue(question_form.is_valid())


    def test_question_form_is_invaid_for_invalid_data(self):
        data={}
        question_form = QuestionForm(data=data)
        self.assertFalse(question_form.is_valid())

    def test_form_returns_false_if_title_field_max_length_is_exceeded(self):
        title=''
        for _ in range(51):
            title+='a'
        data={
            'title':title, 
            'description':'This is to test for is valid with valid data',
            'question':'Is it working?',
            'status':'published'
            }
        question_form = QuestionForm(data=data)
        self.assertFalse(question_form.is_valid())

    def test_form_returns_false_if_question_field_max_length_is_exceeded(self):
        question=''
        for _ in range(256):
            question+='a'
        data={
            'title':'A valid title', 
            'description':'This is to test for is valid with valid data',
            'question':question,
            'status':'published'
            }
        question_form = QuestionForm(data=data)
        self.assertFalse(question_form.is_valid())