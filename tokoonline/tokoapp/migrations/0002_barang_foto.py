# Generated by Django 3.0 on 2019-12-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='barang',
            name='foto',
            field=models.CharField(default='', max_length=200),
        ),
    ]
