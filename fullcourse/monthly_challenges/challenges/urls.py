from django.urls import path
from . import views

app_name = 'challenges'
urlpatterns = [
    path("", views.list_months, name="index"),
    path("<int:number>", views.monthly_challenge_by_number ),
    path("<str:month>", views.monthly_challenge, name="month_challenge")
]


