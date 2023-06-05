from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .forms import RegistrationForm
from .models import Comentario, Producto, Lista_Deseos

directorio_templates = 'usuarios'


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
        
def valorar_producto(request, id_producto):
    if request.method == 'POST':
        if request.user.is_authenticated:
            pagina_previa = request.META.get('HTTP_REFERER')
            
            texto = request.POST.get('texto')
            valoracion = request.POST.get('valoracion')
            producto = Producto.objects.get(pk=id_producto)
            
            try:
                comentario = Comentario.objects.create(
                    comentario=texto,
                    valoracion=valoracion,
                    usuario=request.user,
                    producto=producto
                )
                
                comentario.save()
            except:
                messages.error(request, 'Ha habido un error al añadir la valoración. Inténtalo de nuevo.')
            
            return HttpResponseRedirect(pagina_previa)
        else:
            pagina_previa = request.META.get('HTTP_REFERER')
            messages.error(request, 'Para valorar un producto debes haber iniciado sesión.')
            return HttpResponseRedirect(pagina_previa)
    else:
        pass # 404    
    
def lista_deseos(request):

    # get_or_create devuelve una tupla con dos valores, el object y un booleano diciendo si existia antes o no
    lista_deseos, _ = Lista_Deseos.objects.get_or_create(usuario=request.user)
    productos_lista_deseos = lista_deseos.producto.all()

    contexto = {
        "productos": productos_lista_deseos,
    }

    return render(request, directorio_templates + "/lista-deseos.html", contexto)