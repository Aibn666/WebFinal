import PRODUCTO
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from PRODUCTO.models import Producto, Categoria
from .productos import Productos
from django import forms
from django.urls import reverse

class FormAltaProducto(forms.Form):
    titulo=forms.CharField(label= "nuevo producto")
    imagen=forms.ImageField()
    descripcion=forms.CharField(label= "descripcion")
    precio=forms.FloatField(label= "precio")
    categoria=forms.CharField(label="categoria")


# Create your views here.

def producto(request):
    producto=Producto.objects.all()
    return render(request, 'producto/Producto.html',{
        "productos": producto
    })

def aumentar(request):
    if request.method == "POST":
        form = FormAltaProducto(request.POST)
        if form.is_valid():
            producto= form.cleaned_data["producto"]
            request.session["productos"] += [producto]
            return HttpResponseRedirect(reverse('Producto'))
        else:
            return render(request,"producto/Aumentar.html")
    else:
        return render(request,"producto/Aumentar.html")

def mostrar(request, producto_id):
    productos=Productos(request)
    producto=Producto.objects.get(id=producto_id)
    

    return render(request, 'producto/mostrar.html',{
        "producto": producto
    })
#def aumentar(request):
    return render(request,"producto/Aumentar.html")
#def producto(request):
    producto=Producto.objects.all()
    return render(request, 'producto/Producto.html',{
        "productos": producto
    })



#class FormAltaProducto(forms.Form):
    producto = forms.CharField(label="nuevo producto")

#def producto(request):
    if "productos" not in request.session:
        request.session["productos"] = []
    return render(request, "PRODUCTO/Producto.html",{
        "productos": request.session["productos"]
    })

#def agregar(request):

    if request.method == "POST":
        form = FormAltaProducto(request.POST)
        if form.is_valid():
            producto = form.cleaned_data["producto"]
            request.session["producto"] += [producto]
            return HttpResponse(reverse('PRODUCTO:Producto'))
        else:
            return render(request, "PRODUCTO/agregar.html")
    else:
        return render(request, "PRODUCTO/agregar.html")
