from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Pedido

directorio_templates = 'pedidos'

def pedidos(request):
    pedidos = Pedido.objects.filter(usuario_id = request.user.id)
    paginacion = Paginator(pedidos, 5)
    pagina = request.GET.get("pag")
    pedidos_por_pagina = paginacion.get_page(pagina)
    contexto = {
        'pedidos': pedidos_por_pagina
    }
    return render(request, directorio_templates + "/pedidos.html", contexto)