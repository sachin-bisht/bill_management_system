from django.conf.urls import url
from django.urls import path
from .views import (
    bill_list,
    bill_detail,
    bill_new,
    bill_edit,
)

urlpatterns = [
    path('', bill_list, name='bill_list'),
    path('bill/<int:pk>/', bill_detail, name='bill_detail'),
    path('bill/new/', bill_new, name='bill_new'),
    path('bill/<int:pk>/edit/', bill_edit, name='bill_edit'),
]