from django.shortcuts import render
from .models import Review
# Create your views here.

def show_reviews(request, pk = None):
    if not pk:
        reviews = Review.objects.select_related('student')
        context = {
            'reviews' : reviews
        }
        template_ = 'show_reviews.html'
    return render(request, template_, context = context)


    