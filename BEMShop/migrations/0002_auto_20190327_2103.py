# Generated by Django 2.1.7 on 2019-03-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BEMShop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(max_length=200),
        ),
    ]