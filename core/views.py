from django.contrib.auth.decorators import login_required
from .models import Rack, Sala, Device, Usuario, Movimentacao
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def criar_algo(request):
    if request.method == "POST":
        messages.success(request, "Salvo com sucesso!")
        return redirect('alguma_pagina')

    return render(request, 'pagina.html')


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
    mov = Movimentacao.objects.all()
    return render(request, 'movimentacoes.html', {'mov': mov})


# 🔐 LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')  # 👈 melhor ir direto pra homepage
        else:
            messages.error(request, "Usuário ou senha inválidos")

    return render(request, 'login.html')


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
    sala = Sala.objects.get(id=sala_id)
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
    rack = Rack.objects.get(id=rack_id)
    busca = request.GET.get('q')

    devices = rack.devices.all()

    if busca:
        devices = devices.filter(nome__icontains=busca)

    return render(request, 'devices.html', {
        'rack': rack,
        'devices': devices
    })

def erro_404(request, exception):
    return render(request, '404.html', status=404)

def erro_500(request):
    return render(request, '404.html', status=500)