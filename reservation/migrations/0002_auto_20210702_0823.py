# Generated by Django 3.2.4 on 2021-07-02 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='returntime',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reztime',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='slug',
        ),
    ]