# Generated by Django 4.1.5 on 2023-01-08 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_remove_movie_avg_rating_alter_movie_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='n_of_rates',
        ),
    ]