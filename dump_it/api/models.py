from django.db import models

class Brands(models.Model):
    name = models.CharField
    brand_image = models.CharField
    
class Categories(models.Model):
    name = models.CharField
    image = models.CharField
    
class Products(models.Model):
    name = models.CharField
    sku = models.CharField
    price = models.FloatField
    sale_price = models.FloatField
    short_description = models.TextField
    description = models.TextField
    Brands = models.ForeignKey(Brands, on_delete=models.CASCADE)
    Categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.TextField