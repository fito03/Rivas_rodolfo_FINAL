from django.db import models

# Create your models here.

class Instituciones(models.Model):
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

class Inscritos(models.Model):

    estado_inscrito = (
        ('RESERVADO', 'RESERVADO'),
        ('COMPLETADA', 'COMPLETADA'),
        ('ANULADA', 'ANULADA'),
        ('NO ASISTENTE', 'NO ASISTENTE')
    )

    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_inscripcion = models.DateField(auto_now_add=True)
    hora_inscripcion = models.TimeField(auto_now_add=True)
    institucion = models.ForeignKey(Instituciones, on_delete=models.PROTECT)
    estado = models.CharField(max_length=50, choices=estado_inscrito)
    observacion = models.CharField(max_length=50, blank=True, null=True)