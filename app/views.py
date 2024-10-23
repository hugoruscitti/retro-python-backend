from django.shortcuts import render
from app.models import Proyecto
from django.shortcuts import get_object_or_404
import json
from django.http import JsonResponse


def home(request):
    return render(request, "home.html")

def subir(request):
    data = json.loads(request.body.decode("utf-8"))
    p = Proyecto.objects.create(
        screenshot = data["screenshot"],
        version = data["version"],
        codigo = data["codigo"],
        textura = data["textura"],
    )

    return JsonResponse({"hash": p.hash})

def obtener(request, hash):
    proyecto = get_object_or_404(Proyecto, hash=hash)

    return JsonResponse({
        "hash": proyecto.hash,
        "fecha": proyecto.fecha,
        "version": proyecto.version,
        "screenshot": proyecto.screenshot,
        "textura": proyecto.textura,
        "codigo": proyecto.codigo,
    })
