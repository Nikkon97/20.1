from django.shortcuts import render

from catalog.models import Category, Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Каталог - Главная'
    }
    return render(request, 'catalog/index.html', context)


def categories(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Каталог - все категории'
    }
    return render(request, 'catalog/categories.html', context)


def product_desc(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'{product_item.title}',
        'desc': f'{product_item.desc}'
    }
    return render(request, 'catalog/product.html', context)
