# Generated by Django 4.2 on 2023-04-25 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
    ]
