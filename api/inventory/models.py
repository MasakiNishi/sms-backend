from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product Name')
    price = models.IntegerField(verbose_name='Product Price')
    description = models.TextField(verbose_name='Product Description', null=True, blank=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
