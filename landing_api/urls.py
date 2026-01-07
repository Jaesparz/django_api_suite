from django.urls import path
from . import views

urlpatterns = [
   path("index/", views.LandingAPI.as_view(), name="index"),
]