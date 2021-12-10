from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def monthly_challenges(request, month):
    temp = None
    if month == 'january':
        temp = 'Eat not meat for the entire month!'
    elif month == 'february':
        temp = 'Walk for at least 20 min every day!'
    else:
        temp = 'Nothing'
    return HttpResponse(temp)

