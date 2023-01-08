from django.contrib import admin
from .models import Actor, Director, Movie, Rating

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Rating)