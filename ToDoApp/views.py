from django.shortcuts import render, redirect

from . import forms
from . import models


# Create your views here.


def index(request):
    todos = models.ToDo.objects.all()
    return render(request, "ToDoApp/index.html", {"todos": todos})


def add(request):
    if request.method == "POST":
        form = forms.ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = forms.ToDoForm()
    return render(request, "ToDoApp/add.html", {"form": form})
