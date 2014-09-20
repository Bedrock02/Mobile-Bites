from django.shortcuts import render
from utils import json_result, json_error
from .models import Location
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get(request):
    if not 'id' in request.GET:
        return json_error(1, arg1='id')
    try:
        result = Location.objects\
                         .values('id', 'longitude', 'latitude', 'last_update', 'date_created')\
                         .get(id=int(request.GET['id']))
    except (ObjectDoesNotExist, ValueError, TypeError):
        return json_error(2, arg1='id')

    return json_result(result)


@csrf_exempt
def add(request):

    if not 'longitude' in request.GET:
        return json_error(1, arg1='longitude')

    if not 'latitude' in request.GET:
        return json_error(1, arg1='latitude')
    #
    # defaults = request.GET
    # if 'id' in defaults:
    #     defaults.pop('id')
    # defaults.pop('longitude')
    # defaults.pop('latitude')

    result, created = Location.objects\
        .get_or_create(longitude=request.GET['longitude'], latitude=request.GET['latitude'])

    return json_result(result.id)


def test(request):
    return json_result(True)
