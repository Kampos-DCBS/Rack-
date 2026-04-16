from django.contrib.auth.decorators import login_required
from .models import Sala,Device, Usuario, Movimentacao
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def criar_algo(request):
    if request.method == "POST":
        
        messages.success(request, "Salvo com sucesso!")
        return redirect('alguma_pagina')

    return render(request, 'pagina.html')

@login_required
def dashboard(request):
    devices = Device.objects.all()
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


@login_required
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})


@login_required
def lista_movimentacoes(request):
    mov = Movimentacao.objects.all()
    return render(request, 'movimentacoes.html', {'mov': mov})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Usuário ou senha inválidos")

    return render(request, 'login.html')

@login_required
def lista_salas(request):
    salas = Sala.objects.all()
    return render(request, 'salas.html', {'salas': salas})


@login_required
def devices_sala(request, id):
    devices = Device.objects.filter(sala_id=id)
    return render(request, 'devices.html', {'devices': devices})