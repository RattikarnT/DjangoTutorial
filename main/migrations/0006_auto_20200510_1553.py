# Generated by Django 2.1.5 on 2020-05-10 08:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200510_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 15, 53, 54, 144400), verbose_name='date published'),
        ),
    ]
