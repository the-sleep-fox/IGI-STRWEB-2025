from django.shortcuts import render


# Create your views here.
def create_review(request):
    return render(request, 'reviews/create_review.html')