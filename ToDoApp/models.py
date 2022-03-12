from django.db import models


# Create your models here.

class ToDo(models.Model):
    contenu = models.TextField()
    valide = models.BooleanField(default=False)

    def __str__(self):
        if self.valide:
            return f"[X] {self.contenu}"
        else:
            return f"[ ] {self.contenu}"
