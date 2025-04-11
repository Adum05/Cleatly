from django.db import models
from products.models import Product
from users.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default= False)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits= 10, decimal_places= 2)

    def __str__(self):
        return f"{self.product.prod_name} (x{self.quantity}) in Order {self.order.id}"

