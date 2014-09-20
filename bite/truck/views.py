from django.shortcuts import render
from .models import Truck
from location.models import Location
from utils import json_result, json_error
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get(request):
    if (not 'id' in request.GET) and (not 'name' in request.GET):
        return json_error(1, arg1='id or name')
    try:
        res = Truck.objects.values('id', 'name', 'location_id', 'last_update', 'date_created')
        if 'id' in request.GET:
            result = res.get(id=request.GET['id'])
        else:
            result = res.get(name=request.GET['name'])

    except ObjectDoesNotExist:
        return json_error(2, arg1='id or name')

    return json_result(result)


@csrf_exempt
def add(request):

    if not 'name' in request.GET:
        return json_error(1, arg1='name')

    if not 'location_id' in request.GET:
        return json_error(1, arg1='location_id')

    try:
        location = Location.objects.get(id=int(request.GET['location_id']))
    except (ObjectDoesNotExist, ValueError, TypeError):
        return json_error(2, arg1='location')

    result = Truck.objects.create(name=request.GET['name'], location=location)

    return json_result(result.id)


def test(request):
    return json_result(True)

