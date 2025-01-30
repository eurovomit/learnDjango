from django.test import TestCase, SimpleTestCase
from django.urls import reverse


class IndexTests(SimpleTestCase):
    def test_url(self):
        response = self.client.get('/learn/')
        self.assertEqual(response.status_code, 200)

    def test_name(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "learnDjango/index.html")

    def test_template_content(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, "index")