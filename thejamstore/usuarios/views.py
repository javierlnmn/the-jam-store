from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from usuarios.forms import RegistrationForm


def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        
        pagina_previa = request.META.get('HTTP_REFERER')
        
        if user != None:
            login(request, user)
            return HttpResponseRedirect(pagina_previa)
        else:
            messages.error(request, 'Los datos son incorrectos. Inténtelo con otros distintos.')
            return HttpResponseRedirect(pagina_previa)
        
def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión.')
    request.user = None
    
    pagina_previa = request.META.get('HTTP_REFERER')
    
    return HttpResponseRedirect(pagina_previa)

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        pagina_previa = request.META.get('HTTP_REFERER')
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return HttpResponseRedirect(pagina_previa)
        else:
            messages.error(request, 'Se produjo un error en el registro. Inténtelo de nuevo.')
            return HttpResponseRedirect(pagina_previa)