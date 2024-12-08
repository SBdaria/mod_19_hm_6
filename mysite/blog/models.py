from django.db import models

class Products(models.Model):
    name_category = (
        ("jackets", "Куртки"),
        ("jeans", "Джинсы"),
        ("tshirts", "Футболки"),
        ("hoodies", "Худи"),
        ("shoes", "Кроссовки и кеды")
    )
    name = models.CharField(max_length=20)
    category = models.CharField(max_length=7, choices=name_category, default='tshirts')
    description = models.TextField()
    price = models.IntegerField()
    image_product = models.ImageField(upload_to='images_product/')
