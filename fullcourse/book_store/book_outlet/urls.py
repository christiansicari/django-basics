from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ListBookView.as_view(), name="list-books"),
    path("<slug:slug>/", views.DetailBookView.as_view(), name="detail-book")

]
