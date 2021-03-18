from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_app.models import Usuario, Cuenta
from muro_app.models import Mensajes, Comentarios
from datetime import date
from django.contrib.auth import logout as do_logout
from django.db.models import Q, Max, Count, F
# Create your views here.

def wall(request, id):
    request.session['log_name'] = ""
    request.session['log_email'] = ""
    request.session['log_id'] = ""
    request.session['log_edad'] = 0
    request.session['log_user'] = 0
    return render(request, 'wall.html')