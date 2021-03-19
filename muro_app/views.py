from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_app.models import Usuario, Cuenta
from muro_app.models import Mensajes, Comentarios
from datetime import date
from django.contrib.auth import logout as do_logout
from django.db.models import Q, Max, Count, F
# Create your views here.

def wall(request):
    if request.session['log_user']:
        u_id = request.session['log_id']
        context = {
            'mensaje_w': Mensajes.objects.all().filter(mensaje_usuario_id=u_id).order_by('-id'),
            'comentario_w': Comentarios.objects.all().filter(comentario_usuario_id=u_id).order_by('-id')
        }
    else:
        return redirect('/')
    return render(request, 'wall.html', context)

def mensaje(request):
    if request.session['log_user']:
        if request.method == "POST":
            id = request.session['log_id']
            mensaje_w = Mensajes.objects.create(mensaje=request.POST['mensaje_wall'], mensaje_usuario_id=Usuario.objects.get(id=id))
            return redirect('wall')
        return redirect('/')
    return redirect('/')

def eliminar_msj(request, id):
    if request.session['log_user']:
        if request.method == "POST":
            temp = Mensajes.objects.get(id=id)
            temp.delete()
            return redirect('wall')
        return redirect('/')
    return redirect('/')

def comentar(request, mensaje_id):
    if request.session['log_user']:
        if request.method == "POST":
            id = request.session['log_id']
            comentario_w = Comentarios.objects.create(comentario=request.POST['coment_wall'],
                                                      comentario_mensaje_id=Mensajes.objects.get(id=mensaje_id),
                                                      comentario_usuario_id=Usuario.objects.get(id=id))
            return redirect('wall')
        return redirect('/')
    return redirect('/')

def eliminar_com(request, id):
    if request.session['log_user']:
        if request.method == "POST":
            temp = Comentarios.objects.get(id=id)
            temp.delete()
            return redirect('wall')
        return redirect('/')
    return redirect('/')