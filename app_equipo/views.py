from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo
from datetime import date 

# Listar equipos (READ)
def index(request):
    equipos = Equipo.objects.all()
    return render(request, 'listar_equipos.html', {'equipos': equipos})

# Agregar equipo (CREATE)
def agregar_equipo(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        
        # Convertir la cadena de fecha (YYYY-MM-DD) a objeto date
        fecha_str = request.POST['fecha_fundacion'] 
        fecha_fundacion = date.fromisoformat(fecha_str)

        entrenador = request.POST['entrenador']
        siglas = request.POST['siglas']
        color_uniforme = request.POST['color_uniforme']
        
        Equipo.objects.create(
            nombre=nombre, 
            ciudad=ciudad, 
            fecha_fundacion=fecha_fundacion,
            entrenador=entrenador,
            siglas=siglas,
            color_uniforme=color_uniforme
        )
        return redirect('inicio')
    return render(request, 'agregar_equipo.html')

# Editar equipo (UPDATE)
def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        equipo.nombre = request.POST['nombre']
        equipo.ciudad = request.POST['ciudad']
        
        fecha_str = request.POST['fecha_fundacion']
        equipo.fecha_fundacion = date.fromisoformat(fecha_str)
        
        equipo.entrenador = request.POST['entrenador']
        equipo.siglas = request.POST['siglas']
        equipo.color_uniforme = request.POST['color_uniforme']
        
        equipo.save()
        return redirect('inicio')
    return render(request, 'editar_equipo.html', {'equipo': equipo})

# Borrar equipo (DELETE)
def borrar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        equipo.delete()
        return redirect('inicio')
    return render(request, 'borrar_equipo.html', {'equipo': equipo})