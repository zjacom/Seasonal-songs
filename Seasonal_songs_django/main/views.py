from django.shortcuts import render
from .models import *
from collections import defaultdict, OrderedDict
from django.http import JsonResponse

# Create your views here.
def index(request) :
    return render(request, 'main/index.html')

def winter(request) :
    return render(request, 'main/winter.html')

def base(request) : 
    return render(request, 'base.html')

def exam(request) : 
    return render(request, 'exam.html')

# 봄에 차트인 한 노래 개수를 딕셔너리 형태로 전송
def spring_modal(request):
    dic = defaultdict(int)

    modal_chart = Spring_Modal_chart.objects.all()

    for instance in modal_chart:
        years_str = instance.years.strip("[]")
        years_list = years_str.split(",")

        for year in years_list:
            dic[year.strip()] += 1
    return JsonResponse(dic, safe=False)

# 겨울에 차트인 한 노래 개수를 딕셔너리 형태로 전송
def winter_modal(request):
    dic = defaultdict(int)

    modal_chart = Winter_Modal_chart.objects.all()

    for instance in modal_chart:
        years_str = instance.years.strip("[]")
        years_list = years_str.split(",")

        for year in years_list:
            dic[year.strip()] += 1
    return JsonResponse(dic, safe=False)

# 봄 명예의 전당
def spring_hall_of_frame(request):
    dic = defaultdict(int)

    modal_chart = Spring_Modal_chart.objects.all()

    for instance in modal_chart:
        years_str = instance.years.strip("[]")
        years_list = years_str.split(",")
        dic[instance.title] = len(years_list)
    
    sorted_dict = OrderedDict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    # 상위 3개 항목 추출
    top_3_items = dict(list(sorted_dict.items())[:3])
    return JsonResponse(top_3_items, safe=False)

# 겨울 명예의 전당
def winter_hall_of_frame(request):
    dic = defaultdict(int)

    modal_chart = Winter_Modal_chart.objects.all()

    for instance in modal_chart:
        years_str = instance.years.strip("[]")
        years_list = years_str.split(",")
        dic[instance.title] = len(years_list)
    
    sorted_dict = OrderedDict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    # 상위 3개 항목 추출
    top_3_items = dict(list(sorted_dict.items())[:3])
    return JsonResponse(top_3_items, safe=False)

def twelve(request):
    return render(request, 'main/spring/year_2012.html')
def thirteen(request):
    return render(request, 'main/spring/year_2013.html')
def fourteen(request):
    return render(request, 'main/spring/year_2014.html')
def fifteen(request):
    return render(request, 'main/spring/year_2015.html')
def sixteen(request):
    return render(request, 'main/spring/year_2016.html')
def seventeen(request):
    return render(request, 'main/spring/year_2017.html')
def eighteen(request):
    return render(request, 'main/spring/year_2018.html')
def nineteen(request):
    return render(request, 'main/spring/year_2019.html')
def twenty(request) :
    return render(request, 'main/spring/year_2020.html')
def twentyone(request) :
    return render(request, 'main/spring/year_2021.html')
def twentytwo(request) :
    return render(request, 'main/spring/year_2022.html')
def twentythree(request) :
    return render(request, 'main/spring/year_2023.html')


def twelve_w(request):
    return render(request, 'main/winter/twelve_w.html')
def thirteen_w(request):
    return render(request, 'main/winter/thirteen_w.html')
def fourteen_w(request):
    return render(request, 'main/winter/fourteen_w.html')
def fifteen_w(request):
    return render(request, 'main/winter/fifteen_w.html')
def sixteen_w(request):
    return render(request, 'main/winter/sixteen_w.html')
def seventeen_w(request):
    return render(request, 'main/winter/seventeen_w.html')
def eighteen_w(request):
    return render(request, 'main/winter/eighteen_w.html')
def nineteen_w(request):
    return render(request, 'main/winter/nineteen_w.html')
def twenty_w(request) :
    return render(request, 'main/winter/twenty_w.html')
def twentyone_w(request) :
    return render(request, 'main/winter/twentyone_w.html')
def twentytwo_w(request) :
    return render(request, 'main/winter/twentytwo_w.html')
def twentythree_w(request) :
    return render(request, 'main/winter/twentythree_w.html')