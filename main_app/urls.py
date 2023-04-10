from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flowers/', views.FlowerList.as_view(), name='flower_list'),
    path('flowers/create/', views.FlowerCreate.as_view(), name='flower_create')
]