
from django.urls import path
from .views import HomePageView


urlpatterns = [

    path('',HomePageView.as_view(), name = 'index' ), # boş gelirse cv de bulunan ursl e bak

]
