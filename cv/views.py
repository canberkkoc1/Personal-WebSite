from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'index.html' # sınıf tabanlı view oluşturudk index html i çağırdık
