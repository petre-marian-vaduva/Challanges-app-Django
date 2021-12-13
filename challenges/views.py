from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

dict_months = {'january': 'Eat not meat for the entire month!',
               'february': 'Walk for at least 20 min every day!',
               'march': 'Learn Django for 20 min'}

def monthly_challenges_by_number(request, month):
    months_numbers = list(dict_months.keys())
    forward_month = months_numbers[month-1]
    return HttpResponse(forward_month)



def monthly_challenges(request, month):
    try:
        my_guess = dict_months[month]
        return HttpResponse(my_guess)
    except:
        return HttpResponse('Invalid input')

