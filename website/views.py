from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from .models import FoodItem, MenuDocs
from .helpers import parse_lunch_menu_data


def index(request):
    days = []
    today = datetime.now()
    number_days = 7

    for x in range(0, number_days):
        day = today + timedelta(days=x)
        if day.isoweekday() < 6:
            days.append([day, FoodItem.objects.filter(date=day)])

    return render(request, 'website/home.html', {'days': days})


def vote(request):

    result = 'success'
    try:
        FoodItem.objects.filter(id=request.GET.get('item_id')).update(votes=F('votes') + 1)
    except:
        result = 'failed'

    return JsonResponse({'result': result}, safe=False)


@csrf_protect
@login_required(redirect_field_name='/')
def upload_data(request):
    message = {}

    if request.method == 'POST':
        try:
            document = MenuDocs(date_from=request.POST.get('date_from'), file=request.FILES['file'])
            document.save()

        except Exception as e:
            raise e

        try:
            parse_lunch_menu_data('website/docs/' + document.file.name, document.date_from)
            message['text'] = 'Menu items uploaded successfully!'
            message['type'] = 'success'
        except:
            message['text'] = 'There was an error uploading the data, please fix the excel sheet and try again.'
            message['type'] = 'error'

    return render(request, 'website/load.html', {'message': message})


