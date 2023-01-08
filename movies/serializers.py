from rest_framework import serializers
from .models import Director, Actor, Movie, Rating


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'surname']


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ['id', 'name', 'surname']


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'category', 'description', 'director', 'actor', 'avg_rating', 'created', 'updated', 'n_of_rates']


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ['id', 'value', 'user', 'movie']
