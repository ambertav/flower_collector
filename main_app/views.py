from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Flower, Pollinator
from .forms import WateringForm

# Create your views here.

# view functions
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

def add_watering (request, flower_id) :
    form = WateringForm(request.POST)
    if form.is_valid () :
        new_watering = form.save(commit=False)
        new_watering.flower_id = flower_id
        new_watering.save()
    return redirect('flower_detail', pk=flower_id)

def assoc_flower (request, pollinator_id, flower_id) :
    if Flower.objects.get(id=flower_id).stage == 'P' :
        pollinator = Pollinator.objects.get(id=pollinator_id)
        pollinator.flowers.add(flower_id)
        return redirect('pollinator_detail', pollinator_id=pollinator_id)


def unassoc_flower (request, pollinator_id, flower_id) :
    pollinator = Pollinator.objects.get(id=pollinator_id)
    pollinator.flowers.remove(flower_id)
    return redirect('pollinator_detail', pollinator_id=pollinator_id)

# CBV for Flower
class FlowerList (LoginRequiredMixin, ListView) :
    template_name = 'flowers/flower_list.html'

    def get_queryset (self) :
        return Flower.objects.filter(user=self.request.user)

class FlowerDetail (LoginRequiredMixin, ModelFormMixin, DetailView) :
    template_name = 'flowers/flower_detail.html'
    form_class = WateringForm

    def get_queryset (self) :
        return Flower.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super(FlowerDetail, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

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
    

# CBV for Pollinator
class PollinatorList (LoginRequiredMixin, ListView) :
    template_name = 'pollinators/pollinator_list.html'

    def get_queryset (self) :
        return Pollinator.objects.filter(user=self.request.user)

# class PollinatorDetail (LoginRequiredMixin, DetailView) :
#     template_name = 'pollinators/pollinator_detail.html'

#     def get_queryset (self) :
#         return Pollinator.objects.filter(user=self.request.user)
    
#     def get_context_data(self, **kwargs):
#         context = super(PollinatorDetail, self).get_context_data(**kwargs)
#         context['flowers'] = Flower.objects.all()
#         return context

@login_required
def pollinator_detail (request, pollinator_id) :
    pollinator = Pollinator.objects.get(id=pollinator_id)
    pollinated_flower_ids = pollinator.flowers.all().values_list('id')
    available_flowers = Flower.objects.exclude(id__in=pollinated_flower_ids)

    return render(request, 'pollinators/pollinator_detail.html', {
        'pollinator': pollinator,
        'flowers': available_flowers
    })
    
class PollinatorCreate (LoginRequiredMixin, CreateView) :
    model = Pollinator
    fields = ('name', 'description', 'type')
    template_name = 'pollinators/pollinator_form.html'

    def form_valid (self, form) :
        form.instance.user = self.request.user
        return super().form_valid(form)

class PollinatorUpdate (LoginRequiredMixin, UpdateView) :
    fields = ('name', 'description', 'type')
    template_name = 'pollinators/pollinator_form.html'

    def get_queryset (self) :
        return Pollinator.objects.filter(user=self.request.user)

class PollinatorDelete (LoginRequiredMixin, DeleteView) :
    success_url = '/pollinators/'
    template_name = 'pollinators/pollinator_confirm_delete.html'

    def get_queryset (self) :
        return Pollinator.objects.filter(user=self.request.user)