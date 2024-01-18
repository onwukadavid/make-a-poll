from django.test import TestCase
from Polls.models import Question, Choice
from Accounts.models import User
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

    # def test_slug_is_properly_created(self):
    #     self.assertEqual('test-poll', self.question.slug)

    def test_question_object_returns_title(self):
        self.assertEqual('Test poll', str(self.question))

    def test_question_belongs_to_a_single_user(self):
        user2 = User(username='Test user2', email='testuser2@gmail.com')
        self.assertEqual(self.user.username, self.question.user.username)
        self.assertNotEqual(user2.username, self.question.user.username)
        
    def test_question_contains_multiple_questions(self):
        ...

