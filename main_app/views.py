from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Flower

# Create your views here.

def home(request):
    return render(request, 'home.html')

class FlowerList (ListView) :
    model = Flower
    template_name = 'flowers/flower_list.html'

class FlowerCreate (CreateView) :
    model = Flower
    fields = '__all__'
    template_name = 'flowers/flower_form.html'