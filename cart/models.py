from django.db import models
from products.models import Product
from users.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"Cart for {self.user.username}"
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.prod_name} (x{self.quantity}) in Cart {self.cart.id}"