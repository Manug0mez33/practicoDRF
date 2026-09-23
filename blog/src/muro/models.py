from django.db import models

class Comentario(models.Model):
    contenido = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contenido

class Post(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField(max_length=500)
    comentarios = models.ForeignKey(Comentario, on_delete=models.CASCADE, related_name='comentarios', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

