# Generated by Django 2.1.5 on 2020-04-26 05:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 26, 5, 27, 36, 520680), verbose_name='date published'),
        ),
    ]
