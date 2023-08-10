from django.shortcuts import render, get_object_or_404
from datetime import datetime
from main.models import Product

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    cat_list = Product.objects.all()
    context = {
        'object_list': cat_list
    }
    return render(request, 'main/index.html', context)

def contacts(request):
    """Контроллер, который отвечает за отображение контактной информации."""
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
    return render(request, 'contact.html')

def product(request, product_id):
    """представление страницы main/product.html для каждого продукта"""
    prod_get = get_object_or_404(Product, pk=product_id)
    return render(request, 'main/product.html', {'product': prod_get})

def great_prod(request):
    """Представление страницы main/great_prod.html с формой загрузки нового продукта"""
    if request.method == 'POST':
        product = {
            'name_prod': request.POST.get('name'),
            'description_prod': request.POST.get('description'),
            'category_prod': request.POST.get('category'),
            'price_prod': request.POST.get('price'),
            'data_create_prod': datetime.now(),
            'data_change_prod': datetime.now()
        }
        # загрузка нового продукта в БД
        Product.objects.create(**product)
    return render(request, 'main/great_prod.html')