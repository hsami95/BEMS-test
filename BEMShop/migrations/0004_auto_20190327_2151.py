# Generated by Django 2.1.7 on 2019-03-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BEMShop', '0003_auto_20190327_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('web', 'Android'), ('app', 'Iphone'), ('card', 'Accessories')], max_length=1),
        ),
    ]
