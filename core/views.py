from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto


# ----------------- INICIO -----------------
def inicio(request):
    return render(request, 'core/inicio.html')


# ----------------- CATEGORÍAS -----------------
def categorias_listado(request):
    categorias = Categoria.objects.all()
    return render(request, 'core/categorias_listado.html', {
        'categorias': categorias
    })


def categorias_crear(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")

        Categoria.objects.create(
            nombre=nombre,
            descripcion=descripcion
        )
        return redirect('categorias_listado')

    return render(request, 'core/categorias_form.html')


def categorias_editar(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":
        categoria.nombre = request.POST.get("nombre")
        categoria.descripcion = request.POST.get("descripcion")
        categoria.save()
        return redirect('categorias_listado')

    return render(request, 'core/categorias_form.html', {
        "categoria": categoria
    })


# ----------------- PRODUCTOS -----------------
def productos_listado(request):
    productos = Producto.objects.all()
    return render(request, 'core/productos_listado.html', {
        'productos': productos
    })


def productos_crear(request):
    categorias = Categoria.objects.all()

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")
        descripcion = request.POST.get("descripcion")
        categoria_id = request.POST.get("categoria")

        Producto.objects.create(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            categoria_id=categoria_id
        )
        return redirect('productos_listado')

    return render(request, 'core/productos_form.html', {
        "categorias": categorias
    })


def productos_editar(request, id):
    producto = get_object_or_404(Producto, id=id)
    categorias = Categoria.objects.all()

    if request.method == "POST":
        producto.nombre = request.POST.get("nombre")
        producto.precio = request.POST.get("precio")
        producto.descripcion = request.POST.get("descripcion")
        producto.categoria_id = request.POST.get("categoria")
        producto.save()
        return redirect('productos_listado')

    return render(request, 'core/productos_form.html', {
        "producto": producto,
        "categorias": categorias
    })


# ----------------- CREDITOS -----------------
def creditos(request):
    return render(request, 'core/creditos.html')

