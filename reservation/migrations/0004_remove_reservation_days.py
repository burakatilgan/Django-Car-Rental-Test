# Generated by Django 3.2.4 on 2021-07-02 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20210702_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='days',
        ),
    ]