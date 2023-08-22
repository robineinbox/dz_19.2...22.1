from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from .models import Product, Category


def home(request: HttpRequest):
    return render(request, 'main/base.html')

def contact(request: HttpRequest):
    return render(request, 'main/contact.html')

def index(request: HttpRequest):
    cat_list = Product.objects.all()
    context = {
        'object_list': cat_list
    }
    return render(request, 'main/index.html', context)

def contacts(request: HttpRequest):
    """Контроллер, который отвечает за отображение контактной информации."""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
    return render(request, 'main/contact.html')

def product(request: HttpRequest, product_id: int):
    """представление страницы main/product.html для каждого продукта"""
    prod_get = get_object_or_404(Product, pk=product_id)
    return render(request, 'main/product.html', {'product': prod_get})

def great_prod(request: HttpRequest):
    """Представление страницы main/great_prod.html с формой загрузки нового продукта"""
    if request.method == 'POST':
        product = {
            'name_prod': request.POST.get('name'),
            'description_prod': request.POST.get('description'),
            'category_prod': int(request.POST.get('category')),
            'price_prod': int(request.POST.get('price')),
            'data_create_prod': datetime.now(),
            'data_change_prod': datetime.now()
        }
        new_product = Product.objects.create(
            name=product['name_prod'],
            description=product['description_prod'],
            category_id=product['category_prod'],
            unit_price=product['price_prod'],
            produce_day=product['data_create_prod'],
            last_change=product['data_change_prod']
        )
        new_product.save()
        return redirect('index')
    else:
        return render(request, 'main/great_prod.html', {'categories': Category.objects.all()})

