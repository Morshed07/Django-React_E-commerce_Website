from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['-id']

    def __str__(self) -> str:
        return self.title