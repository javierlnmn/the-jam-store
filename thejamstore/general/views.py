from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView

class IndiceView(TemplateView):
    template_name = "indice.html"