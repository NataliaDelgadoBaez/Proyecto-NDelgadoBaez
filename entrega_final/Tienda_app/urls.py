from django.urls import path
from Tienda_app import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path('inicio/', views.inicio, name="Inicio"),
    path('tienda/', views.tienda, name="Tienda"),
    path('blog/', views.blog, name="Blog"),
    path('carrito/', views.carrito, name="Carrito"),
    path('carrito/', views.final_carrito, name="Fcarrito"),
    path('destacados/', views.destacados, name="Destacados"),
    path('login/', views.login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name='Tienda_app/logout.html'), name="Logout"),
    path('tu opinion/', views.tu_opinion, name="Tu opinion"),
    path('crear album/', views.Agregaralbum, name="Crear album"),
    path('musica de siempre/', views.musica_siempre, name="Musica de siempre"),
    path('musica de hoy/', views.musica_hoy, name="Musica de hoy"),
    path('entrevistas/', views.entrevistas, name="Entrevistas"),
    path('conocenos/', views.conocenos, name="Conocenos"),
    
]  
  
urlpatterns +=[  
    path('disco_lista/', views.DiscoList.as_view(), name="List"),
    path('disco_detalle/<pk>/', views.DiscoDetail.as_view(), name="Detail"),
    path('disco_create/', views.DiscoCreate.as_view(), name="Create"),
    path('disco_update/<pk>/', views.DiscoUpdate.as_view(), name="Update"),
    path('disco_delete/<pk>/', views.DiscoDelete.as_view(), name="Delete"),

]
    
