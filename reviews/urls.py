from django.urls import path
from reviews.views import review_list

urlpatterns = [
    path("", review_list, name='review_list')
]