from django.shortcuts import render
from reviews.models import Review

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()

    context = {
        "review_list": reviews
    }

    return render(request, "index.html", context=context)