# Generated by Django 4.2.4 on 2023-08-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]
