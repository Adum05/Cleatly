from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from .models import Product, Review
from django.contrib.auth.models import User
from django.utils.timezone import now

class ReviewListView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        reviews = Review.objects.filter(product=product)
        return render(request, 'review_list.html', {'product': product, 'reviews': reviews})


class AddReviewView(View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        rating = int(request.POST.get('rating'))
        comment = request.POST.get('comment')
        Review.objects.create(
            product=product,
            user=request.user,
            rating=rating,
            comment=comment,
            date_created=now()
        )
        return redirect('product_detail', pk=product_id)