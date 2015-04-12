from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import F
from django.contrib.auth.decorators import login_required

from .models import FoodItem
from .helpers import parse_lunch_menu_data


def index(request):
    days = []
    today = datetime.now()
    number_days = 7

    for x in range(0, number_days):
        day = datetime(today.year, today.month, today.day + x, 0, 0, 0)
        if day.isoweekday() < 6:
            days.append([day, FoodItem.objects.filter(date=day)])

    return render(request, 'website/home.html', {'days': days})


def vote(request):

    result = 'success'
    try:
        FoodItem.objects.filter(id=request.GET.get('item_id')).update(votes=F('votes') + 1)
    except Exception as e:
        result = 'failed'

    return JsonResponse({'result': result}, safe=False)


@login_required(redirect_field_name='/')
def upload_data(request):
    #parse_lunch_menu_data('website/docs/menu16.xls', '2015/4/13')
    return render(request, 'website/load.html', {})
