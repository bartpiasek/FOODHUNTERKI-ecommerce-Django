# Generated by Django 3.0.8 on 2020-08-14 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhblog', '0005_post_snippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_thumbnail_image',
            field=models.ImageField(blank=True, height_field=200, null=True, upload_to='images/fhblog', width_field=200),
        ),
    ]
