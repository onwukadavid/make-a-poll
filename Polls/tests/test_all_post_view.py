from django.test import TestCase, Client
from django.urls import reverse


class TestAllPostView(TestCase):
    
    def setUp(self):
        self.client = Client()

    # test home view returns 200
    def test_home_view_is_(self):
        url = reverse('polls:all-polls')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        print(url)

    # test home view contains different polls by different users
        
    # test home view contains only poll whose status is published
        
    # test each poll is properly hyperlinked to the poll details page
        
    # test 