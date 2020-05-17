from django.contrib import admin

from .models import Tag, Restaurant, DishCategory, Dish


class TagConfig(admin.ModelAdmin):
    fields = ('name', 'img', 'slug_tag')
    prepopulated_fields = {'slug_tag': ('name',)}


admin.site.register(Tag, TagConfig)


class RestaurantConfig(admin.ModelAdmin):
    fields = ('name', 'description', 'img', ('rating', 'time_delivery'), 'tags', 'slug_restaurant')
    list_display = ('name', 'description', 'rating', 'time_delivery')
    prepopulated_fields = {'slug_restaurant': ('name',)}


admin.site.register(Restaurant, RestaurantConfig)


class DishCategoryConfig(admin.ModelAdmin):
    fields = ('name', 'slug_dishcategory')
    prepopulated_fields = {'slug_dishcategory': ('name',)}


admin.site.register(DishCategory, DishCategoryConfig)


class DishConfig(admin.ModelAdmin):
    fields = (('name', 'available'), ('restaurant', 'category'), 'description', ('img', 'price'), 'slug_dish')
    list_display = ('name', 'restaurant', 'category', 'price', 'available')
    prepopulated_fields = {'slug_dish': ('name',)}


admin.site.register(Dish, DishConfig)
