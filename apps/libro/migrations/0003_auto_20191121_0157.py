# Generated by Django 2.2.7 on 2019-11-21 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_auto_20191121_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.Autor'),
        ),
    ]
