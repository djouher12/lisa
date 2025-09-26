from django.db import models


class Localisation(models.Model):
    nom = models.CharField(max_length=100)
    taxes = models.IntegerField()
    prix_m2 = models.IntegerField()

    def __str__(self):
        return self.nom

    def json(self):
        return {"nom": self.nom, "taxes": self.taxes, "prix_m2": self.prix_m2}


class Local(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.ForeignKey(
        Localisation,
        on_delete=models.PROTECT,
    )

    surface = models.IntegerField()

    def __str__(self):
        return self.nom

    def costs(self):
        s = 0
        for m in self.machine_set.all():
            s += m.costs()
        for p in self.produit_set.all():
            s += p.costs()
        s = (self.surface) * (self.localisation.taxes) * (self.localisation.prix_m2)
        print(s)

    def json(self):
        return {
            "nom": self.nom,
            "localisation": self.localisation,
            "surface": self.surface,
        }


class MatierePremiere(models.Model):
    nom = models.CharField(max_length=100)
    stock = models.IntegerField()
    emprise = models.IntegerField()

    def __str__(self):
        return self.nom

    def json(self):
        return {"nom": self.nom, "stock": self.stock, "emrpise": self.emprise}


class QuantiteMatierePremiere(models.Model):
    quantite = models.IntegerField()
    matiere_premiere = models.ForeignKey(
        MatierePremiere,
        on_delete=models.PROTECT,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.quantite), self.matierePremiere.nom

    def json(self):
        return {"quantite": self.quantite, "matiere_premiere": self.matiere_premiere}


class Energie(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    localisation = models.ForeignKey(
        Localisation,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.nom

    def json(self):
        return {" nom ": self.nom, "prix": self.prix, "localisation": self.localisation}


class DebitEnergie(models.Model):
    debit = models.IntegerField()
    energie = models.IntegerField()

    def __str__(self):
        return str(self.debit)

    def costs(self, debit_energetique):
        debit_energetique = (self.debit) * (self.energie)
        return debit_energetique

    def json(self):
        return {" debit": self.debit, "energie ": self.energie}


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix_de_vente = models.IntegerField()
    quantite = models.IntegerField()
    emprise = models.IntegerField()
    local = models.ForeignKey(
        Local,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.nom

    def costs(self, s):
        s = (self.quantite) * (self.prix_de_vente)
        return s

    def json(self):
        return {
            "nom ": self.nom,
            "prix_de_vente ": self.prix_de_vente,
            "quantite ": self.quantite,
            "emprise ": self.emprise,
            "local": self.local,
        }


class UtilisationMatierePremiere(MatierePremiere):
    pass


class ApprovisionnementMatierePremiere(models.Model):
    localisation = models.ForeignKey(
        Localisation,
        on_delete=models.PROTECT,
    )
    prix_unitaire = models.IntegerField()
    delais = models.IntegerField()

    def __str__(self):
        return self.localisation.nom

    def costs(self, s):
        s = (self.matiere_premiere.stock) * (self.prix_unitaire)
        return s

    def json(self):
        return {
            "localisation": self.localisation,
            "prix_unitaire": self.prix_unitaire,
            "delais": self.delais,
        }


class Metier(models.Model):
    nom = models.CharField(max_length=100)
    renumeration = models.IntegerField()

    def __str__(self):
        return self.nom

    def json(self):
        return {"nom": self.nom, "renumeration": self.renumeration}


class RessourceHumaine(models.Model):
    metier = models.ForeignKey(
        Metier,
        on_delete=models.PROTECT,
    )
    quantite = models.CharField(max_length=100)

    def __str__(self):
        return self.metier.nom

    def costs(self, s):
        s = (self.metier.renumeration) * (self.quantite)
        return s

    def json(self):
        return {"quantite": self.quantite, "metier": self.metier}


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix_achat = models.IntegerField()
    cout_maintenance = models.IntegerField()
    operateur = models.ManyToManyField(RessourceHumaine)
    debit = models.IntegerField()
    surface = models.IntegerField()
    debit_energie = models.IntegerField()
    taux_utilisation = models.IntegerField()
    local = models.ForeignKey(
        Local,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.nom

    def costs(self):
        return (
            (self.prix_achat)
            + (self.cout_maintenance)
            + (self.debit_energie) * (self.taux_utilisation)
        )

    def json(self):
        return {
            "nom": self.nom,
            "prix_achat": self.prix_achat,
            "cout_maintenance": self.cout_maintenance,
            "operateur": self.operateur,
            "debit": self.debit,
            "surface": self.surface,
            "debit_energie": self.debit_energie,
            "taux_utilisation": self.taux_utilisation,
            "local": self.local,
        }


class Fabrication(models.Model):
    produit = models.ForeignKey(
        Produit,
        on_delete=models.PROTECT,
    )
    utilisation_matiere_premiere = models.ManyToManyField(UtilisationMatierePremiere)
    machines = models.ManyToManyField(Machine)
    ressources_humaines = models.ManyToManyField(RessourceHumaine)

    def __str__(self):
        return self.produit.nom

    def json(self):
        return {
            "produit": self.produit,
            "utilisation_matiere_premiere": self.utilisation_matiere_premiere,
            "machines": self.machines,
            "ressources_humaines": self.ressources_humaines,
        }
