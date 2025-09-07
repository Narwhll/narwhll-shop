from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=10)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name