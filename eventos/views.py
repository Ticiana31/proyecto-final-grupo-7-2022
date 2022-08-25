from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings 


def Inicio(request):
    template_name = "inicio.html"
    return render(request, template_name, {})

def Informacion(request):
    template_name = "eventos_info.html"
    return render(request, template_name, {})

def Eventos(request):
    template_name = "eventos.html"
    return render(request, template_name, {})

def Recursos(request):
    template_name = "recursos.html"
    return render(request, template_name, {})

def Contactos(request):
    template_name= "contactos.html"
    return render(request, template_name, {})

def Login(request):
    template_name= "login.html"
    return render(request, template_name, {})

def Register(request):
    template_name= "register.html"
    return render(request, template_name, {})

def formularioContacto(request):
    return render(request, "formularioContacto.html")

def contactar (request):
    if request.method == "POST"
    asunto = request.POST ["txtAsunto"]
    mensaje = request.POST ["txtMensaje"] + "/ Email: " + request.POST ["txtMensaje"]
    email_desde = setting.EMAIL_HOST_USER
    email_para = [ticiana.31052001@gmail.com]
    send_email (asunto, mensaje, email_desde, email_para, fail_silently= False)
    return render (request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")
    
