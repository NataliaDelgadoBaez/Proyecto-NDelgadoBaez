from django.shortcuts import render
from Tienda_app.models import Disco
from Tienda_app.forms import Crearalbumform, Buscaralbumform, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy




def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid(): 

            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')

            nombre_usuario = authenticate(username= usuario, password=clave)

            if usuario is not None:
                login (request, nombre_usuario)
                return render(request, "Tienda_app/tienda.html", {"mensaje":f"Has iniciado sesion, Bienvenido {usuario}"})
            else:
                return render(request, "Tienda_app/login.html", {"mensaje":"Usuario o contraseña incorrecta"})
           
        else:

            return render(request,"Tienda_app/login.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, "Tienda_app/login.html", {"form": form})

def register(request):

      if request.method == 'POST':

            
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"Tienda_app/register.html")

      else:
                 
            form = UserRegisterForm()     

      return render(request,"Tienda_app/soy nuevo.html" ,  {"form":form})

def inicio(request):
    return render(request, "Tienda_app/index.html")

def tienda(request):
    return render(request, "Tienda_app/tienda.html")

def blog(request):
    return render(request, "tienda_app/blog.html")

def busca_favorito(request):
    return render(request, "Tienda_app/busca tu favorito.html")

@login_required
def carrito(request):
    return render(request, "Tienda_app/carrito.html")

def final_carrito(request):
    return render(request, "Tienda_app/fcarrito.html")

def destacados(request):
    return render(request, "Tienda_app/destacados.html")

def iniciar_sesion(request):
    return render(request, "Tienda_app/login.html")

def tu_opinion(request):
    return render(request, "Tienda_app/tu opinion.html")

def musica_siempre(request):
    return render(request, "Tienda_app/Musica de siempre.html")

def musica_hoy(request):
    return render(request, "Tienda_app/Musica de hoy.html")

def conocenos(request):
    return render(request, "Tienda_app/conocenos.html")

def entrevistas(request):
    return render(request, "Tienda_app/entrevistas.html")


def Agregaralbum (request):
 
    if request.method == "POST":
 
        miFormulario = Agregaralbum(request.POST) 
        print(miFormulario)
 
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            album=  Disco(album=request.POST['album'],autor=request.POST['artista'], año=request.POST['año'], precio=request.POST['precio'])
            album.save()
            return render(request, "Tienda_app/index.html")
    else:
            miFormulario = Crearalbumform()
 
            return render(request, "Tienda_app/agregar album.html", {"miFormulario": miFormulario})


def Buscar_album(request):
    if request.method == "POST":
        miFormulario = Buscaralbumform(request.POST) 

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            discos = Disco.objects.filter(nombre__icontains=informacion["album"])

            return render(request, "Tienda_app/mostra tu favorito.html", {"album": discos})
    else:
        miFormulario = Buscaralbumform()

    return render(request, "Tienda_app/busca tu favorito.html", {"miFormulario": miFormulario})


def Mostraralbum (request):

    discos = Disco.objects.all() 

    contexto= {"cursos":discos} 

    return render(request, "Tienda_app/mostra tu favorito.html",contexto)

def leer_disco(request):

      discos = Disco.objects.all() 
      
      contexto= {"discos":discos} 

      return render(request, "Tienda_app/leerDiscos.html",contexto)

def eliminar_discos(request, discos_nombre):
 
    disco = Disco.objects.get(nombre = discos_nombre)
    disco.delete()
 
    # vuelvo al menú
    discos = Disco.objects.get(id=int(discos_nombre))  
    discos.delete()
 
    return render(request, "Tienda_app/leerDiscos.html", contexto)

class DiscoList (ListView):
    model = Disco
    template_name = "Tienda_app/ disco_lista.html"
    
class DiscoDetail(ListView):
    model = Disco
    template_name = "Tienda_app/ disco_detalles.html"
    
class DiscoCreate (ListView):
    model = Disco
    template_name = "Tienda_app/ disco_form.html"
    success_url = reverse_lazy ("list")
    fields = ['nombre', 'autor']

class DiscoUpdate (UpdateView):
    model = Disco
    template_name = "Tienda_app/ disco_edicion.html"
    success_url = reverse_lazy ("list")
    fields = ['nombre', 'autor']
    
class DiscoDelete (DeleteView):
    model = Disco
    template_name = "Tienda_app/ disco_borrado.html"
    success_url = reverse_lazy ("list")
    