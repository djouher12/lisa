from django.test import TestCase

from .models import Machine


class MachineModelTests(TestCase):
    def test_machine_creation(self):
        self.assertEqual(Machine.objects.count(), 0)
        Machine.objects.create(
            nom="Mélangeur",
            prix_achat=28_000,
            cout_maintenance=3000,
            operateur="op1",
            debit=1200,
            surface=500,
            debit_energie=1200,
            taux_utilisation=24,
        )
        self.assertEqual(Machine.objects.count(), 1)
