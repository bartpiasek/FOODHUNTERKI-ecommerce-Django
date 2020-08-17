# Generated by Django 3.0.8 on 2020-08-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fhblog', '0007_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='instalink',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profilepicture',
            field=models.ImageField(blank=True, height_field=200, null=True, upload_to='images/fhblog/profiles', width_field=200),
        ),
    ]
