from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flowers/', views.FlowerList.as_view(), name='flower_list'),
    path('flowers/<int:pk>/', views.FlowerDetail.as_view(), name='flower_detail'),
    path('flowers/create/', views.FlowerCreate.as_view(), name='flower_create'),
    path('flowers/<int:pk>/update/', views.FlowerUpdate.as_view(), name='flower_update'),
    path('flowers/<int:pk>/delete/', views.FlowerDelete.as_view(), name='flower_delete'),
    path('flowers/<int:flower_id>/add_watering', views.add_watering, name='add_watering'),

    path('accounts/signup/', views.signup, name='signup'),

    path('pollinators/', views.PollinatorList.as_view(), name='pollinator_list'),
    path('pollinators/<int:pk>/', views.PollinatorDetail.as_view(), name='pollinator_detail'),
    path('pollinators/create', views.PollinatorCreate.as_view(), name='pollinator_create'),
]