from django.forms import formset_factory
from django.test import TestCase
from django.urls import reverse
from Accounts.models import User
from Polls.forms import QuestionForm, ChoiceForm


class TestCreatePollView(TestCase):
    def setUp(self):
        self.url = reverse('polls:create-poll')
        self.response = self.client.get(self.url)
        # self.user1 = User.objects.create(username='TestUser', email = 'test@gmail.com')
        # self.data = {
        #     'title':'My question',
        #     'description':'test description',
        #     'question':'Is this working',
        #     'user':self.user1,
        #     'status':'published',
        #     # 'thumbnail':None
        #     'choices-TOTAL_FORMS': 3,
        #     'choices-INITIAL_FORMS': 0,
        #     'choices-MIN_NUM_FORMS': 0,
        #     'choices-MAX_NUM_FORMS': 1000,
        #     'choices-0-text': 'yes',
        #     'choices-1-text': 'no',
        #     'choices-2-text': 'maybe',
        #     # 'choices-0-votes': 0,
        #     # 'choices-1-votes': 0,
        #     # 'choices-2-votes': 0,
        #     # 'choices-0-id': '',
        #     # 'choices-1-id': '',
        #     # 'choices-2-id': '',
        #     # 'choices-0-question': '',
        # }
    
    def test_create_view_returns_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_create_poll_view_uses_the_right_template(self):
        self.assertTemplateUsed(self.response, 'Polls/create_poll.html')

    def test_create_poll_view_uses_the_right_context(self):
        self.assertTrue('poll_form' in self.response.context)
        self.assertTrue('formset' in self.response.context)

    # # Fix this test
    # def test_create_poll_view_redierct_to_homepage_when_form_is_valid(self):
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
        ChoiceFormset = formset_factory(ChoiceForm, extra=3)
        self.assertIsInstance(self.response.context.get('poll_form'), QuestionForm)
        # self.assertIsInstance(self.response.context.get('formset'), ChoiceFormset) fix this