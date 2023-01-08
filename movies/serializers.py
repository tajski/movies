from rest_framework import serializers
from .models import Director, Actor


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'surname']


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ['id', 'name', 'surname']
