from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_app.models import Usuario, Cuenta
from muro_app.models import Mensajes, Comentarios
from datetime import date, datetime, timedelta
from django.contrib.auth import logout as do_logout
from django.db.models import Q, Max, Count, F
# Create your views here.

def wall(request):
    if request.session['log_user']:
        u_id = request.session['log_id']

        context = {
            # 'mensaje_w': Mensajes.objects.all().filter(mensaje_usuario_id=u_id).order_by('-id'),
            # 'comentario_w': Comentarios.objects.all().filter(comentario_usuario_id=u_id).order_by('-id')

            'mensaje_w': Mensajes.objects.all().order_by('-id'),
            'comentario_w': Comentarios.objects.all().order_by('-id')
        }

        return render(request, 'wall.html', context)
    return redirect('/')

def mensaje(request):
    if request.session['log_user']:
        if request.method == "POST":
            if request.POST['mensaje_wall']:
                id = request.session['log_id']
                mensaje_w = Mensajes.objects.create(mensaje=request.POST['mensaje_wall'], mensaje_usuario_id=Usuario.objects.get(id=id))
                return redirect('wall')
            return redirect('wall')
        return redirect('/')
    return redirect('/')

# def eliminar_msj(request, id):
#     if request.session['log_user']:
#         if request.method == "POST":
#             temp = Mensajes.objects.get(id=id)
#             temp.delete()
#             return redirect('wall')
#         return redirect('/')
#     return redirect('/')

    ### Probando límite de tiempo para eliminar mensaje ###

def eliminar_msj(request, id):
    hora_actual = datetime.now()
    msj = Mensajes.objects.get(id=id)
    hora_msj = msj.created_at
    print('hora actual datetime: ', hora_actual)
    print('hora msj: ', hora_msj)

    # minutos_tranascurridos = hora_actual - hora_msj
    if request.session['log_user']:
        if request.method == "POST":
            # if minutos_tranascurridos < 30:
                temp = Mensajes.objects.get(id=id)
                temp.delete()
                return redirect('wall')
            # return redirect('wall')
        return redirect('/')
    return redirect('/')


def comentar(request, mensaje_id):
    if request.session['log_user']:
        if request.method == "POST":
            if request.POST['coment_wall']:
                id = request.session['log_id']
                comentario_w = Comentarios.objects.create(comentario=request.POST['coment_wall'],
                                                          comentario_mensaje_id=Mensajes.objects.get(id=mensaje_id),
                                                          comentario_usuario_id=Usuario.objects.get(id=id))
                return redirect('wall')
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