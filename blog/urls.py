from django.urls import path
from django.contrib import admin
from .views import HomePage , BlogDetailView

urlpatterns = [
    path('' , HomePage.as_view() , name='home'),
    path('post/<int:pk>/' , BlogDetailView.as_view() , name='post_detail')
]