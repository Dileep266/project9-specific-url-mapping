from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def williamson(request):
    return render(request,'williamson.html')
def philips(request):
    return HttpResponse('<h1>best fielder</h1>')
