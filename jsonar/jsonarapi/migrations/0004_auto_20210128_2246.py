# Generated by Django 3.1.5 on 2021-01-28 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jsonarapi', '0003_films_actors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='films',
            old_name='Actors',
            new_name='actors',
        ),
    ]
