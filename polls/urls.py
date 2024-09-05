from .views import categorylist, Categorydetails
from django.urls import path

urlpatterns = [
    path('categorylist/', categorylist.as_view()),
    path('categorydetails/<int:pk>/', Categorydetails.as_view()),

]