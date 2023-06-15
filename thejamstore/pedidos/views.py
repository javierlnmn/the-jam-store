from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Pedido
from usuarios.models import Custom_User, Direccion
from usuarios.models import Carrito

import stripe
from stripe.error import CardError

stripe.api_key = settings.STRIPE_SECRET_KEY

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
    
    return render(request, directorio_templates + "/detalle_pedido.html", contexto)
        
    

# @login_required
# def realizar_pago(request):
#     # Obtener el ID del viaje de la sesión
#     session = SessionStore(request.session.session_key)
#     viaje_id = session.get('viaje_id')

#     # Verificar si el ID del viaje está presente en la sesión
#     if viaje_id is None:
#         # El ID del viaje no está en la sesión, manejar el error o redirigir a una página apropiada
#         return redirect('error')

#     try:
#         # Obtener el objeto Viaje por su ID
#         viaje = Viaje.objects.get(id=viaje_id)

#         # Realizar cualquier lógica adicional necesaria antes del pago

#         # Renderizar el template de pago y pasar el objeto Viaje como variable de contexto
#         return render(request, directorio_templates+'payment.html', {'pedido': pedido})

#     except Viaje.DoesNotExist:
#         # El objeto Viaje no existe, manejar el error o redirigir a una página apropiada
#         return redirect('error')



# @login_required
# def marcar_viaje_como_pagado(request, viaje_id):
#     if request.method == 'POST':
#         try:
#             # Obtén el objeto Viaje por su ID
#             viaje = Viaje.objects.get(id=viaje_id)

#             # Actualiza el campo 'pagado' a True
#             viaje.pagado = True

#             # Procesar el pago utilizando la biblioteca de Stripe
#             stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
#             charge = stripe.Charge.create(
#                 amount=int(viaje.precioTotal * 100),  # Convertir a entero y montar en centavos
#                 currency='usd',  # Moneda (actualiza según tu configuración)
#                 source=request.POST['stripeToken'],  # Token de tarjeta enviado desde el formulario
#                 description='Pago del viaje: {}'.format(viaje.id)
#             )

#             # Guarda los cambios en la base de datos
#             viaje.save()

#             # Redirige a la vista de verViajes
#             return redirect('verViajes')

#         except Viaje.DoesNotExist:
#             # El objeto Viaje no existe, maneja el error o redirige a una página apropiada
#             return redirect('error')

#         except CardError as e:
#             # Captura la excepción de CardError y pasa el mensaje de error al template
#             error_message = e.user_message
#             return render(request, 'payment.html', {'viaje': viaje, 'error': error_message})

#     return redirect('error')