from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.


def index(request):
    return JsonResponse({"user": [
        {"id": 1, "name": "taro"},
        {"id": 2, "name": "jiro"}
    ]})
