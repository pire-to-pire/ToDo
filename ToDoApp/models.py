from django.db import models


# Create your models here.

class ToDo(models.Model):
    contenu = models.TextField()
    valide = models.BooleanField(default=False)
    #favori = models.BooleanField(default=False)

    def __str__(self):
        nom = self.contenu
        if self.valide:
            nom = "[✔] " + nom
        else:
            nom = "[X] " + nom
        return nom
