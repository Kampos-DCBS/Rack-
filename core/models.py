from django.db import models


# 📦 SALA (Rack físico onde ficam os devices)
class Sala(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# 💻 DEVICE (Notebook)
class Device(models.Model):
    nome = models.CharField(max_length=100)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='devices')
    carregando = models.BooleanField(default=False)
    presente = models.BooleanField(default=True)  # Está no rack ou não

    def __str__(self):
        return self.nome


# 👤 USUÁRIO (quem usa o device)
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome


# 🔄 MOVIMENTAÇÃO (log de uso dos devices)
class Movimentacao(models.Model):
    TIPOS = (
        ('retirada', 'Retirada'),
        ('devolucao', 'Devolução'),
    )

    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='movimentacoes')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.nome} - {self.tipo} - {self.data.strftime('%d/%m/%Y %H:%M')}"