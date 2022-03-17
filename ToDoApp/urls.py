from django.urls import path
from ToDoApp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('fait/', views.add, name="fait"),
    path('non_fait/', views.add, name="non_fait"),
]
