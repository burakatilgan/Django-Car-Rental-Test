# Generated by Django 3.2.4 on 2021-07-02 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210702_0702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='address',
        ),
    ]
