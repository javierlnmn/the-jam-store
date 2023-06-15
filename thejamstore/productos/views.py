from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Producto, Tipo_Prenda
from pedidos.models import Pedido
from usuarios.models import Comentario, Lista_Deseos

directorio_templates = "productos"


def busqueda_productos(request):
    busqueda = request.GET.get("busqueda")
    palabras_busqueda = busqueda.split()

    resultado_busqueda = []
    for palabra in palabras_busqueda:
        # Se busca a traves del nombre y del tipo de prenda
        filtro = (
            Producto.objects.filter(nombre__icontains=palabra)
            | Producto.objects.filter(producto_tipo_prenda__descripcion__icontains=palabra)
            | Producto.objects.filter(producto_color__descripcion__icontains=palabra)
            | Producto.objects.filter(producto_marca__nombre__icontains=palabra)
        )
        for producto in filtro:
            resultado_busqueda.append(producto)

    resultado_busqueda = list(set(resultado_busqueda))

    pagina = request.GET.get("pag")
    paginacion = Paginator(resultado_busqueda, 12)
    productos_por_pagina = paginacion.get_page(pagina)

    contexto = {
        "busqueda": busqueda,
        "productos": productos_por_pagina,
    }

    return render(request, directorio_templates + "/resultados-busqueda.html", contexto)


# def filtrar_productos(palabras_busqueda):
#     filtro_nombre = Q()
#     filtro_color = Q()
#     filtro_tipo_prenda = Q()
#     filtro_marca = Q()

#     for palabra in palabras_busqueda:
#         filtro_nombre |= Q(nombre__icontains=palabra)
#         filtro_color |= Q(producto_color__descripcion__icontains=palabra)
#         filtro_tipo_prenda |= Q(producto_tipo_prenda__descripcion__icontains=palabra)
#         filtro_marca |= Q(producto_marca__nombre__icontains=palabra)

#     productos_por_nombre = Producto.objects.filter(filtro_nombre)
#     productos_por_color = Producto.objects.filter(filtro_color)
#     productos_por_tipo_prenda = Producto.objects.filter(filtro_tipo_prenda)
#     productos_por_marca = Producto.objects.filter(filtro_marca)

#     consulta = Producto.objects.none()

#     if productos_por_nombre:
#         consulta = productos_por_nombre

#     if productos_por_color and consulta:
#         consulta = consulta & productos_por_color
#     elif productos_por_color:
#         consulta = productos_por_color

#     if productos_por_tipo_prenda and consulta:
#         consulta = consulta & productos_por_tipo_prenda
#     elif productos_por_tipo_prenda:
#         consulta = productos_por_tipo_prenda

#     if productos_por_marca and consulta:
#         consulta = consulta & productos_por_marca
#     elif productos_por_marca:
#         consulta = productos_por_marca

#     return consulta


def producto_detalle(request, id_producto):
    # 404
    producto_detalle = get_object_or_404(Producto, pk=id_producto)

    productos_recomendados = Producto.objects.exclude(id=id_producto).order_by("?")[:4]

    pedido_por_usuario = False
    if request.user.is_authenticated:
        pedidos_del_usuario = Pedido.objects.filter(usuario=request.user.id)
        pedido_por_usuario = comprobarPedidoPorUsuario(
            producto_detalle.id, pedidos_del_usuario
        )
    
    esta_en_lista_de_deseos = False
    
    if request.user.is_authenticated:
        lista_deseos, _ = Lista_Deseos.objects.get_or_create(usuario=request.user)
        if lista_deseos and lista_deseos.producto.filter(id=producto_detalle.id).exists():
            esta_en_lista_de_deseos = True
    
    comentarios_producto = Comentario.objects.filter(producto__id=id_producto)
    paginacion = Paginator(comentarios_producto, 5)
    pagina = request.GET.get("pag")
    comentarios_por_pagina = paginacion.get_page(pagina)

    contexto = {
        "producto_detalle": producto_detalle,
        "productos_recomendados": productos_recomendados,
        "esta_en_lista_de_deseos": esta_en_lista_de_deseos,
        "pedido_por_usuario": pedido_por_usuario,
        "comentarios": comentarios_por_pagina,
    }

    return render(request, directorio_templates + "/producto-detalle.html", contexto)


def comprobarPedidoPorUsuario(producto_detalle, pedidos_del_usuario):
    pedido_por_usuario = {
        "comprado": False,
        "recibido": False,
    }

    for pedido in pedidos_del_usuario:
        for producto in pedido.producto.all():
            if producto.id == producto_detalle:
                pedido_por_usuario["comprado"] = True
                if pedido.estado.descripcion == "Entregado":
                    pedido_por_usuario["recibido"] = True
                return pedido_por_usuario

    return pedido_por_usuario


def seccion_productos(request, categoria=None):
    if categoria:
        productos = Producto.objects.filter(categoria__nombre=categoria)
    else:
        return HttpResponseNotFound('Error 404')

    tipo_prenda_list = Tipo_Prenda.objects.filter(
        producto__in=productos, categoria_padre__nombre=categoria
    ).distinct()

    productos_por_tipo_prenda = {}

    for tipo_prenda in tipo_prenda_list:
        productos_por_tipo_prenda[tipo_prenda] = productos.filter(
            producto_tipo_prenda=tipo_prenda
        ).order_by("?")[:4]

    context = {
        "productos_por_tipo_prenda": productos_por_tipo_prenda,
        "categoria": categoria,
    }

    return render(request, directorio_templates + "/seccion.html", context)


def seccion_productos_tipo_prenda(request, categoria=None, tipo_prenda=None):
    tipo_prenda_descripcion_formateada = tipo_prenda.replace("-", " ").capitalize()
    tipo_prenda_id = Tipo_Prenda.objects.get(
        descripcion=tipo_prenda_descripcion_formateada,
        categoria_padre__nombre=categoria,
    )

    lista_productos = Producto.objects.filter(
        categoria__nombre=categoria, producto_tipo_prenda=tipo_prenda_id
    )

    paginacion = Paginator(lista_productos, 20)
    pagina = request.GET.get("pag")
    productos_por_pagina = paginacion.get_page(pagina)

    context = {
        "productos": productos_por_pagina,
        "categoria": categoria,
        "tipo_prenda": tipo_prenda_descripcion_formateada,
    }

    return render(request, directorio_templates + "/seccion-tipo-prenda.html", context)
