from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView
)
from .models import Client


class ClientListView(ListView):
    model = Client
    # template_name = 'clients/clients_client.html' # <app>/<model>_<viewtyoe>.html
    context_object_name = 'clients'
    ordering = ['client_id']
    paginate_by = 10

class ClientDetailView(DetailView):
    model = Client
    # context_object_name = 'client'
