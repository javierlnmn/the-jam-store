from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Pedido, Pedido_Producto
from usuarios.models import Custom_User, Direccion, Carrito

import stripe
from stripe.error import CardError

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

directorio_templates = 'pedidos'

@login_required
def pedidos(request):
    pedidos = Pedido.objects.filter(usuario_id = request.user.id)
    paginacion = Paginator(pedidos, 5)
    pagina = request.GET.get("pag")
    pedidos_por_pagina = paginacion.get_page(pagina)
    
    contexto = {
        'pedidos': pedidos_por_pagina
    }
    
    return render(request, directorio_templates + "/pedidos.html", contexto)

@login_required
def detalle_pedido(request, id_pedido):
    pedido = Pedido.objects.get(pk=id_pedido)
    contexto = {
        'pedido': pedido
    }
    
    return render(request, directorio_templates + "/detalle_pedido.html", contexto)

@login_required
def formulario_pago(request):
    id_direccion = request.GET.get('direccion')
    try:
        direccion = Direccion.objects.get(pk=id_direccion)
    except:
        pagina_previa = request.META.get('HTTP_REFERER')
        messages.error(request, 'Se produjo un error al realizar el pedido. Inténtelo de nuevo.')
        return HttpResponseRedirect(pagina_previa)
    
    carrito = Carrito.objects.get(usuario_id=request.user.id)
    productos_carrito_del_usuario = carrito.carrito_productos_set.all()

    precio_total = 0
    for producto_carrito in productos_carrito_del_usuario:
        if not producto_carrito.producto.oferta:
           precio_total += producto_carrito.producto.precio * producto_carrito.cantidad
        else:
           precio_total += producto_carrito.producto.precio_oferta * producto_carrito.cantidad
    
    contexto = {
        'direccion': direccion.id,
        'precio_total': precio_total
    }
    
    return render(request, directorio_templates + "/formulario_pago.html", contexto)

@login_required
def realizar_pedido(request, id_direccion):
    
    if request.method == 'POST':
        
        try:
            
            carrito = Carrito.objects.get(usuario_id=request.user.id)
            productos_carrito_del_usuario = carrito.carrito_productos_set.all()
            precio_total = 0
            for producto_carrito in productos_carrito_del_usuario:
                if not producto_carrito.producto.oferta:
                    precio_total += producto_carrito.producto.precio * producto_carrito.cantidad
                else:
                    precio_total += producto_carrito.producto.precio_oferta * producto_carrito.cantidad
                
            pedido = Pedido.objects.create(
                usuario_id = request.user.id,
                direccion_id = id_direccion,
                estado_id=1
            )

            stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
            
            cargo = stripe.Charge.create(
                amount=(int(float(precio_total) * 100)),
                currency='eur',
                source=request.POST['stripeToken'],
                description='Pago del pedido: {}'.format(pedido)
            )
            
            carrito = Carrito.objects.get(usuario_id=request.user.id)

            productos_carrito_del_usuario = carrito.carrito_productos_set.all()
            
            for producto_carrito in productos_carrito_del_usuario:
                Pedido_Producto.objects.create(
                    pedido=pedido, 
                    producto=producto_carrito.producto,
                    cantidad=producto_carrito.cantidad,
                    talla=producto_carrito.talla
                )

            return redirect('pedidos:pedidos')

        except Pedido.DoesNotExist:
            pagina_previa = request.META.get('HTTP_REFERER')
            messages.error(request, 'Se produjo un error al realizar el pedido. Inténtelo de nuevo.')
            return HttpResponseRedirect(pagina_previa)

        except CardError as e:
            pagina_previa = request.META.get('HTTP_REFERER')
            messages.error(request, 'Se produjo un error al realizar el pago. Inténtelo de nuevo.')
            return HttpResponseRedirect(pagina_previa)

    return redirect('general:indice')