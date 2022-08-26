from django.shortcuts import render


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
usuario1= input()
    contraseña1= input()
    if usuario==usuario1 and contraseña==contraseña1
        print("Te damos la bienvenida a la Fundación Pueblo")
    else: 
        print("usuario o contraseña inválido")
    
def Register(request):
    template_name= "register.html"
    return render(request, template_name, {})


def contacto.Exitoso(request)
template_name="contacto.Exitoso.html"
return render (request,template_name)
