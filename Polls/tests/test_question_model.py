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
    def test_field_label_for_question_model(self):
        title_label =self.question._meta.get_field('title').verbose_name
        slug_label =self.question._meta.get_field('slug').verbose_name
        description_label =self.question._meta.get_field('description').verbose_name
        thumbnail_label =self.question._meta.get_field('thumbnail').verbose_name
        question_label =self.question._meta.get_field('question').verbose_name
        pub_date_label =self.question._meta.get_field('pub_date').verbose_name
        updated_at_label =self.question._meta.get_field('updated_at').verbose_name
        status_label =self.question._meta.get_field('status').verbose_name

        self.assertEqual('title', title_label)
        self.assertEqual('slug', slug_label)
        self.assertEqual('description', description_label)
        self.assertEqual('thumbnail', thumbnail_label)
        self.assertEqual('question', question_label)
        self.assertEqual('Date published', pub_date_label)
        self.assertEqual('Last update', updated_at_label)
        self.assertEqual('status', status_label)

    def test_field_max_length_for_question_model(self):
        title_max_length = self.question._meta.get_field('title').max_length
        slug_max_length = self.question._meta.get_field('slug').max_length
        description_max_length = self.question._meta.get_field('description').max_length
        question_max_length = self.question._meta.get_field('question').max_length
        status_max_length = self.question._meta.get_field('status').max_length

        self.assertEqual(50, title_max_length)
        self.assertEqual(50, slug_max_length)
        self.assertEqual(50, description_max_length)
        self.assertEqual(255, question_max_length)
        self.assertEqual(9, status_max_length)

    # test question contains choices
    
    # test soft delete feature
