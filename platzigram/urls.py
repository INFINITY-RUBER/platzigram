
from django.urls import path
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('hola mundo por ruber hernadez')


urlpatterns = [

    path('hello-word/', hello_world)

]
