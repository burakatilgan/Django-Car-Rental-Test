# Generated by Django 3.2.4 on 2021-07-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_setting_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
