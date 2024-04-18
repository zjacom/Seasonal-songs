from django.shortcuts import render
from .models import Modal_chart
from collections import defaultdict
from django.http import JsonResponse

# Create your views here.
def index(request) :
    return render(request, 'main/index.html')

def winter(request) :
    return render(request, 'main/winter.html')

def modal(request):
    data = Modal_chart.objects.all().values('title', 'year', 'chartin_counts')
    return JsonResponse(list(data), safe=False)



def twenty(request) :
    return render(request, 'main/spring/twenty.html')
def twentyone(request) :
    return render(request, 'main/spring/twentyone.html')
def twentytwo(request) :
    return render(request, 'main/spring/twentytwo.html')
def twentythree(request) :
    return render(request, 'main/spring/twentythree.html')


def twenty_w(request) :
    return render(request, 'main/winter/twenty_w.html')
def twentyone_w(request) :
    return render(request, 'main/winter/twentyone_w.html')
def twentytwo_w(request) :
    return render(request, 'main/winter/twentytwo_w.html')