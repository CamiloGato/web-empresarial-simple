# Generated by Django 2.0.2 on 2019-12-27 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.SlugField(max_length=200, verbose_name='Red social'),
        ),
    ]
