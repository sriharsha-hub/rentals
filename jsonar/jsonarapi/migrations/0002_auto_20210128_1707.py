# Generated by Django 3.1.2 on 2021-01-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsonarapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='films',
            name='actors',
        ),
        migrations.AlterField(
            model_name='payment',
            name='Amount',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
