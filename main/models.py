from django.db import models

# Create your models here.
class Product(models.Model):
    PILIHAN = [
        ('Running', 'Running Shoe'),
        ('Indoor', 'Indoor Shoe'),
        ('Football', 'Football Shoe'),
        ('Ball', 'Football'),
    ]

    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField()
    thumbnail = models.URLField(null=True, blank=True)
    category = models.CharField(max_length=10, choices=PILIHAN, default='Running')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name