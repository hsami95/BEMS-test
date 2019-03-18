# Generated by Django 2.1.5 on 2019-03-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BEMShop', '0005_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, default='uploaded_media/None/No-image.jpg', null=True, upload_to='uploaded_media')),
                ('product_title', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=10)),
            ],
        ),
    ]