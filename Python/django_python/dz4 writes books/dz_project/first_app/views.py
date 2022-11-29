from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home_page(request):
    return render(request, 'index.html', context={'text': 'Главная страница', 'page_list': [('writes', "Писатели"), ('books', "Книги")]})


def writes(request, write):
    if write == "aleksandr_pushkin":
        return HttpResponse(f"<h2>Русский поэт, драматург и прозаик, заложивший основы русского реалистического направления, литературный критик и теоретик литературы, историк, публицист, журналист.</h2>")
    elif write == "taras_shevchenko":
        return HttpResponse(f"<h2>Український поет, прозаїк, мислитель, живописець, гравер, етнограф, громадський діяч. Національний герой і символ України.</h2>")
    else:
        return render(request, 'writes.html', context={'text': 'Главная страница', 'page_list': [('aleksandr_pushkin', 'Александр Пушкин'), ('taras_shevchenko', 'Тарас Шевченко')]})
        # return HttpResponse(f"<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")

def books(request, book):
    if book == "voina_and_mir" or book == "1":
        return HttpResponse(f"<h2>Роман-эпопея Льва Николаевича Толстого, описывающий русское общество в эпоху войн против Наполеона в 1805—1812 годах.</h2>")
    elif book == "kavkaskii_plennik" or book == "2":
        return HttpResponse(f"<h2>Первая из цикла южных байронических поэм Пушкина. Начата в Гурзуфе (Крым), окончена 20 февраля 1821 г. в Каменке.</h2>")
    else:
        return render(request, 'books.html', context={'text': 'Главная страница', 'page_list': [('voina_and_mir', 'Война и мир'), ('kavkaskii_plennik', 'Кавказкий Пленник')]})
        # return HttpResponse(f"<br><div><a href='http://127.0.0.1:8000/'>Главная страница</a></div>")