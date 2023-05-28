from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Producto

directorio_templates = "productos/"


def producto_detalle(request, id_producto):
    
    productos_recomendados = Producto.objects.exclude(id=id_producto).order_by('?')[:4]
    
    producto_detalle = get_object_or_404(Producto, pk=id_producto)

    contexto = {
        "producto_detalle": producto_detalle,
        "productos_recomendados":productos_recomendados,
    }

    return render(request, directorio_templates + "/producto-detalle.html", contexto)
