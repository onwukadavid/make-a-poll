from django.test import TestCase
from Polls.models import Question, Choice
from Accounts.models import User


class TestChoiceModel(TestCase):
    def setUp(self):
        self.user = User(username='Test user', email='testuser@gmail.com')
        self.question = Question(title='Test poll', description='This is a test poll', question='Is it working')
        self.choice1 = Choice(question=self.question, text='Yes', votes=0)
        self.choice2 = Choice(question=self.question, text='No', votes=0)

    def test_choice_belongs_to_a_question(self):
        self.assertEqual(self.question.title, self.choice1.question.title)

    # test str method
        
    # test field labels
        
    # test soft delete feature