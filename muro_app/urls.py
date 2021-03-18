from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall, name='wall'),
    path('/mensaje', views.mensaje, name='mensaje')
    ]