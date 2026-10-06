from django.db import models

class Estado(models.Model):
    estado = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.estado

class Ubicacion(models.Model):
    ubicacion = models.CharField(max_length=50)
    detalles = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
        return self.ubicacion

class Inventario(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


