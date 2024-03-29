# Generated by Django 3.2.4 on 2021-06-25 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_alter_car_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='car',
            name='keyword',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='stock',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
