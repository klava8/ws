from django.shortcuts import render
from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


class FishListView(ListView):
    model = Product
    fields = '__all__'
    context_object_name = 'fishes'
    template_name = 'list.html'

class FishDetailView(DetailView):
    model = Product
    fields = '__all__'
    template_name = 'detail.html'
    context_object_name = 'fish'