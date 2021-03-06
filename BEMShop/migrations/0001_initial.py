# Generated by Django 2.1.7 on 2019-03-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Please enter your name here...', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(default='Please enter your subject here...', max_length=200)),
                ('message', models.TextField(default='Please enter your message here...', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(blank=True, default='uploaded_media/None/No-image.jpg', null=True, upload_to='uploaded_media')),
                ('title', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=300)),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
