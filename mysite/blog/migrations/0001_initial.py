# Generated by Django 5.1.4 on 2024-12-08 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.CharField(choices=[('jackets', 'Куртки'), ('jeans', 'Джинсы'), ('tshirts', 'Футболки'), ('hoodies', 'Худи'), ('shoes', 'Кроссовки и кеды')], default='tshirts', max_length=7)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('image_product', models.ImageField(upload_to='images_product/')),
            ],
        ),
    ]
