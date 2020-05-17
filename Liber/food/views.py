from django.shortcuts import render, get_object_or_404
from .models import Tag, Restaurant, DishCategory, Dish


def restaurant_list(request):
    tag = Tag.objects.all()
    restaurant = Restaurant.objects.all()
    context = {
        'tag': tag,
        'restaurant': restaurant,
    }
    return render(request, 'food/restaurant_list.html', context)

def dish_list(request, slug_restaurant):
    restaurant = get_object_or_404(Restaurant, slug_restaurant__iexact=slug_restaurant)
    dishcat = DishCategory.objects.all()
    context = {
        'restaurant': restaurant,
        'dishcat': dishcat,
    }
    return render(request, 'food/dish_list.html', context)

def dish_detail(request, slug_restaurant, slug_dish):
    dish = get_object_or_404(Dish, slug_dish__iexact=slug_dish)
    restaurant = get_object_or_404(Restaurant, slug_restaurant__iexact=slug_restaurant)
    context = {
        'dish': dish,
        'restaurant': restaurant,
    }
    return render(request, 'food/dish_detail.html', context)