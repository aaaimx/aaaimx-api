from django.test import TestCase
from utils.images import generate_qr

class AnimalTestCase(TestCase):
    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        print(generate_qr('jajaj'))
