# Generated by Django 2.2.7 on 2019-11-21 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0004_auto_20191121_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creación'),
        ),
    ]
