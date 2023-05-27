from django.shortcuts import render
from django.views.generic import TemplateView
from productos.models import Producto

directorio_templates = "general/"

    
def indice(request):
    
    descuentos_semanales= []
    productos_oferta = Producto.objects.filter(oferta=True).order_by('-updated')
    for producto in productos_oferta:
        producto_stock = producto.producto_talla_set.all()
        hay_stock = False
        for talla in producto_stock:
            if talla.cantidad > 0: 
                hay_stock = True
                break
        if hay_stock and len(descuentos_semanales)<4: 
            descuentos_semanales.append(producto) 
        elif len(descuentos_semanales)>=4: 
            break
    print(descuentos_semanales)        
        
            
    contexto = {'productos': productos_oferta}
    return render(request,'general/indice.html',contexto)
