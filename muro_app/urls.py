from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall, name='wall'),
    path('/mensaje', views.mensaje, name='mensaje'),
    path('/eliminar_msj/<int:id>', views.eliminar_msj, name='eliminar_msj'),
    path('/comentar/<int:mensaje_id>', views.comentar, name='comentar'),
    path('/eliminar_com/<int:id>', views.eliminar_com, name='eliminar_com'),
    ]