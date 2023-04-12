from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    fields = ('name', 'color', 'description', 'stage')
    template_name = 'flowers/flower_form.html'

    def form_valid (self, form) :
       form.instance.user = self.request.user
       return super().form_valid(form)

class FlowerUpdate (UpdateView) :
    model = Flower
    fields = ('name', 'color', 'description', 'stage')
    template_name = 'flowers/flower_form.html'

class FlowerDelete (DeleteView) :
    model = Flower
    success_url = '/flowers/'
    template_name = 'flowers/flower_confirm_delete.html'