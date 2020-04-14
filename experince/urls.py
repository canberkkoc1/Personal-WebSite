from django.contrib import admin
from django.urls import path
from .views import exper_view

urlpatterns = [
   path('',exper_view, name='experince'),

]
