from django.db import models


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
    category = models.CharField(max_length=45, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actor = models.ManyToManyField(Actor)
    avg_rating = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)
    n_of_rates = models.IntegerField(blank=True, null=True)

    def count(self):
        number = Rating.objects.filter(movie = self)
        return len(number)

    def __str__(self):
        return self.title

class Rating(models.Model):
    value = models.FloatField(blank=True, null=True)
    user = models.CharField(max_length=45, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.user + ': ' + self.movie + ' (' + self.value + ")"
