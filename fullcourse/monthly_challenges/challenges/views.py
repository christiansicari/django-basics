from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
import calendar
from django.template.loader import render_to_string

challenges = {}
for month in list(calendar.month_name)[1:]:
    challenges[month] = f"Some challenge of {month}"


print(challenges)

# Create your views here.
def index(request):
    return HttpResponse("It works!")


def monthly_challenge(request, month):
    if month != "" and month.capitalize() in list(calendar.month_name):
       return render(request, 'challenges/challenge.html', {'month': month, 'challenge': challenges[month]})
    else: 
        raise Http404()


def monthly_challenge_by_number(request, number):
    if  0 < number <= 12:
        url = reverse('challenges:month_challenge', args=(calendar.month_name[number], ))
        return HttpResponseRedirect(url)
    else:
        raise Http404()
    
def list_months(request):
    return render(request, "challenges/index.html", context={"months": challenges})
