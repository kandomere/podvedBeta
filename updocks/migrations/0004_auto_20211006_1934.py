# Generated by Django 3.2.7 on 2021-10-06 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updocks', '0003_auto_20210928_0023'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='cover',
        ),
        migrations.AlterField(
            model_name='post',
            name='data_add',
            field=models.DateField(default=datetime.date(2021, 10, 6), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_end',
            field=models.DateField(default=datetime.date(2022, 10, 6), verbose_name='Дата конца'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Действителен'), ('draft', 'Срок вышел')], default='published', max_length=10, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ManyToManyField(to='updocks.FeedFile'),
        ),
    ]