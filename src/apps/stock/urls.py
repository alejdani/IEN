from django.urls import path, include
from .views import eliminar_articulo, home_view, listar_stock, detalle_articulo, crear_articulo, CrearArticulo, CrearCategoria, ListarArticulos   


urlpatterns = [
    
    path('', home_view, name='home'),
    path('stock/listar/', listar_stock, name='listar_stock'),
    path('stock/detalle/<int:pk>/', detalle_articulo, name='detalle_articulo'),
    path("stock/eliminar/<int:pk>/", eliminar_articulo, name="eliminar_articulo"),

    path("stock/crear-categoria/", CrearCategoria.as_view(), name="crear_vbc_categoria"),
    path("stock/crear-articulo/", CrearArticulo.as_view(), name="crear_vbc_articulo"),
    path("stock/crear/", crear_articulo, name="crear_Articulo"),
    path("stock/listar-articulo/", ListarArticulos.as_view(), name="listar_articulo"),
]