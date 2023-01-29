from django.shortcuts import render
from django.http import JsonResponse
from .models import Trades, Test
from .management.commands import stocks


# Create your views here.


def index(request):
    # _trade = Test.objects.all()
    stocks.test()

    return JsonResponse({"trades": [
        # t.to_json() for t in _trade
    ]})
