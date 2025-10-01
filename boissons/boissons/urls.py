"""
URL configuration for boissons project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import models


urlpatterns = [
    path(
        "",
        models.views.LocalisationDetailView.as_view(),
        name=models.Localisation,
    ),
    path(
        "",
        models.views.LocalDetailView.as_view(),
        name=models.Local,
    ),
    path(
        "",
        models.views.EnergieDetailView.as_view(),
        name=models.Energie,
    ),
    path(
        "",
        models.views.DebitEnergieDetailView.as_view(),
        name=models.DebitEnergie,
    ),
    path(
        "",
        models.views.ProduitDetailView.as_view(),
        name=models.Produit,
    ),
    path(
        "",
        models.views.MetierDetailView.as_view(),
        name=models.Metier,
    ),
    path(
        "",
        models.views.ApprovisionnementMatierePremiereDetailView.as_view(),
        name=models.ApprovisionnementMatierePremiere,
    ),
    path(
        "",
        models.views.RessourceHumaineDetailView.as_view(),
        name=models.RessourceHumaine,
    ),
    path(
        "",
        models.views.FabricationDetailView.as_view(),
        name=models.Fabrication,
    ),
    path(
        "",
        models.views.MachineDetailView.as_view(),
        name=models.Machine,
    ),
    path(
        "",
        models.views.MatierePremiereDetailView.as_view(),
        name=models.MatierePremiere,
    ),
]
