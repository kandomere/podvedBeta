# Generated by Django 3.2.7 on 2021-10-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updocks', '0005_auto_20211006_1939'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FeedFile',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cover2',
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.FileField(upload_to='images/', verbose_name='Документы'),
        ),
    ]