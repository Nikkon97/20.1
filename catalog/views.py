from django.shortcuts import render

from catalog.models import Category, Product


def index(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Каталог - Главная'
    }
    return render(request, 'catalog/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Каталог - все категории'
    }
    return render(request, 'catalog/categories.html', context)


def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Продукты категории - {category_item.title}'
    }
    return render(request, 'catalog/products.html', context)
