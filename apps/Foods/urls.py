from django.urls import path
from apps.Foods.views import index
urlpatterns = [
    path('',index),
]