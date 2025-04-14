from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from .models import Orders, OrderItems
from django.contrib.auth.models import User
from django.utils.timezone import now

def user_orders_api(request):
    orders = Orders.objects.filter(user=request.user)
    data = [
        {
            'id': order.id,
            'date': order.date,
            'completed': order.completed,
            'total_price': sum(item.unit_price * item.quantity for item in OrderItems.objects.filter(order=order))
        }
        for order in orders
    ]
    return JsonResponse({'orders': data})