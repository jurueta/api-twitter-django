from django.db import models

# Create your models here.
class UserTwitter(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombres')
    last_name = models.CharField(max_length=100, verbose_name='Apellidos')
    email = models.EmailField(max_length=100, verbose_name='Correo', unique=True, null=True)
    phone = models.CharField(max_length=100, verbose_name='Telefono', null=True)
    username = models.CharField(max_length=100, verbose_name='Usuario', unique=True)
    password = models.CharField(max_length=200, verbose_name='Password')
    photo = models.ImageField(verbose_name="foto perfil", upload_to='images/', null=True)
    cover_photo = models.ImageField(verbose_name="foto portada", upload_to='images/', null=True)
    verified = models.SmallIntegerField(verbose_name="Verificado", default=0)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")

    def __str__(self):
        return f"{self.id} - {self.name} {self.last_name}"

class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre pais')
    iso_code = models.CharField(max_length=11, verbose_name='Codigo ISO')
    status = models.SmallIntegerField(verbose_name="Estado", default=1)

class Gender(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre genero')
    status = models.SmallIntegerField(verbose_name="Estado", default=1)

class Language(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre idioma')
    status = models.SmallIntegerField(verbose_name="Estado", default=1)

class AdditionalData(models.Model):
    country = models.ForeignKey(Country, verbose_name="pais_id", on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, verbose_name="genero_id", on_delete=models.CASCADE)
    language = models.ForeignKey(Language, verbose_name="idioma_id", on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name="edad")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")