from django.db import models
from django.db.models.constraints import UniqueConstraint

class Category(models.Model):
    """ Product category model """

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_display_name(self):
        return self.display_name


class Subcategory(models.Model):
    """ Product subcategory model """
    name = models.CharField(max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.CASCADE
    )
    display_name = models.CharField(max_length=254, null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "Subcategories"
        # constraints = [
        #     UniqueConstraint(
        #         fields=['name', 'category'],
        #         name='unique_subcategory_per_category'
        #     )
        # ]
    
    def __str__(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name


class Product(models.Model):
    """ Products model """
    title = models.CharField(max_length=254)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL
    )
    subcategory = models.ForeignKey(
        'Subcategory', null=True, blank=True, on_delete=models.SET_NULL
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    sku = models.CharField(max_length=25, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    usage = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=25, null=True, blank=True)
    type = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, default=0
    )

    def __str__(self):
        return self.title
