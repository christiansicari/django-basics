from typing import Any, Dict
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

from .models import Post

class PostListView(ListView):
    model = Post
    context_object_name = 'all_posts'
    template_name = 'blog/all-posts.html'
    ordering = ['-date']


class PostTopListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'
    ordering = ['date']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if len(context['posts']) > 3:
            context['posts'] = context['posts'][len(context['posts'])-3:]
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'
        