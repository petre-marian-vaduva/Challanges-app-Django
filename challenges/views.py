from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

dict_months = {'january': 'Eat not meat for the entire month!',
               'february': 'Walk for at least 20 min every day!',
               'march': 'Learn Django for 20 min',
               'april': 'Walk for at least 20 min every day!',
               'may': 'Learn Django for 20 min',
               'june': 'Eat not meat for the entire month!',
               'july': 'Learn Django for 20 min',
               'september': 'Walk for at least 20 min every day!',
               'october': 'Learn Django for 20 min',
               'november': 'Walk for at least 20 min every day!',
               'december': 'Eat not meat for the entire month!'}

def index(request):
    str_result = ''
    dict_keys = list(dict_months.keys())
    for key in dict_keys:
        path_dict = reverse('monthly-challenge', args=[key])
        str_result += f'<li><a href="{path_dict}">{key.capitalize()}</a></li>'
    return HttpResponse(f'<ol>{str_result}</ol>')





def monthly_challenges_by_number(request, month):
    months_numbers = list(dict_months.keys())
    forward_month = months_numbers[month-1]
    redirect_path = reverse('monthly-challenge', args=[forward_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        my_month = f'<h1>{dict_months[month]}</h1>'
        return HttpResponse(my_month)
    except:
        return HttpResponse('Invalid input')

