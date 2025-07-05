from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación del registro
    firstName = models.CharField(max_length=100)  # Nombre del registro
    lastName = models.CharField(max_length=100)  # Apellido del registro
    email = models.EmailField(max_length=100)  # Correo electrónico del registro
    phone = models.CharField(max_length=15)  # Teléfono del registro
    address = models.CharField(max_length=100)  # Dirección del registro
    city = models.CharField(max_length=50)  # Ciudad del registro
    state = models.CharField(max_length=50)  # Estado del registro
    zip_code = models.CharField(max_length=20)  # Código postal del registro
    
    def __str__ (self):
        return (f"{self.firstName} {self.lastName}")
    