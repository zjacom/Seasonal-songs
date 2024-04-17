from django.shortcuts import render

# Create your views here.
def index(request) :
    return render(request, 'main/index.html')

def winter(request) :
    return render(request, 'main/winter.html')



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