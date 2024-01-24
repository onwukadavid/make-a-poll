from django.test import TestCase, Client
from django.urls import reverse
from Polls.models import Question


class TestAllPostView(TestCase):
    
    def setUp(self):
        self.client = Client()
        # question = Question.objects.create(title='My question')

    # test home view returns 200
    def test_home_view_is_(self):
        url = reverse('polls:all-polls')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        print(response.content)
        print(url)

    # test home view contains title, description, status, owner
    # def test_home_view_poll_contains_title_description_status_owner(self):
    #     url = reverse('polls:all-polls')
    #     response = self.client.get(url)
    #     self.assertContains(response.content, 'First poll')
    #     print(response)

    # test home view contains different polls by different users
        
    # test home view contains only poll whose status is published
        
    # test each poll is properly hyperlinked to the poll details page
        
    # test the home view uses the right template
        
    # test the home view contains the right context
        
    