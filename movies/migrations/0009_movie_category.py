# Generated by Django 4.1.5 on 2023-01-17 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_remove_movie_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('Action', 'Action'), ('Drama', 'Drama'), ('Comedy', 'Comedy')], default='Action', max_length=20),
        ),
    ]
