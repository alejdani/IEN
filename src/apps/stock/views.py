from django.shortcuts import render

from .models import Articulo, Categoria
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from datetime import datetime
from .forms import FormularioArticulos 

from django.contrib import messages 


def home_view(request):
    template = "stock/home.html"
    return render(request, template)

def listar_stock(request):
    template = "stock/listar_stock.html"
    #> = gt  >= gte  <=lt  <= lte 
    lista_articulos_bd = Articulo.objects.all().order_by("precio")


    context ={
        "lista_articulos" : lista_articulos_bd
    }
    return render(request, template, context)


def detalle_articulo(request, pk):
    template = "stock/detalle_articulo.html"
    articulo_bd = Articulo.objects.get(id=pk)


    context ={
        "articulo" : articulo_bd
    }
    return render(request, template, context)


def eliminar_articulo(request, pk):
    Articulo.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse("listar_stock"))
    

def crear_articulo(request):
    template = "stock/crear_articulo.html"
    context = {}
    print( "obtener metodo",request.method)
    
    if request.method == "GET":
        form = FormularioArticulos()
        print("formulario", form)
        context["form"] =form 


    print ("request", request.POST)

    if request.method =="POST":
        try:
            Articulo.objects.create(nombre=request.POST["nombre"],precio=request.POST["precio"],descripcion=request.POST["descripcion"],fecha=datetime.now())
            messages.success(request, "articulo creado exitsamente")
            return HttpResponseRedirect(reverse("listar_stock"))
        except:
            messages.error(request, "fallo al crear articulo")
    
    
    return render(request,template,context)

from django.views.generic.edit import CreateView
from django.views.generic import  ListView
class CrearArticulo(CreateView):
    model = Articulo
    template_name = "stock/crear_articulo.html" 
    # form_class = FormularioArticulos 
    fields = ["nombre", "precio","descripcion","fecha"]
    success_url = reverse_lazy("listar_stock")


class CrearCategoria(CreateView):
    model = Categoria
    template_name = "categoria/crear_categoria.html" 
    # form_class = FormularioArticulos 
    fields = ["nombre", "precio","descripcion","fecha"]
    success_url = reverse_lazy("listar_categoria")

class ListarArticulos(ListView):
    model = Articulo
    template_name = "stock/listar_stock.html"
    context_objext_name = "lista_articulos" 
