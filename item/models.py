from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
#     slug = models.SlugField()

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
class Item(models.Model):
     category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
     name = models.CharField(max_length=255)
     description = models.TextField(blank=True, null=True)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     image = models.ImageField(upload_to='item_images', blank=True, null=True)
     is_sold = models.BooleanField(default=False)
     created_at = models.DateTimeField(auto_now_add=True)
     created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
     def __str__(self):
        return self.name
