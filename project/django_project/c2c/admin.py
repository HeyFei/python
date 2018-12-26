from django.contrib import admin
from . models import Restaurant, Dish, RestaurantReview
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(RestaurantReview)
