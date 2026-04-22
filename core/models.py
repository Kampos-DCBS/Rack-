from django.db import models


# 📦 SALA
class Sala(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# 🗄️ RACK
class Rack(models.Model):
    nome = models.CharField(max_length=100)
    sala = models.ForeignKey(
        Sala,
        on_delete=models.CASCADE,
        related_name='racks'
    )

    def __str__(self):
        return f"{self.nome} ({self.sala.nome})"


# 💻 DEVICE
class Device(models.Model):
    nome = models.CharField(max_length=100)

    rack = models.ForeignKey(
        Rack,
        on_delete=models.CASCADE,
        related_name='devices'
    )

    processador = models.CharField(max_length=100)

    armazenamento = models.CharField(
        max_length=100,
        default="Não informado"  # 👈 resolve problema de migration
    )

    carregando = models.BooleanField(default=False)
    presente = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nome} ({self.rack.nome})"


# 👤 USUÁRIO
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome


# 🔄 MOVIMENTAÇÃO
class Movimentacao(models.Model):
    TIPOS = (
        ('retirada', 'Retirada'),
        ('devolucao', 'Devolução'),
    )

    device = models.ForeignKey(
        Device,
        on_delete=models.CASCADE,
        related_name='movimentacoes'
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    tipo = models.CharField(max_length=20, choices=TIPOS)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.nome} - {self.tipo} - {self.data.strftime('%d/%m/%Y %H:%M')}"