from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Producto, Tipo_Prenda
from usuarios.models import Comentario

directorio_templates = "productos/"


def producto_detalle(request, id_producto):
    productos_recomendados = Producto.objects.exclude(id=id_producto).order_by('?')[:4]
    
    # 404
    producto_detalle = get_object_or_404(Producto, pk=id_producto)
    
    comentarios_producto = Comentario.objects.filter(producto__id=id_producto)

    contexto = {
        "producto_detalle": producto_detalle,
        "productos_recomendados":productos_recomendados,
        "comentarios":  comentarios_producto,
    }

    return render(request, directorio_templates + "/producto-detalle.html", contexto)

def seccion_productos(request, categoria=None):
    if categoria:
        productos = Producto.objects.filter(categoria__nombre=categoria)
    else:
        # 404
        productos = Producto.objects.all()
    
    tipo_prenda_list = Tipo_Prenda.objects.filter(producto__in=productos).distinct()
    
    productos_por_tipo_prenda = {}
    
    for tipo_prenda in tipo_prenda_list:
        productos_por_tipo_prenda[tipo_prenda] = productos.filter(producto_tipo_prenda=tipo_prenda).order_by('?')[:4]
        
    context = {
        'productos_por_tipo_prenda': productos_por_tipo_prenda,
        'categoria': categoria
    }
        
    return render(request, directorio_templates + 'seccion.html', context)

# Usamos una clase para esta vista porque es mas facil hacer la paginacion asi
def seccion_productos_tipo_prenda(request, categoria=None, tipo_prenda=None):
    tipo_prenda_descripcion_formateada = tipo_prenda.replace('-', ' ').capitalize()
    tipo_prenda_id = Tipo_Prenda.objects.get(descripcion = tipo_prenda_descripcion_formateada, categoria_padre__nombre=categoria)
    
    lista_productos = Producto.objects.filter(categoria__nombre=categoria, producto_tipo_prenda=tipo_prenda_id)
    
    paginacion = Paginator(lista_productos, 20)
    pagina = request.GET.get('pag')
    productos_por_pagina = paginacion.get_page(pagina)
        
    context = {
        'productos': productos_por_pagina,
        'categoria': categoria,
        'tipo_prenda': tipo_prenda_descripcion_formateada,
    }
    
    return render(request, directorio_templates + 'seccion-tipo-prenda.html', context)
   