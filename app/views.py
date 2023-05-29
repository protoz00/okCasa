from unittest import skip
from urllib import response
import requests
from django.http import JsonResponse
from django.db.models import Sum,Count
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required, permission_required,user_passes_test
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from .forms import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SolicitudSerializer
from .models import Solicitud

# Create your views here.
@receiver(post_save, sender=User) 
def create_user_profile(sender, instance, created, **kwargs):     
    if created:
        instance.groups.add(Group.objects.get(name='cliente'))
       
def must_be_supervisor(user):
    return user.groups.filter(name='empleado').count()

def must_be_client(user):
    return user.groups.filter(name='cliente').count()

def login_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index.html') 
            else:
                messages.error(request, 'Credenciales inválidas. Por favor, intenta nuevamente.')
    else:
        form = UsuarioForm()
    
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
        logout(request)
        return redirect('login')


def inicio(request):
    current_user = request.user
    userid=current_user.id
    datos ={
        'userid':userid,
        'current_user':current_user
    }
        
    return render(request,'index.html',datos)

def placa(request):
    return render(request,'patron.html')

def must_be_supervisor(user):
    return user.groups.filter(name='admin').count()

def registro(request):
    datos = {
        'form' : FormularioUserRegistro()
    }
    if request.method == 'POST':
        formulario = FormularioUserRegistro(data=request.POST)
        if formulario.is_valid():

            formulario.save()
            messages.success(request,'Registrado correctamente!',extra_tags='bien')
            return redirect('index')
        datos["form"] = formulario
    else:
        messages.error(request,'Usuario no registrado',extra_tags='mal')
    return render(request, 'registration/registro.html', datos)

@login_required
def sol_informe(request):

    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        
        if form.is_valid():
            print("si")
            form.save()
            messages.success(request,'Solicitud registrada correctamente!')
            return redirect('index')
    else:
        form= SolicitudForm()
        print (form.errors)
        messages.error(request,'Solicitud no ha podido ser registrada ')
    return render(request,'sol_informe.html',{'form':form})


@login_required
@user_passes_test(must_be_client)
def usuariopag(request):
    current_user=request.user
    solicitudes=Solicitud.objects.filter()
    return render(request, 'usuario.html')

@login_required
def lista_view(request): 
        return render(request,'lista.html')


@login_required
@api_view(['GET'])
def solicitud_list(request):
    usuario = request.GET.get('usuario', None)  # Obtiene el valor del parámetro 'usuario' de la URL

    if usuario is not None:
        solicitudes = Solicitud.objects.filter(usuario=usuario)
    else:
        solicitudes = Solicitud.objects.all()

    serializer = SolicitudSerializer(solicitudes, many=True)
    return Response(serializer.data)