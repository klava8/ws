from django.urls import path
from .views import *

urlpatterns = [
    path('', FishListView.as_view(), name='list'),
    path('detail/<int:pk>/', FishDetailView.as_view(), name='detail')
]