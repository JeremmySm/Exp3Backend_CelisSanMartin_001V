from django.db import models

# Create your models here.

#Modelo para usuario

class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True, verbose_name='Id de usuario')
    nombreusuario = models.CharField(max_length=16, verbose_name='Nombre de usuario')
    contrausuario = models.CharField(max_length=12,verbose_name='Password')

    def __int__(self):

        return self.idusuario


class Usuariomoroso(models.Model):
    idmoroso = models.IntegerField(primary_key=True, verbose_name='Id de moroso')
    nombremoroso = models.CharField(max_length=16, verbose_name='Nombre de moroso')
    mesesmoroso = models.CharField(max_length=100, verbose_name='meses de morosidad')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __int__(self):

        return self.idmoroso

class Servicio(models.Model):
    idservicio = models.IntegerField(primary_key=True, verbose_name='Id de servicio')
    nomservicio = models.CharField(max_length=100, verbose_name='Nombre de servicio')
    valorservicio = models.CharField(max_length=100, verbose_name='valor servicio por hora')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __int__(self):

        return self.idservicio




