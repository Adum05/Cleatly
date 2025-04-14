from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from .models import Product, Cart, CartItem, Orders, OrderItems
from django.contrib.auth.models import User
from django.utils.timezone import now

class CreateOrderView(View):
    def post(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        order = Orders.objects.create(user=request.user, date=now(), completed=False)
        cart_items = CartItem.objects.filter(cart=cart)
        for item in cart_items:
            OrderItems.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                unit_price=item.product.price,
            )
        cart_items.delete()  # Clear the cart after creating the order
        return redirect('order_detail', pk=order.pk)


class OrderDetailView(View):
    def get(self, request, pk):
        order = get_object_or_404(Orders, pk=pk)
        order_items = OrderItems.objects.filter(order=order)
        return render(request, 'order_detail.html', {'order': order, 'order_items': order_items})