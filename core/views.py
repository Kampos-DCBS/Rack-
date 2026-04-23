from django.contrib.auth.decorators import login_required
from .models import Rack, Sala, Device, Usuario, Movimentacao
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout


# 📊 DASHBOARD
@login_required
def dashboard(request):
    total_salas = Sala.objects.count()
    total_devices = Device.objects.count()
    ok = Device.objects.filter(carregando=True).count()
    erro = Device.objects.filter(carregando=False).count()

    return render(request, 'dashboard.html', {
        'total_salas': total_salas,
        'total_devices': total_devices,
        'ok': ok,
        'erro': erro
    })


# 👤 USUÁRIOS
@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})


# 🔄 MOVIMENTAÇÕES
@login_required
def lista_movimentacoes(request):
    mov = Movimentacao.objects.select_related('device', 'usuario').order_by('-data')
    return render(request, 'movimentacoes.html', {'mov': mov})


# 🔐 LOGIN
def login_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso.")
            return redirect('homepage')
        else:
            messages.error(request, "Usuario ou senha invalidos.")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "Sessao encerrada com sucesso.")
    return redirect('login')


# 🏠 HOMEPAGE (SALAS)
@login_required
def lista_salas(request):
    busca = request.GET.get('q')

    salas = Sala.objects.all()

    if busca:
        salas = salas.filter(nome__icontains=busca)

    return render(request, 'homepage.html', {
        'salas': salas
    })


# 🗂️ RACKS DE UMA SALA
@login_required
def lista_racks(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    busca = request.GET.get('q')

    racks = sala.racks.all()

    if busca:
        racks = racks.filter(nome__icontains=busca)

    for rack in racks:
        rack.tem_erro = rack.devices.filter(carregando=False).exists()

    return render(request, 'racks.html', {
        'sala': sala,
        'racks': racks
    })


# 💻 DEVICES DE UM RACK
@login_required
def lista_devices(request, rack_id):
    rack = get_object_or_404(Rack, id=rack_id)
    busca = request.GET.get('q')

    devices = rack.devices.all()

    if busca:
        devices = devices.filter(nome__icontains=busca)

    return render(request, 'devices.html', {
        'rack': rack,
        'devices': devices
    })


@login_required
def detalhe_device(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    auditoria = device.movimentacoes.select_related('usuario').order_by('-data')[:8]

    return render(request, 'device_detail.html', {
        'device': device,
        'rack': device.rack,
        'auditoria': auditoria,
    })


@login_required
def criar_sala(request):
    if request.method != "POST":
        messages.error(request, "Metodo de requisicao invalido.")
        return redirect('homepage')

    nome = (request.POST.get("nome") or "").strip()
    professor = (request.POST.get("professor") or "").strip()

    if not nome:
        messages.error(request, "Informe o nome da sala.")
        return redirect('homepage')

    Sala.objects.create(
        nome=nome,
        professor=professor or "Nao informado"
    )
    messages.success(request, "Sala criada com sucesso.")
    return redirect('homepage')


@login_required
def criar_rack(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)

    if request.method != "POST":
        messages.error(request, "Metodo de requisicao invalido.")
        return redirect('racks', sala_id=sala.id)

    nome = (request.POST.get("nome") or "").strip()

    if not nome:
        messages.error(request, "Informe o nome do rack.")
        return redirect('racks', sala_id=sala.id)

    Rack.objects.create(
        nome=nome,
        sala=sala
    )
    messages.success(request, "Rack criado com sucesso.")
    return redirect('racks', sala_id=sala.id)

@login_required
def criar_device(request, rack_id):
    rack = get_object_or_404(Rack, id=rack_id)

    if request.method != "POST":
        messages.error(request, "Metodo de requisicao invalido.")
        return redirect('devices', rack_id=rack.id)

    nome = (request.POST.get("nome") or "").strip()
    processador = (request.POST.get("processador") or "").strip()
    memoria_ram = (request.POST.get("memoria_ram") or "").strip() or "Nao informado"
    placa_video = (request.POST.get("placa_video") or "").strip() or "Nao informado"
    duracao_media_bateria = (request.POST.get("duracao_media_bateria") or "").strip() or "Nao informado"
    status_descricao = (request.POST.get("status_descricao") or "").strip() or "No lugar certo e carregando"

    if not nome or not processador:
        messages.error(request, "Nome e processador sao obrigatorios.")
        return redirect('devices', rack_id=rack.id)

    try:
        bateria_percentual = int(request.POST.get("bateria_percentual") or 100)
        total = int(request.POST.get("armazenamento_total") or 0)
        usado = int(request.POST.get("armazenamento_usado") or 0)
    except (TypeError, ValueError):
        messages.error(request, "Informe apenas numeros validos para bateria e armazenamento.")
        return redirect('devices', rack_id=rack.id)

    if total <= 0:
        messages.error(request, "O armazenamento total deve ser maior que zero.")
        return redirect('devices', rack_id=rack.id)

    if usado < 0:
        messages.error(request, "O armazenamento usado nao pode ser negativo.")
        return redirect('devices', rack_id=rack.id)

    bateria_percentual = max(0, min(bateria_percentual, 100))
    usado = max(0, min(usado, total))

    Device.objects.create(
        nome=nome,
        processador=processador,
        memoria_ram=memoria_ram,
        placa_video=placa_video,
        bateria_percentual=bateria_percentual,
        duracao_media_bateria=duracao_media_bateria,
        status_descricao=status_descricao,
        armazenamento_total=total,
        armazenamento_usado=usado,
        rack=rack
    )
    messages.success(request, "Device criado com sucesso.")
    return redirect('devices', rack_id=rack.id)

def erro_404(request, exception):
    return render(request, '404.html', status=404)

def erro_500(request):
    return render(request, '404.html', status=500)
