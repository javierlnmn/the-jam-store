from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.urls import resolve
from .forms import RegistrarUsuarioForm, ActualizarUsuarioForm, DireccionForm
from .models import Comentario, Producto, Producto_Talla, Lista_Deseos, Carrito, Carrito_Productos, Direccion, Talla, PROVINCIAS_CHOICES
from urllib.parse import urlparse
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


directorio_templates = 'usuarios'

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        pagina_previa = request.META.get('HTTP_REFERER')
        if form.is_valid():
            form.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return HttpResponseRedirect(pagina_previa)
        else:
            messages.error(request, 'Se produjo un error en el registro. Inténtelo de nuevo.')
            return HttpResponseRedirect(pagina_previa)
    else:
        return HttpResponseNotFound('Error 404')

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
    else:
        return HttpResponseNotFound('Error 404')

@login_required  
def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión.')
    request.user = None
    
    pagina_previa = request.META.get('HTTP_REFERER')
    parsed_url = urlparse(pagina_previa)
    url_pagina_previa = parsed_url.path
    return redirect('general:indice')
    
@login_required
def actualizar_datos_usuario(request):
    user = request.user 
    if request.method == 'POST':
        form = ActualizarUsuarioForm(request.POST, request.FILES, instance=user)
        pagina_previa = request.META.get('HTTP_REFERER')
        if form.is_valid():
            form.save()
            messages.success(request, '¡Has actualizado los datos de tu perfil!')
            return HttpResponseRedirect(pagina_previa)
        else:
            messages.error(request, 'Se produjo un error al actualizar los datos. Inténtelo de nuevo.')
            return HttpResponseRedirect(pagina_previa)
    else:
        return HttpResponseNotFound('Error 404')

@login_required
def valorar_producto(request, id_producto):
    if request.method == 'POST':
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
        return HttpResponseNotFound('Error 404')


def lista_deseos(request):
    if not request.user.is_authenticated:
        messages.success(request, '¡Inicia sesión para crear tu lista de deseos!')
        pagina_previa = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(pagina_previa)
    
    # get_or_create devuelve una tupla con dos valores, el object y un booleano diciendo si existia antes o no
    lista_deseos, _ = Lista_Deseos.objects.get_or_create(usuario=request.user)
    productos_lista_deseos = lista_deseos.producto.all()
    
    paginacion = Paginator(productos_lista_deseos, 5)
    pagina = request.GET.get("pag")
    productos_por_pagina = paginacion.get_page(pagina)

    contexto = {
        "productos": productos_por_pagina,
    }

    return render(request, directorio_templates + "/lista-deseos.html", contexto)

    
def anadir_a_lista_deseos(request, id_producto):
    if not request.user.is_authenticated:
        messages.success(request, '¡Inicia sesión para crear tu lista de deseos!')
        return redirect('productos:producto_detalle', id_producto=id_producto)

    producto = Producto.objects.get(pk=id_producto)
    lista_deseos, _ = Lista_Deseos.objects.get_or_create(usuario=request.user)
    lista_deseos.producto.add(producto)
    
    return redirect('productos:producto_detalle', id_producto=id_producto)

@login_required
def quitar_de_lista_deseos(request, id_producto):
    producto = Producto.objects.get(pk=id_producto)
    lista_deseos, _ = Lista_Deseos.objects.get_or_create(usuario=request.user)
    lista_deseos.producto.remove(producto)
    pagina_previa = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(pagina_previa)


def carrito(request):
    if not request.user.is_authenticated:
        messages.success(request, '¡Inicia sesión para crear tu carrito!')
        pagina_previa = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(pagina_previa)
    
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    productos_carrito = carrito.producto.all()

    contexto = {
        "productos": productos_carrito,
    }

    return render(request, directorio_templates + "/lista-deseos.html", contexto)

def anadir_a_carrito(request, id_producto):
    if not request.user.is_authenticated:
        messages.success(request, '¡Inicia sesión para añadir productos a tu carrito!')
        return redirect('productos:producto_detalle', id_producto=id_producto)

    formulario_talla = int(request.GET.get('talla')) # El id de la talla que obtenemos es el de la relación producto_talla
    talla_producto = Producto_Talla.objects.get(pk=formulario_talla)
    talla = Talla.objects.get(pk=talla_producto.talla_id)
    cantidad = request.GET.get('cantidad') # Lo mismo para cantidad

    producto = Producto.objects.get(pk=id_producto)
    
    carrito, _ =   Carrito.objects.get_or_create(usuario=request.user)
    
    carrito_productos = Carrito_Productos.objects.create(producto_id=id_producto, carrito_id=carrito.id, talla=talla, cantidad=cantidad)
    carrito_productos.save()
    
    messages.success(request, '¡Has añadido '+ producto.nombre +' a tu carrito!')
    return redirect('productos:producto_detalle', id_producto=id_producto)

@login_required
def quitar_de_carrito(request, id_producto):
    # producto = Producto.objects.get(pk=id_producto)
    # lista_deseos, _ = Lista_Deseos.objects.get_or_create(usuario=request.user)
    # lista_deseos.producto.remove(producto)
    # pagina_previa = request.META.get('HTTP_REFERER')
    # return HttpResponseRedirect(pagina_previa)
    pass



@login_required
def ver_direcciones(request):
    user = request.user
    direcciones = Direccion.objects.filter(usuario=user)
    
    paginacion = Paginator(direcciones, 5)
    pagina = request.GET.get("pag")
    direcciones_por_pagina = paginacion.get_page(pagina)
    
    contexto = {
        'direcciones': direcciones_por_pagina
    }
    
    return render(request, directorio_templates + "/direcciones.html", contexto)

@login_required
def formulario_crear_direccion(request):
    contexto = {
        'provincias': PROVINCIAS_CHOICES
    }
    return render(request, directorio_templates + "/formulario-crear-direccion.html", contexto)


@login_required
def anadir_direccion(request):
    if request.method == 'POST':
        form = DireccionForm(request.POST)
        if form.is_valid():
            direccion = form.save(commit=False)
            direccion.usuario = request.user
            direccion.save()
            messages.success(request, '¡Dirección añadida con éxito!')
            return redirect('usuarios:ver_direcciones')
        else:
            messages.error(request, 'Se produjo un error al añadir la dirección. Inténtelo de nuevo.')
            return redirect('usuarios:ver_direcciones')
    else:
        return HttpResponseNotFound('Error 404')
    
@login_required
def eliminar_direccion(request, id_direccion):
    direccion = Direccion.objects.get(pk=id_direccion)
    direccion.delete()
    messages.success(request, 'Dirección eliminada.')
    return redirect('usuarios:ver_direcciones')

@login_required
def formulario_editar_direccion(request, id_direccion):
    direccion = Direccion.objects.get(pk=id_direccion)
    contexto = {
        'provincias': PROVINCIAS_CHOICES,
        'direccion': direccion
    }
    return render(request, directorio_templates + "/formulario-editar-direccion.html", contexto)

@login_required
def editar_direccion(request, id_direccion):
    direccion = Direccion.objects.get(pk=id_direccion)
    if request.method == 'POST':
        form = DireccionForm(request.POST, instance=direccion)
        if form.is_valid():
            direccion = form.save(commit=True)
            messages.success(request, '¡Dirección actualizada con éxito!')
            return redirect('usuarios:ver_direcciones')
        else:
            messages.error(request, 'Se produjo un error al añadir la dirección. Inténtelo de nuevo.')
            return redirect('usuarios:ver_direcciones')
    else:
        return HttpResponseNotFound('Error 404')
    

class CustomRestablecerContrasenaFormularioView(PasswordResetView):
    template_name = directorio_templates + '/restablecer-contrasena/formulario_restablecer_contrasena.html'
    email_template_name = directorio_templates + '/restablecer-contrasena/correo_restablecer_contrasena.html'
    asunto_correo = directorio_templates + '/restablecer-contrasena/asunto_correo.txt'
    success_url = '/usuarios/restablecer-contrasena/correo-enviado/'

class CustomRestablecerContrasenaCorreoEnviadoView(PasswordResetDoneView):
    template_name = directorio_templates + '/restablecer-contrasena/correo_restablecer_contrasena_enviado.html'

class CustomRestablecerContrasenaView(PasswordResetConfirmView):
    template_name = directorio_templates + '/restablecer-contrasena/restablecer_contrasena.html'
    success_url = '/usuarios/restablecer-contrasena/completado/'

class CustomRestablecerContrasenaCompletadoView(PasswordResetCompleteView):
    template_name = directorio_templates + '/restablecer-contrasena/completado.html'