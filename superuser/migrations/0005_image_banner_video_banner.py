# Generated by Django 4.2.7 on 2023-12-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0004_rename_image_image_image_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='banner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='banner',
            field=models.BooleanField(default=False),
        ),
    ]