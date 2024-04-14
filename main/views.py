from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
    }

    return render(request, 'main/about.html', context)

def contact(request):
    context = {
        'title': ' Home - Связь со мной',
        'content': 'Шахмедов Артур',
        'instagram': 'https://www.instagram.com/true.l_am_rip/',
        'telegram': 'https://t.me/True_Love_Artur',
    }
    return render(request, 'main/mycontact.html', context)