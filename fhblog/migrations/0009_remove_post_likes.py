# Generated by Django 3.0.8 on 2020-08-15 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fhblog', '0008_auto_20200814_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
