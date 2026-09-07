from django.db import models

class Muro(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    