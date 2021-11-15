from django.db import models


class Hotel(models.Model):

    name = models.CharField(max_length=100)


    def __str__(self):

        return self.name


class Huesped(models.Model):

    name = models.CharField(max_length=100)
    direccion = models.TextField()
    correo = models.TextField()
    telefono = models.TextField()
    Hotel = models.ForeignKey(

        Hotel, related_name="Huesped", on_delete=models.CASCADE

    )


    def __str__(self):

        return self.name

# Create your models here.
