from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>/", views.show, name="show"),
    path("", views.index, name="index")
]