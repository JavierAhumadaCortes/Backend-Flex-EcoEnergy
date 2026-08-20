from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    return HttpResponse(
        "<h1>EcoEnergy</h1>"
        "<p>Back End en funcionamiento</p>"
    )

def dispositivos_zona(request, zona_id):
    if zona_id != 3:
        return HttpResponse(
            "Zona no encontrada", status=404
        )
    
    return HttpResponse(
        f"Dispositivos de la zona {zona_id}"
    )

def dispositivo(request, dispositivo_id):
    if dispositivo_id != 3:
        return HttpResponse(
            "dispositivo no encontrada", status=404
        )
    
    return HttpResponse(
        f"Dispositivos encontrado {dispositivo_id}"
    )