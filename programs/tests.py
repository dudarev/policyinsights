from django.contrib.auth.models import User
from django.test import TestCase

# TODO: consider using Request Factory to test views directly
# from django.test import RequestFactory

from django.test import Client
from django.urls import reverse

from locations.models import Location
from programs.models import Program


class AutocompleteTest(TestCase):
    def setUp(self):
        User.objects.all().delete()
        self.user = User.objects.create(username='testuser', password='12345')
        self.client = Client()
        self.client.force_login(user=self.user, backend=None)

    def test_search_keywords(self):
        # create location
        response = self.client.post(reverse('location-create'), {"content": "Location", "slug": "location"})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Location.objects.count(), 1)

        # create program with search_keywords
        response = self.client.post(reverse('program-create'), {
            "content": "Program\nsearch_keywords: education",
            "slug": "program",
            "location": "location"
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Program.objects.count(), 1)

        # program is found by search_keywords
        response = self.client.get(reverse('program-autocomplete'), {"term": "education"})
        self.assertTrue(len(response.json()), 1)
