from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Producto

directorio_templates = "productos/"


def producto_detalle(request, id_producto):
    
    producto_detalle = get_object_or_404(Producto, pk=id_producto)

    contexto = {
        "producto_detalle": producto_detalle,
    }
    
    print(producto_detalle.producto_color.all())

    return render(request, directorio_templates + "/producto-detalle.html", contexto)
