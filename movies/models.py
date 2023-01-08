from django.db import models


# class Movie(models.Model):
#     id = models.IntegerField(primary_key=True)
#     title = models.CharField(max_length=45, blank=True, null=True)
#     category = models.CharField(max_length=45, blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     director = models.ForeignKey(Director, models.DO_NOTHING)
#     actor = models.ManyToManyField(Actor, models.DO_NOTHING)
#     avg_rating = models.FloatField(blank=True, null=True)
#     created = models.DateTimeField(blank=True, null=True)
#     updated = models.DateTimeField(blank=True, null=True)
#     n_of_rates = models.IntegerField(blank=True, null=True)


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


# class Rating(models.Model):
#     id = models.IntegerField(primary_key=True)
#     value = models.FloatField(blank=True, null=True)
#     user = models.CharField(max_length=45, blank=True, null=True)
#     movie = models.ForeignKey(Movie, models.DO_NOTHING)
