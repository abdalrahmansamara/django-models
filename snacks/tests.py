# from _typeshed import Self
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
# Create your tests here.

class test_Snack_page(TestCase):
    def test_status_code(self):
        self.assertEqual(self.client.get(reverse('home')).status_code, 200)
    def test_template_used(self):
        self.assertEqual(self.client.get(reverse('home')).templates[0].name ,'snack_list.html')
        self.assertEqual(self.client.get(reverse('home')).templates[1].name ,'base.html')