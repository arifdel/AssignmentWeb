from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcat = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

        
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcat = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)
    product = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
