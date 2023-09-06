from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
from django.db.models import Avg
# Create your views here.

class ListBookView(ListView):
    model = Book
    template_name = "book_outlet/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = context['object_list'].count()
        context["avg_rating"] = context['object_list'].aggregate(Avg('rating'))
        return context

class DetailBookView(DetailView):
    model = Book
    template_name = "book_outlet/book-detail.html"
    #pk_url_kwarg = "slug"

