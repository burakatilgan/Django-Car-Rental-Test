# Generated by Django 3.2.4 on 2021-07-02 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0013_auto_20210629_0340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
