from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=32)


class Category(models.Model):
    category_name = models.CharField(max_length=64)


class Product(models.Model):
    product_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_price = models.PositiveSmallIntegerField()
    product_quantity = models.CharField(max_length=36, null=True, blank=True, verbose_name='Количество предметов в упаковке:')
    composition = models.TextField(null=True, blank=True, verbose_name='Состав:')
    action = models.TextField(null=True, blank=True, verbose_name='Действие:')
    expiration_date = models.CharField(max_length=36, null=True, blank=True, verbose_name='Срок годности:')
    package_contents = models.TextField(null=True, blank=True, verbose_name='Комплектация:')
    product_image = models.ImageField(upload_to='product_images/')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='')
    client = models.ForeignKey(UserProfile, related_name='client_review', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
