# Generated by Django 3.2.4 on 2021-07-02 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_reservation_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='days',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='reservation',
            name='price',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='reservation',
            name='total',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
