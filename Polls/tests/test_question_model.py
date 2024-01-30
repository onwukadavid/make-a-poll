from django.test import TestCase
from Polls.models import Question, Choice
from Accounts.models import User
from django.template.defaultfilters import slugify
# import unittest


class TestQuestionModel(TestCase):

    def setUp(self):
        self.user = User(username='Test user', email='testuser@gmail.com')
        self.question = Question(title='Test poll', description='This is a test poll', question='Is it working', user=self.user)

    def test_default_status_is_published(self):
        self.assertEqual('published', self.question.status)

    def test_status_is_draft_if_saved_as_draft(self):
        question = Question(title='Test poll', description='This is a test poll', question='Is it working', status='draft')
        self.assertEqual('draft', question.status)

    #NOT WORKING
    # def test_slug_is_properly_created(self):
    #     title = 'My question'
    #     self.user1 = User.objects.create(username='TestUser', email = 'test@gmail.com')
    #     self.question1 = Question.objects.create(
    #         title=title,
    #         slug=slugify(title),
    #         description='test description',
    #         question='Is this working',
    #         user=self.user1
    #         )
    #     # self.question1.save()

    #     self.assertEqual('my-question', self.question.slug)

    def test_question_object_returns_title(self):
        self.assertEqual('Test poll', str(self.question))

    def test_question_belongs_to_a_single_user(self):
        user2 = User(username='Test user2', email='testuser2@gmail.com')
        self.assertEqual(self.user.username, self.question.user.username)
        self.assertNotEqual(user2.username, self.question.user.username)
        
    def test_question_contains_multiple_choices(self):
        ...

    # test str method
    def test_question_object_returns_question_name(self):
        self.assertEqual('Test poll', str(self.question))
        
    # test field labels
    
    # test soft delete feature
