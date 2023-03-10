# Generated by Django 4.1.5 on 2023-01-07 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=45, null=True)),
                ('category', models.CharField(blank=True, max_length=45, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('avg_rating', models.FloatField(blank=True, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('n_of_rates', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
