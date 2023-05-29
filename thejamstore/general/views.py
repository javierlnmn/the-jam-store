from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from productos.models import Producto, Producto_Destacado

directorio_templates = "general/"


def indice(request):
    ofertas_recientes = []
    productos_oferta = Producto.objects.filter(oferta=True).order_by("-updated")

    for producto in productos_oferta:
        producto_stock = producto.producto_talla_set.all()
        hay_stock = False

        for talla in producto_stock:
            if talla.cantidad > 0:
                hay_stock = True
                break

        if hay_stock and len(ofertas_recientes) < 4:
            ofertas_recientes.append(producto)

        elif len(ofertas_recientes) >= 4:
            break

    producto_destacado = None
    destacados = get_object_or_404(Producto_Destacado,)
    producto_destacado = destacados.producto
    
    print(request.user)

    contexto = {
        "ofertas_recientes": ofertas_recientes,
        "producto_destacado": producto_destacado,
    }

    return render(request, directorio_templates+"/indice.html", contexto)
