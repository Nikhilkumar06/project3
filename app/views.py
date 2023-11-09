from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nikhil(request):
    return HttpResponse('<h1><marquee>Hey Divya I have huge crush on you and you just got into my heart and nerves</h1></marquee>')

def divya(request):
    return HttpResponse('<h1><marquee>but i need some time</h1></marquee>')

