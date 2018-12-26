from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(blank=True, default='')
    telephone = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, default='')
    price = models.DecimalField('USD amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="myrestaurants", blank=True, null=True)
# Related name "dishes" allows you to use restaurant.dishes.all to access all dishes objects
# instead of using restaurant.dish_set.all
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# This Abstract Review can be used to create RestaurantReview and DishReview


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True


class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return "{} review".format(self.restaurant.name)
