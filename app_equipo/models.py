from django.db import models

class Equipo(models.Model):
    # Django automáticamente crea el campo 'id' (id_equipo)
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    fecha_fundacion = models.DateField()
    entrenador = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    color_uniforme = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} ({self.siglas}) - Ciudad: {self.ciudad}'