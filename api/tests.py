from django.test import TestCase
from django.urls import resolve

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        print("Tests executed")
