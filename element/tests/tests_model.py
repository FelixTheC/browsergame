from django.test import TestCase
from ..models import Element


class ElementModelTest(TestCase):

    def test_create_new_element(self):
        element = Element.objects.create(name='wind', description='wind element')
        self.assertIsNotNone(element)
        self.assertIsInstance(element, Element)

    def test_fail_create_new_element(self):
        element = Element.objects.create(description='empty name')
        self.assertIsNone(element)