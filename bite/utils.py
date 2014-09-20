import json
import decimal
from django.http import HttpResponse
from datetime import date, datetime


def json_result(result, request=None):
    response = {
        'error': None,
        'result': result,
    }
    return HttpResponse(content=json.dumps(response, default=json_handler),
                        content_type='application/json')


def json_handler(x):
    if isinstance(x, date) or isinstance(x, datetime):
        return x.isoformat()
    elif isinstance(x, decimal.Decimal):
        return float(x)
    else:
        return None


def json_error(code, request=None, arg1=None):
    message_list = {
        -1: "Unknown error.",
        0:  "",
        1:  "Argument missing. '%s' is a required argument." % arg1,
        2:  "'%s' is not valid." % arg1,
    }

    response = {
        'error': {
            'code': code,
            'message': message_list[code]
        },
        'result': None,
    }

    return HttpResponse(content=json.dumps(response),
                        content_type='application/json')