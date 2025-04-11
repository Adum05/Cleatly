from django.db import models
from products.models import Product
from users.models import User

class Review(models.Model):
    RATE_CHOICES = [
        ('1', 'Poor'),
        ('2', 'Bad'),
        ('3', 'Decent'),
        ('4', 'Good'),
        ('5', 'Excellent')
    ]

    product = models.ForeignKey(Product, on_delete= models.CASCADE, related_name= 'reviews')
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    rating = models.IntegerField(choices=RATE_CHOICES)
    comments = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {self.product.prod_name} ({self.rating})"
    
    
