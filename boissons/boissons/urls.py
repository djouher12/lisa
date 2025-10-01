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

from django.contrib import admin
from django.urls import path
from high_level import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "localisation/<int:pk>",
        views.LocalisationDetailView.as_view(),
        name="localisation",
    ),
    path(
        "local/<int:pk>",
        views.LocalDetailView.as_view(),
        name="local",
    ),
    path(
        "energie/<int:pk>",
        views.EnergieDetailView.as_view(),
        name="energie",
    ),
    path(
        "debitEnergie/<int:pk>",
        views.DebitEnergieDetailView.as_view(),
        name="debitenergie",
    ),
    path(
        "produitdetail/<int:pk>",
        views.ProduitDetailView.as_view(),
        name="produit",
    ),
    path(
        "metier/<int:pk>",
        views.MetierDetailView.as_view(),
        name="metier",
    ),
    path(
        "approvisionnementMatierePremiere/<int:pk>",
        views.ApprovisionnementMatierePremiereDetailView.as_view(),
        name="approvisionnementmatierepremiere",
    ),
    path(
        "ressourceHumaine/<int:pk>",
        views.RessourceHumaineDetailView.as_view(),
        name="ressourceHumaine",
    ),
    path(
        "fabrication/<int:pk>",
        views.FabricationDetailView.as_view(),
        name="fabrication",
    ),
    path(
        "machine/<int:pk>",
        views.MachineDetailView.as_view(),
        name="machine",
    ),
    path(
        "matierePremiere/<int:pk>",
        views.MatierePremiereDetailView.as_view(),
        name="matierepremiere",
    ),
]
