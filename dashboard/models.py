from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORIA = (
    ('Herramienta', 'Herramienta'),
    ('Material', 'Material'),
    ('Tornillos', 'Tornillos'),
    ('Tuercas', 'Tuercas'),
    ('Mangeras', 'Mangueras'),
)

class Productos(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA, null=True)
    cantidad = models.PositiveBigIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'{self.nombre} {self.cantidad}'

class Ordenes(models.Model):
    producto= models.ForeignKey(Productos, on_delete= models.CASCADE, null=True)
    staff = models.ForeignKey(User,models.CASCADE, null=True)
    orden_cantidad = models.PositiveIntegerField(null= True)
    dia = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Ordenes'

    def __str__(self):
        return f'{self.producto} orden por {self.staff.username}'
    
