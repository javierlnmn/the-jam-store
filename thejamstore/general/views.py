from django.shortcuts import render
from django.views.generic import TemplateView

directorio_templates = "general/"


class IndiceView(TemplateView):
    template_name = directorio_templates + "indice.html"
