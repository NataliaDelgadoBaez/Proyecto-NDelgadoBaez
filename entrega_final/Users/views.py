from django.shortcuts import render
from Tienda_app.views import UserEditForm, UserRegisterForm


@login_required
def editarUser(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return render(request, "Users/index.html")

    else:

        miFormulario = UserEditForm(initial={'email': usuario.email})

    return render(request, "Users/editar_user.html", {"miFormulario": miFormulario, "usuario": usuario})

def register(request):

      if request.method == 'POST':

            
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"Tienda_app/register.html")

      else:
                 
            form = UserRegisterForm()     

      return render(request,"/soy nuevo.html" ,  {"form":form})

def iniciar_sesion(request):
    return render(request, "Users/login.html")