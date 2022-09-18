from django.urls import path
import api.views as views

urlpatterns = [
    path('pet-list/', views.petList, name='pet-list'),
    path('pet-details/<str:pk>/', views.petDetails, name='pet-details'),
    path('pet-add/', views.addPet, name='pet-add'),
    path('pet-update/<str:pk>/', views.updatePet, name='pet-update'),
    path('pet-delete/<str:pk>/', views.deletePet, name='pet-delete'),
]