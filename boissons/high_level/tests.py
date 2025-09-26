from django.test import TestCase
from .models import Localisation
from .models import Local
from .models import Machine


class MachineModelTests(TestCase):
    def test_machine_creation(self):
        self.assertEqual(Machine.objects.count(), 0)
        lolo = Localisation.objects.create(nom="Labège", taxes=50, prix_m2=2000)  # ok
        toto = Local.objects.create(nom="Local303", localisation=lolo, surface=40)
        Machine.objects.create(
            nom="Machine 1",
            prix_achat=1000,
            cout_maintenance=3000,
            # operateur="op1",
            debit=1200,
            surface=500,
            debit_energie=1200,
            taux_utilisation=24,
            local=toto,
        )
        Machine.objects.create(
            nom="Machine 2",
            prix_achat=2000,
            cout_maintenance=3000,
            # operateur="op1",
            debit=1200,
            surface=500,
            debit_energie=1200,
            taux_utilisation=24,
            local=toto,
        )
        # self.assertEqual(Machine.objects.count(), 1)
