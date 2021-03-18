from django.urls import path
from . import views

urlpatterns = [
    path('wall/<int:id>', views.wall),
    ]