# Generated by Django 4.0.4 on 2024-05-19 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBSITE', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='estado',
            field=models.IntegerField(default=0),
        ),
    ]
