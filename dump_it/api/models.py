from django.db import models

class Brands(models.Model):
    name = models.CharField(max_length=255)
    brand_image = models.CharField(max_length=255)
    
class Categories(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    
class Products(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    price = models.FloatField(max_length=255)
    sale_price = models.FloatField(default=0)
    short_description = models.TextField()
    description = models.TextField()
    Brands = models.ForeignKey(Brands, on_delete=models.CASCADE)
    Categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.CharField(max_length=255)