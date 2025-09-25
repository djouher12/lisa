from django.test import TestCase

from .models import Machine


class MachineModelTests(TestCase):
    def test_machine_creation(self):
        self.assertEqual(Machine.objects.count(), 0)
        Machine.objects.create(nom="Mélangeur", prix=28_000)
        self.assertEqual(Machine.objects.count(), 1)
