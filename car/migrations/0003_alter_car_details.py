# Generated by Django 3.2.4 on 2021-06-22 21:09

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_car_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='details',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]