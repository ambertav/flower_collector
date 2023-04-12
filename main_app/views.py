from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Flower

# Create your views here.

def home (request) :
    return render(request, 'home.html')

def signup (request) :
    # handling POST request
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid () :
            user = form.save()
            login(request, user)
            return redirect('flower_list')
        
    # handling GET request
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })


class FlowerList (LoginRequiredMixin, ListView) :
    template_name = 'flowers/flower_list.html'

    def get_queryset (self) :
        return Flower.objects.filter(user=self.request.user)

class FlowerDetail (LoginRequiredMixin, DetailView) :
    template_name = 'flowers/flower_detail.html'

    def get_queryset (self) :
        return Flower.objects.filter(user=self.request.user)

class FlowerCreate (LoginRequiredMixin, CreateView) :
    model = Flower
    fields = ('name', 'color', 'description', 'stage')
    template_name = 'flowers/flower_form.html'

    def form_valid (self, form) :
       form.instance.user = self.request.user
       return super().form_valid(form)

class FlowerUpdate (LoginRequiredMixin, UpdateView) :
    fields = ('name', 'color', 'description', 'stage')
    template_name = 'flowers/flower_form.html'

    def get_queryset (self) :
        return Flower.objects.filter(user=self.request.user)

class FlowerDelete (LoginRequiredMixin, DeleteView) :
    success_url = '/flowers/'
    template_name = 'flowers/flower_confirm_delete.html'

    def get_queryset (self) :
        return Flower.objects.filter(user=self.request.user)