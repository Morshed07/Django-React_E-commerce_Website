from django.db import models
from autoslug import AutoSlugField
from apps.categories.models import Category
# Create your models here.

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',on_delete=models.CASCADE)
    title = models.CharField(max_length=250,unique = True)
    slug = AutoSlugField(populate_from='title', max_length=250)
    featured = models.BooleanField(default=False)
    price = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField()
    description = models.TextField(null=True,blank=True,default='N/A')
    in_stock = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.title