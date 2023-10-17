from django.urls import path
from Users import views
from django.contrib.auth.views import LogoutView


urlpatterns +=[
    
    path('Users/register/', views.register, name="Soy nuevo"),
    path('editarUser', views.editarUser, name="EditarUser"), 

]