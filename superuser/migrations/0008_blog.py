# Generated by Django 5.0.1 on 2024-01-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0007_image_heading_image_subheading'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_file', models.ImageField(default='', null=True, upload_to='blog-uploads/')),
                ('heading', models.CharField(default='', max_length=100, null=True)),
                ('subheading', models.CharField(default='', max_length=100, null=True)),
                ('body', models.CharField(default='', max_length=500, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]