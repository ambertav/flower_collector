from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Flower

# Create your views here.

def home(request):
    return render(request, 'home.html')

class FlowerList (ListView) :
    model = Flower
    template_name = 'flowers/flower_list.html'

class FlowerDetail (DetailView) :
    model = Flower
    template_name = 'flowers/flower_detail.html'

class FlowerCreate (CreateView) :
    model = Flower
    fields = '__all__'
    template_name = 'flowers/flower_form.html'

class FlowerUpdate (UpdateView) :
    model = Flower
    fields = '__all__'
    template_name = 'flowers/flower_form.html'