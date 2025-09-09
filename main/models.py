import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jerseys', 'Jerseys'),
        ('boots', 'Football Boots'),
        ('training', 'Training Gear'),
        ('accessories', 'Accessories'),
        ('equipment', 'Equipment'),
        ('merchandise', 'Club Merchandise'),
        ('collectibles', 'Collectibles'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    @property
    def is_premium(self):
        return self.price > 1000

    def update_price(self, new_price):
        self.price = new_price
        self.save()