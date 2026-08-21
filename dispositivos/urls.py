# dispositivos/urls.py
from django.urls import path
from . import views

app_name = "dispositivos"

urlpatterns = [
    path("", views.inicio, name="inicio"),

    path("dispositivos/", views.catalogo, name="catalogo"),

    path(
    "zonas/<int:zona_id>/dispositivos/",
    views.dispositivos_zona,
    name="por_zona"),
    path(
        "dispositivo/<int:dispositivo_id>/",
        views.dispositivo,
        name="por_dispositivo",
    )
]