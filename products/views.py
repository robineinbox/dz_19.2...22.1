from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from main.models import Product
from .forms import ProductForm, VersionForm
from .models import Version


def great_prod(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'Продукт успешно создан!')
            return redirect('products:product_detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'products/create_product.html', {'form': form})


def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Продукт успешно отредактирован!')
            return redirect('products:product_detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/edit_product.html', {'form': form})


def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Продукт успешно удален!')
        return redirect('products:product_list')
    return render(request, 'products/delete_product.html', {'product': product})


def create_version(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = VersionForm(request.POST)
        if form.is_valid():
            version = form.save(commit=False)
            version.product = product
            version.save()
            messages.success(request, 'Версия успешно создана!')
            return redirect('products:product_detail', pk=product.pk)
    else:
        form = VersionForm()
    return render(request, 'products/create_version.html', {'form': form, 'product': product})


def edit_version(request, pk):
    version = get_object_or_404(Version, pk=pk)
    if request.method == 'POST':
        form = VersionForm(request.POST, instance=version)
        if form.is_valid():
            version = form.save()
            messages.success(request, 'Версия успешно отредактирована!')
            return redirect('products:product_detail', pk=version.product.pk)
    else:
        form = VersionForm(instance=version)
    return render(request, 'products/edit_version.html', {'form': form, 'version': version})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    active_version = product.versions.filter(is_active=True).first()
    return render(request, 'products/product_detail.html', {'product': product, 'active_version': active_version})
