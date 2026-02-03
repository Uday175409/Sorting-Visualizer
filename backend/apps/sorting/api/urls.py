from django.urls import path
from .views import SortView

urlpatterns = [
    path('sort/', SortView.as_view(), name='sort'),
]
