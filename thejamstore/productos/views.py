from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Producto, Tipo_Prenda

directorio_templates = "productos/"


def producto_detalle(request, id_producto):
    
    productos_recomendados = Producto.objects.exclude(id=id_producto).order_by('?')[:4]
    
    producto_detalle = get_object_or_404(Producto, pk=id_producto)

    contexto = {
        "producto_detalle": producto_detalle,
        "productos_recomendados":productos_recomendados,
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
        productos_por_tipo_prenda[tipo_prenda] = productos.filter(producto_tipo_prenda=tipo_prenda)[:4]
        
    context = {
        'productos_por_tipo_prenda': productos_por_tipo_prenda,
        'categoria': categoria
    }
        
    return render(request, directorio_templates + 'seccion.html', context)