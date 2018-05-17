from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from newapp.models import Produs

class Index(TemplateView):
    template_name = "base.html"

class ListaProduse(ListView):
    template_name = "newapp/produse_list.html"
    queryset = Produs.objects.all()

