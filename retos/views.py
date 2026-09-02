from django.shortcuts import render
from django.shortcuts import render
from django.http import Http404

RETES_BD = {
    1: {
        'titulo': 'Suma de dos números',
        'dificultad': 'Fácil',
        'descripcion': 'Escribe una función que reciba dos números enteros y devuelva su suma.',
        'entrada': '2, 3',
        'salida': '5'
    },
    2: {
        'titulo': 'Invertir una cadena',
        'dificultad': 'Media',
        'descripcion': 'Crea un algoritmo que tome un texto (String) y lo devuelva al revés.',
        'entrada': '"hola"',
        'salida': '"aloh"'
    },
    3: {
        'titulo': 'Validar número Primo',
        'dificultad': 'Difícil',
        'descripcion': 'Determina si un número entero positivo dado es un número primo.',
        'entrada': '7',
        'salida': 'True'
    }
}

def inicio(request):
    contexto = {'lista_retos': RETES_BD}
    return render(request, 'retos/inicio.html', contexto)

def detalle_reto(request, reto_id):
    reto = RETES_BD.get(reto_id)
    if reto is None:
        raise Http404("El reto solicitado no existe.")
    
    contexto = {
        'reto': reto
    }
    return render(request, 'retos/detalle_reto.html', contexto) 

def error_404(request, exception):
    return render(request, 'retos/404.html', status=404)
