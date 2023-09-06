from django.urls import path
from . import views
app_name ="blog"

urlpatterns = [
    path("", views.PostTopListView.as_view(), name="starting-page"),
    path("posts", views.PostListView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="post-detail-page")
]