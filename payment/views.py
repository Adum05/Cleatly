from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from .models import Orders, Payment
from django.contrib.auth.models import User
from django.utils.timezone import now

class PaymentView(View):
    def get(self, request, order_id):
        order = get_object_or_404(Orders, id=order_id)
        return render(request, 'payment.html', {'order': order})

    def post(self, request, order_id):
        order = get_object_or_404(Orders, id=order_id)
        method = request.POST.get('method')
        Payment.objects.create(
            order=order,
            method=method,
            status='Pending',
            payment_date=now()
        )
        order.completed = True
        order.save()
        return redirect('order_detail', pk=order.pk)