from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all().order_by('-fecha_creacion')
    return render(request, 'productos/lista.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']

        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            stock=stock
        )
        return redirect('lista_productos')

    return render(request, 'productos/crear.html')

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.save()
        return redirect('lista_productos')

    return render(request, 'productos/editar.html', {'producto': producto})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('lista_productos')