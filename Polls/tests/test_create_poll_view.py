from django.forms import formset_factory
from django.test import TestCase
from django.urls import reverse
from Accounts.models import User
from Polls.forms import QuestionForm, ChoiceFormFormSet


class TestCreatePollView(TestCase):
    def setUp(self):
        self.url = reverse('polls:create-poll')
        self.response = self.client.get(self.url)
        self.user1 = User.objects.create(username='TestUser', email = 'test@gmail.com', password='password')
        self.data = {
            'title':'My question',
            'description':'test description',
            'question':'Is this working',
            'user':self.user1,
            'status':'published',
            # 'thumbnail':None
            'form-TOTAL_FORMS': 3,
            'form-INITIAL_FORMS': 0,
            'form-MIN_NUM_FORMS': 0,
            'form-MAX_NUM_FORMS': 1000,
            'form-0-text': 'yes',
            'form-1-text': 'no',
            'form-2-text': 'maybe',
        }
    
    def test_create_view_returns_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_create_poll_view_uses_the_right_template(self):
        self.assertTemplateUsed(self.response, 'Polls/create_poll.html')

    def test_create_poll_view_uses_the_right_context(self):
        self.assertTrue('poll_form' in self.response.context)
        self.assertTrue('formset' in self.response.context)

    # will test when i create login endpoint
    # def test_create_poll_view_redierct_to_homepage_when_form_is_valid(self):
    #     login = self.client.login(username='TestUser', password='password')
    #     response = self.client.post(path=self.url, data=self.data)
    #     print(response.content)

    #     self.assertRedirects(response, reverse('polls:all-polls'))

    def test_create_polls_view_returns_the_same_page_if_data_is_invalid(self):
        response = self.client.post(path=self.url, data={})
        self.assertEqual(response.status_code, 200)

    def test_create_poll_view_displays_error_if_empty_data_was_sent(self):
        response = self.client.post(path=self.url, data={})
        self.assertTrue('This field is required' in str(response.content))
        self.assertTrue('Form contains errors' in str(response.content))
        self.assertTrue('error' in response.context)

    def test_create_poll_view_uses_the_right_form(self):
        self.assertIsInstance(self.response.context.get('poll_form'), QuestionForm)
        self.assertIsInstance(self.response.context.get('formset'), ChoiceFormFormSet.ChoiceFormset)

    def test_choice_for_formset_returns_3_forms(self):
        num_of_forms_in_formset = len(self.response.context.get('formset').forms)
        self.assertEqual(num_of_forms_in_formset, 3)

    def test_create_poll_view_displays_error_if_empty_formset_data_was_sent(self):
        data = {
        'title':'My question',
        'description':'test description',
        'question':'Is this working',
        'user':self.user1,
        'status':'published',
        'form-TOTAL_FORMS': 3,
        'form-INITIAL_FORMS': 0,
        'form-MIN_NUM_FORMS': 0,
        'form-MAX_NUM_FORMS': 1000,
        'form-0-text': '',
        'form-1-text': '',
        'form-2-text': '',
        }
        response = self.client.post(path=self.url, data=data)
        self.assertTrue('Please provide a text for this choice.' in str(response.content))

# Can only test endpoint when i create login endpoint
    # def test_question_cannot_be_created_if_title_already_exists(self):
    #     login = self.client.login(username=self.user1.username, password=self.user1.password)
        
    #     response1 = self.client.post(path=self.url, data=self.data)
    #     print(response1.status_code)
    #     response2 = self.client.post(path=self.url, data=self.data)
    #     print(response2.status_code)
    #     self.assertTrue('Title already exists.' in str(response2.content))