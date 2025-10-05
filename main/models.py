import uuid
from django.db import models
from django.contrib.auth.models import User
import locale
locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

# Create your models here.
class Product(models.Model):
    PILIHAN = [
        ('Running', 'Running Shoes'),
        ('Indoor', 'Indoor Shoes'),
        ('Football', 'Football Shoes'),
        ('Match Ball', 'Match Ball'),
        ('Misc', 'Miscellaneous'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.PositiveIntegerField()
    description = models.TextField()
    thumbnail = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=10, choices=PILIHAN)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def in_rupiah(self):
        formatted = f"Rp{self.price:,.0f}".replace(",", ".")
        return formatted
    
# class Employee(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.PositiveIntegerField(default=0)
#     persona = models.TextField()
