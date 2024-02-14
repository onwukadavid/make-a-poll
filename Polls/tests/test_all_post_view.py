from django.test import TestCase, Client
from django.urls import reverse, resolve
from Polls.models import Question
from Accounts.models import User


class TestAllPostView(TestCase):
    
    def setUp(self):
        self.url = reverse('polls:all-polls')

        self.user1 = User.objects.create(username='TestUser', email = 'test@gmail.com')
        self.user2 = User.objects.create(username='TestUser2',email = 'test2@gmail.com')
        self.question1 = Question.objects.create(
            title='My question',
            slug='my-question',
            description='test description',
            question='Is this working',
            user=self.user1
            )


    # test home view returns 200
    def test_home_view_returns_200(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)

    # test home view contains title, description, status, owner
    def test_home_view_poll_contains_title_description_status_owner(self):
        response = self.client.get(self.url)

        self.assertIn('My question', str(response.content)) # can also use assertContains
        self.assertIn('test description', str(response.content)) # can also use assertContains
        self.assertIn('published', str(response.content)) # can also use assertContains

    # test home view contains different polls by different users
    def test_home_view_contains_polls_by_different_users(self):
        question2 = Question.objects.create(
        title='My question2',
        slug='my-question2',
        description='test description2',
        question='Is this working2',
        user=self.user2
        )
        response = self.client.get(self.url)

        self.assertContains(response, 'My question')
        self.assertContains(response, 'My question2')
        
        
    # test home view contains only poll whose status is published
    def test_home_view_contains_only_polls_whose_status_is_published(self):
        question3 = Question.objects.create(
        title='My question3',
        slug='my-question3',
        description='test description3',
        question='Is this working3',
        user=self.user2,
        status='draft'
        )
        response = self.client.get(self.url)

        self.assertIn('My question', str(response.content))
        self.assertTrue('My question3' not in str(response.content))
        
    # test each poll is properly hyperlinked to the poll details page
    def test_each_poll_is_properly_hyperlinked_to_the_poll_details_page(self):
        response = self.client.get(self.url)

        username = self.user1.username
        question_slug = self.question1.slug
        details_page_url = reverse('polls:view-poll', kwargs={'username':username, 'slug':question_slug})
        self.assertContains(response, details_page_url)
        
    # test the home view uses the right template
    def test_home_uses_correct_template(self):
        response = self.client.get(self.url)

        self.assertTemplateUsed(response, 'Polls/home.html')
        
    # test the home view contains the right context
    def test_home_view_contains_the_right_context(self):
        response = self.client.get(self.url)
        for poll in response.context['polls']:
            self.assertEqual(str(poll), 'My question')
        # test length of polls returned
            
    # test home view resolves home url
    def test_home_url_resolves_home_url_name(self):
        view = resolve('/polls/')
        self.assertEqual('all-polls', view.url_name) 