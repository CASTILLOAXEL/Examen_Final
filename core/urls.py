from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('categorias/', views.categorias_listado, name='categorias_listado'),
    path('categorias/nueva/', views.categorias_crear, name='categorias_crear'),
    path('categorias/editar/<int:id>/', views.categorias_editar, name='categorias_editar'),

    path('productos/', views.productos_listado, name='productos_listado'),
    path('productos/nuevo/', views.productos_crear, name='productos_crear'),
    path('productos/editar/<int:id>/', views.productos_editar, name='productos_editar'),

    path('creditos/', views.creditos, name='creditos'),
]
