""" platzigram views."""
#Django
from django.http import HttpResponse
# utilidades
from datetime import datetime
import json

def hello_world(request):
    #now = datetime.now().strftime('%b %dht, %Y - %H:%M hrs')
    return HttpResponse('hola ruber! esta es la hora {now}'.format(
		now=datetime.now().strftime('%b - %d - %Y : %H:%M hrs')
	))


def sort_intergers(request):
    """ Resturn  a JSON response with """
    numbers = [ int(i) for i in request.GET["numbers"].split(",") ]
    sorted_ints = sorted(numbers)
    data = {
        'status': 'ok',
        'number': sorted_ints,
        'message': 'integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')


def say_hi(request, name, age):
    """Returana a greeting. """
    if age < 12:
        messege = 'Sorry  {},  you are not allowed hare'.format(name)
    else:
        messege = 'Hello Ruber  {}, Bienvenido '.format(name)
    return HttpResponse(messege)