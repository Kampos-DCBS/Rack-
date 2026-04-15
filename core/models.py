from django.db import models

class Device(models.Model):
    nome = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    posicao = models.IntegerField()

    def __str__(self):
        return self.nome


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Movimentacao(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)