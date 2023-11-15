from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat.html')
def shreyas(request):
    return HttpResponse('<h1>shreyas scored his 2nd hundred in world cup</h1>')
