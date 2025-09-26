from django.views.generic import DetailView, ListView
from .models import Boissons


class BoissonsListView(ListView):
    model = Boissons


class BoissonsDetailView(DetailView):
    model = Boissons
