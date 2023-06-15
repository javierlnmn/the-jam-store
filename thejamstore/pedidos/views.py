from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Pedido

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