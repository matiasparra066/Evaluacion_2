from django.shortcuts import render
from django.http import Http404

# Create your views here.
TEMAS = [
    {
        "slug": "paisajes-de-chile",
        "nombre": "Paisajes de Chile",
        "descripcion": (
            "Chile se extiende por más de 4.000 km y reúne desiertos, volcanes, "
            "lagos, glaciares y costa. Un recorrido visual por algunos de sus "
            "escenarios naturales más impresionantes."
        ),
        "resumen": "Desiertos, volcanes, lagos y glaciares de norte a sur.",
        "imagenes": [
            {"archivo": "images/paisajes/desierto.svg", "titulo": "Desierto de Atacama"},
            {"archivo": "images/paisajes/volcan.svg", "titulo": "Volcán Osorno"},
            {"archivo": "images/paisajes/glaciar.svg", "titulo": "Glaciares de la Patagonia"},
        ],
    },
    {
        "slug": "cocina-chilena",
        "nombre": "Cocina Chilena",
        "descripcion": (
            "La gastronomía chilena mezcla tradición indígena, influencia "
            "española y productos del mar y del campo. Estos platos son parte "
            "de la mesa en celebraciones y días comunes."
        ),
        "resumen": "Empanadas, pastel de choclo y más sabores tradicionales.",
        "imagenes": [
            {"archivo": "images/cocina/empanada.svg", "titulo": "Empanada de pino"},
            {"archivo": "images/cocina/pastel.svg", "titulo": "Pastel de choclo"},
        ],
    },
]


def _buscar_tema(slug):
    for tema in TEMAS:
        if tema["slug"] == slug:
            return tema
    raise Http404("El tema solicitado no existe.")


def lista_temas(request):
    return render(request, "inicio_parra_flores/lista_temas.html", {"temas": TEMAS})


def detalle_tema(request, slug):
    tema = _buscar_tema(slug)
    return render(request, "inicio_parra_flores/detalle_tema.html", {"tema": tema})


def acerca(request):
    return render(request, "inicio_parra_flores/acerca.html", {"temas": TEMAS})