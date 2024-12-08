from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products


def catalog(request):
    cloth = Products.objects.all()
    per_page = request.GET.get('per_page', 5)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 5
    paginator = Paginator(cloth, per_page)

    page_number = request.GET.get('page')
    type_cloth = paginator.get_page(page_number)
    context = {
        'namepage': 'catalog',
        'title': 'Каталог',
        'type_cloth': cloth,
        'type_cloth': type_cloth,
        'per_page': per_page
    }
    return render(request, 'catalogpage.html', context)
