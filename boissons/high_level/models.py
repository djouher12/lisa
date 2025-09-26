from django.db import models


class Localisation(models.Model):
    nom = models.CharField(max_length=100)
    taxes = models.IntegerField()
    prix_m2 = models.IntegerField()

    def __str__(self):
        return self.nom


class Local(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.ForeignKey(
        Localisation,
        on_delete=models.PROTECT,
    )
    surface = models.IntegerField()

    def __str__(self):
        return self.nom

    def costs(self, s):
        s = (self.surface) * (self.localisation.taxes) * (self.localisation.prix_m2)
        return s


class MatierePremiere(models.Model):
    nom = models.CharField(max_length=100)
    stock = models.IntegerField()
    emprise = models.IntegerField()

    def __str__(self):
        return self.nom


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


class Energie(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    localisation = models.ForeignKey(
        Localisation,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.nom


class DebitEnergie(models.Model):
    debit = models.IntegerField()
    energie = models.IntegerField()

    def __str__(self):
        return str(self.debit)

    def costs(self, debit_energetique):
        debit_energetique = (self.debit) * (self.energie)
        return debit_energetique


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


class Metier(models.Model):
    nom = models.CharField(max_length=100)
    renumeration = models.IntegerField()

    def __str__(self):
        return self.nom


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
