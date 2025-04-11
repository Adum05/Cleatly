from django.db import models
from orders.models import Order

class Payment(models.Model):
    STATUS = [
        ('Pending', 'pending'),
        ('Compleyed', 'completed'),
        ('Failed', 'failed'),
    ]

    PAYMENT_CHOICES = [
        ('Card', 'card'),
        ('PayPal', 'paypal'),
        ('Apple Pay', 'apple pay'),
        ('Google Pay', 'goggle pay'),
    ]

    order = models.ForeignKey(Order, on_delete= models.CASCADE)
    method = models.CharField(max_length= 20, choices=PAYMENT_CHOICES,)
    status = models.CharField(max_length= 20, choices=STATUS)
    payment_date = models.DateTimeField()

    def __str__(self):
        return f"Payment for Order #{self.order.id} - {self.status}"

