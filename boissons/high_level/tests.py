from django.test import TestCase
from .models import Localisation
from .models import Local
from .models import Machine


class MachineModelTests(TestCase):
    def test_machine_creation(self):
        self.assertEqual(Machine.objects.count(), 0)
        lolo = Localisation.objects.create(nom="Lyon", taxes=20, prix_m2=6000)
        toto = Local.objects.create(nom="Local303", localisation=lolo, surface=40)
        Machine.objects.create(
            nom="Mélangeur",
            prix_achat=28_000,
            cout_maintenance=3000,
            # operateur="op1",
            debit=1200,
            surface=500,
            debit_energie=1200,
            taux_utilisation=24,
            local=toto,
        )
        self.assertEqual(Machine.objects.count(), 1)
