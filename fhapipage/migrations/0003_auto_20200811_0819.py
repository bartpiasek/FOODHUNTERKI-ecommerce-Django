# Generated by Django 3.0.8 on 2020-08-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhapipage', '0002_auto_20200810_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeform',
            name='food',
            field=models.CharField(max_length=500),
        ),
    ]
