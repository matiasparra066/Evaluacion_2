from django.urls import path

from . import views

app_name = "inicio"

urlpatterns = [
    path("", views.lista_temas, name="lista_temas"),
    path("tema/<slug:slug>/", views.detalle_tema, name="detalle_tema"),
    path("acerca/", views.acerca, name="acerca"),
]