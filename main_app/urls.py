from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flowers/', views.FlowerList.as_view(), name='flower_list'),
    path('flowers/<int:pk>', views.FlowerDetail.as_view(), name='flower_detail'),
    path('flowers/create/', views.FlowerCreate.as_view(), name='flower_create'),
    path('flowers/<int:pk>/update/', views.FlowerUpdate.as_view(), name='flower_update'),
]