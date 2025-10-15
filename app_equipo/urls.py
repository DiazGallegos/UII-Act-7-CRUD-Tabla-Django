from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('agregar/', views.agregar_equipo, name='agregar_equipo'),
    path('editar/<int:id>/', views.editar_equipo, name='editar_equipo'),
    path('borrar/<int:id>/', views.borrar_equipo, name='borrar_equipo'),
]