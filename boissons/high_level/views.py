from django.views.generic import DetailView
from django.http import JsonResponse
from . import models


class LocalisationDetailView(DetailView):
    model = models.Localisation

    def render_to_response(self, context, **kw):
        return JsonResponse(self.object.json())


class LocalDetailView(DetailView):
    model = models.Local

    def render_to_response(self, context, **kw):
        return JsonResponse(self.object.json())


class EnergieDetailView(DetailView):
    model = models.Energie

    def render_to_response(self, context, **kw):
        return JsonResponse(self.object.json())


class DebitEnergieDetailView(DetailView):
    model = models.DebitEnergie

    def render_to_response(self, context, **kw):
        return JsonResponse(self.object.json())


class ProduitDetailView(DetailView):
    model = models.Produit

    def render_to_response(self, context, **kw):
        return JsonResponse(self.object.json())


class MetierDetailView(DetailView):
    model = models.Metier

    def render_to_response(self, context, **kw):
        return JsonResponse(self.object.json())


class ApprovisionnementMatierePremiereDetailView(DetailView):
    model = models.ApprovisionnementMatierePremiere

    def render_to_response(self, context, **kw):
        return JsonResponse(self.object.json())


class RessourceHumaineDetailView(DetailView):
    model = models.RessourceHumaine

    def render_to_response(self, context, **kw):
        return JsonResponse(self.object.json())


class FabricationDetailView(DetailView):
    model = models.Fabrication

    def render_to_response(self, context, **kw):
        return JsonResponse(self.object.json())


class MachineDetailView(DetailView):
    model = models.Machine

    def render_to_response(self, context, **kw):
        return JsonResponse(self.object.json())


class MatierePremiereDetailView(DetailView):
    model = models.MatierePremiere

    def render_to_response(self, context, **kw):
        return JsonResponse(self.object.json())
