from django.db import models
from django.db.models import Avg, Count
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Actor(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    surname = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + self.surname


class Director(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    surname = models.CharField(max_length=45, blank=True, null=True)

    def __str__(self):
        return self.name + ' ' + self.surname


class Movie(models.Model):
    title = models.CharField(max_length=45, blank=True, null=True)

    class Category(models.TextChoices):
        ACTION = _('Action')
        DRAMA = _('Drama')
        COMEDY = _('Comedy')
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.ACTION,
    )
    description = models.CharField(max_length=255, blank=True, null=True)
    director = models.ManyToManyField(Director)
    actor = models.ManyToManyField(Actor)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    def count(self):
        number = Rating.objects.filter(movie=self)
        return 'number of rates: ' + str(len(number))

    def get_rating(self):
        return Rating.objects.filter(movie=self).aggregate(Avg("value"))

    def __str__(self):
        return self.title


class Rating(models.Model):
    value = models.FloatField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.user + ': ' + str(self.movie) + ' (' + str(self.value) + ")"


