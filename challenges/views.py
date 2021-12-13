from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

dict_months = {'january': 'Eat not meat for the entire month!',
               'february': 'Walk for at least 20 min every day!',
               'march': 'Learn Django for 20 min'}

def monthly_challenges_by_number(request, month):
    months_numbers = list(dict_months.keys())
    forward_month = months_numbers[month-1]
    redirect_path = reverse('monthly-challenge', args=[forward_month])
    return HttpResponseRedirect(redirect_path)



def monthly_challenges(request, month):
    try:
        my_guess = dict_months[month]
        response_data = f'<h1>{my_guess}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponse('Invalid input')

