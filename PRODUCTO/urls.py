from django.urls import path
from PRODUCTO import views


urlpatterns = [
    path('',views.producto, name= "Producto"),
    path('Aumentar',views.aumentar, name="Aumentar"),
    path('mostrar/<int:producto_id>/', views.mostrar, name="mostrar"),
]
