from django.urls import path
from ToDoApp import views


urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add")
]