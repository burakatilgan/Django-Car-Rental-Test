# Generated by Django 3.2.4 on 2021-07-02 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20210702_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='price',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='days',
            field=models.IntegerField(blank=True),
        ),
    ]
