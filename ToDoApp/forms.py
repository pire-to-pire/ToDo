from django.forms import ModelForm

from ToDoApp.models import ToDo


class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = "__all__"
