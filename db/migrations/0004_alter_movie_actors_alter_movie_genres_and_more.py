# Generated by Django 5.1.4 on 2024-12-30 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_movie_actors_alter_movie_genres_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='db.actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='db.genre'),
        ),
        migrations.AlterField(
            model_name='moviesession',
            name='cinema_hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='db.cinemahall'),
        ),
        migrations.AlterField(
            model_name='moviesession',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='db.movie'),
        ),
    ]
