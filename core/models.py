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
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE, related_name='devices')

    processador = models.CharField(max_length=100)
    memoria_ram = models.CharField(max_length=100, default='Nao informado')
    placa_video = models.CharField(max_length=120, default='Nao informado')
    bateria_percentual = models.PositiveIntegerField(default=100)
    duracao_media_bateria = models.CharField(max_length=100, default='Nao informado')
    status_descricao = models.CharField(
        max_length=200,
        default='No lugar certo e carregando'
    )

    armazenamento_total = models.IntegerField()
    armazenamento_usado = models.IntegerField()

    carregando = models.BooleanField(default=False)
    presente = models.BooleanField(default=True)

    @property
    def armazenamento_disponivel(self):
        return max(self.armazenamento_total - self.armazenamento_usado, 0)

    @property
    def armazenamento_percentual(self):
        if self.armazenamento_total <= 0:
            return 0

        percentual = (self.armazenamento_usado / self.armazenamento_total) * 100
        return max(0, min(round(percentual), 100))

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
