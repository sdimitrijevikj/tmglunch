import xlrd

from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import F
from django.contrib.auth.decorators import login_required

from .models import Day, FoodItem


def index(request):
    days = Day.objects.all()
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

    return render(request, 'website/load.html', {})
