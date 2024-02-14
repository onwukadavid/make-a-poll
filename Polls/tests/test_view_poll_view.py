from django.test import TestCase
from django.urls import reverse
from Accounts.models import User
from Polls.models import Choice, Question

class TestViewPoll(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='TestUser', email = 'test@gmail.com')
        self.question1 = Question.objects.create(
            title='My question',
            slug='my-question',
            description='test description',
            question='Is this working',
            user=self.user1
            )
        self.question2 = Question.objects.create(
            title='My question2',
            slug='my-question2',
            description='test description2',
            question='Is this second test working',
            user=self.user1
            )
        
        self.choice1 = Choice.objects.create(question=self.question1, text='yes', votes=0)
        self.choice2 = Choice.objects.create(question=self.question1, text='no', votes=0)
        self.choice3 = Choice.objects.create(question=self.question1, text='maybe', votes=0)
        
        

    def test_view_poll_view_returns_200_for_poll_that_exists(self):
        url1 = reverse('polls:view-poll', kwargs={'username':self.user1.username, 'slug':self.question1.slug})
        response1 = self.client.get(url1)
        url2 = reverse('polls:view-poll', kwargs={'username':self.user1.username, 'slug':self.question2.slug})
        response2 = self.client.get(url2)
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)

    def test_view_poll_view_returns_404_for_poll_that_does_not_exists(self):
        url = reverse('polls:view-poll', kwargs={'username':self.user1.username, 'slug':'I-do-not-exist'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_view_poll_view_uses_the_right_template(self):
        url = reverse('polls:view-poll', kwargs={'username':self.user1.username, 'slug':self.question1.slug})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'Polls/detail_poll.html')

    def test_displays_data_for_only_a_single_poll(self):
        url1 = reverse('polls:view-poll', kwargs={'username':self.user1.username, 'slug':self.question1.slug})
        response1 = self.client.get(url1)
        url2 = reverse('polls:view-poll', kwargs={'username':self.user1.username, 'slug':self.question2.slug})
        response2 = self.client.get(url2)

        self.assertTrue('Is this working' in str(response1.content))
        self.assertTrue('Is this second test working' not in str(response1.content))

        self.assertTrue('Is this second test working' in str(response2.content))
        self.assertTrue('Is this working' not in str(response2.content))

    def test_view_contains_the_right_context(self):
        url = reverse('polls:view-poll', kwargs={'username':self.user1.username, 'slug':self.question1.slug})
        response = self.client.get(url)
        self.assertEqual(response.context['poll'], self.question1)

    def test_view_displays_its_choice(self):
        url = reverse('polls:view-poll', kwargs={'username':self.user1.username, 'slug':self.question1.slug})
        response = self.client.get(url)
        choices = self.question1.choices.all()

        for choice in choices:
            self.assertTrue(str(choice) in str(response.content))

    def test_view_dsplays_error_if_no_choice_was_selected(self):
        url = reverse('polls:vote', kwargs={'username':self.user1.username, 'slug':self.question1.slug})
        response = self.client.post(path=url, data={})

        self.assertTrue('You did not select a choice' in str(response.content))

    def test_view_redirects_after_submitting_a_choice(self):
        url = reverse('polls:vote', kwargs={'username':self.user1.username, 'slug':self.question1.slug})
        response = self.client.post(path=url, data={'choice':str(self.choice1.id)})

        self.assertRedirects(response, reverse('polls:result', kwargs={'username':self.user1.username, 'slug':self.question1.slug}))
        self.assertEqual(response.status_code, 302)

    # test form returns errors