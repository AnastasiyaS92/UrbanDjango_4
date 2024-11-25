from django.shortcuts import render


def platform_page(request):
    title = 'Play'
    headline = 'Главная страница'
    context = {
        'title': title,
        'headline': headline,
    }
    return render(request, 'fourth_task/platform.html', context)


def games_page(request):
    title = 'Games'
    text = 'Игры'
    pay = 'Купить'
    context = {
        'title': title,
        'Игры': text,
        'pay': pay,
    }
    return render(request, 'fourth_task/games.html', context)


def cart_page(request):
    title = 'Cart'
    text = 'Корзина'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'fourth_task/cart.html', context)

# Create your views here.
