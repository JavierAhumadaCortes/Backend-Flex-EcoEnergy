from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def inicio(request):
    contexto = {
        "sistema": "EcoEnergy 2 asdmnabsd khasd hg",
        "mensaje": "Monitoreo energético responsable",
        "asignatura": "Programación Back End",
    }

    return render(
        request,
        "dispositivos/inicio.html",
        contexto,
    )

def catalogo(request):
    dispositivos = [
        {"nombre": "Medidor inteligente", "estado": "Activo"},
        {"nombre": "Sensor de temperatura", "estado": "Activo"},
        {"nombre": "Medidor inteligente", "estado": "Activo"},
                {"nombre": "Sensor de temperatura", "estado": "Activo"},
                {"nombre": "Medidor inteligente", "estado": "Activo"},
                        {"nombre": "Sensor de temperatura", "estado": "Activo"},
                        {"nombre": "Medidor inteligente", "estado": "Activo"},
                                {"nombre": "Sensor de temperatura", "estado": "Activo"},
                                {"nombre": "Medidor inteligente", "estado": "Activo"},
                                        {"nombre": "Sensor de temperatura", "estado": "Activo"},
                                        {"nombre": "Medidor inteligente", "estado": "Activo"},
                                                {"nombre": "Sensor de temperatura", "estado": "Activo"},
        {"nombre": "Climatizador", "estado": "Revisión"},
    ]
    return render(
        request,
        "dispositivos/catalogo.html",
        {"dispositivos": dispositivos},
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