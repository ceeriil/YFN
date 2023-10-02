# from django.shortcuts import render
from django.views.generic import TemplateView
from app.vars import NAME


class HomeView(TemplateView):
    template_name = f"{NAME}/home.html"
