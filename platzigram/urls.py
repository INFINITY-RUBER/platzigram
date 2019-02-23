
from django.urls import path
from platzigram import views



urlpatterns = [

    path('hello-word/', views.hello_world),
    path('sorted/', views.sort_intergers),
    path('hi/<str:name>/<int:age>/', views.say_hi),


]
