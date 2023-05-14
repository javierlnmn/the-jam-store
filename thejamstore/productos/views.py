from django.shortcuts import render
from django.views.generic import DetailView
from .models import Producto

directorio_templates = "productos/"


class ProductoView(DetailView):
    model = Producto
    template_name = directorio_templates + "producto.html"
