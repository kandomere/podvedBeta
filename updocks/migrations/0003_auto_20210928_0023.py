# Generated by Django 3.2.7 on 2021-09-27 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updocks', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_add',
            field=models.DateField(default=datetime.date(2021, 9, 28), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_end',
            field=models.DateField(default=datetime.date(2022, 9, 28), verbose_name='Дата конца'),
        ),
    ]