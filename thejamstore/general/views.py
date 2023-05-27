from django.shortcuts import render
from django.views.generic import TemplateView
from productos.models import Producto

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

    producto_novedad = Producto.objects.latest("created")

    contexto = {
        "ofertas_recientes": ofertas_recientes,
        "producto_novedad": producto_novedad,
    }

    return render(request, directorio_templates+"/indice.html", contexto)
