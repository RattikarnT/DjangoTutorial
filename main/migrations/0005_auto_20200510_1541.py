# Generated by Django 2.1.5 on 2020-05-10 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200510_1500'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_image',
            field=models.ImageField(default='djangopony.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 15, 41, 56, 70986), verbose_name='date published'),
        ),
    ]