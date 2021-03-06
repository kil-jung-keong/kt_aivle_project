# Generated by Django 4.0.1 on 2022-01-25 08:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_movie_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FileField(null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
