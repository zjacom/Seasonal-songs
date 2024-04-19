from django.shortcuts import render
from .models import *
from collections import defaultdict, OrderedDict
from django.http import JsonResponse
from .graph import *
import json

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

def exam2(request):
    this_year = 2012
    this_season = 0
    graph_html = chart_view(this_year, this_season)
    this_spring_list = All_chart.objects.filter(year=this_year, season=this_season)
    data_list = list(this_spring_list.values( 'title','singer'))
    
    return render(request, 'exam2.html',{'graph_html': graph_html})

def twelve(request):
    graph_html =chart_view(2012, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2012")
    context = { 'graph_html':graph_html, 'dic' : dict(dic)}        
    
    return render(request, 'main/spring/year_2012.html',context)

def thirteen(request):
    graph_html = chart_view(2013, 0)    
    return render(request, 'main/spring/year_2013.html' ,{'graph_html': graph_html})

def fourteen(request):
    graph_html = chart_view(2014, 0)    
    return render(request, 'main/spring/year_2014.html',{'graph_html': graph_html})

def fifteen(request):
    graph_html = chart_view(2015, 0)    
    
    return render(request, 'main/spring/year_2015.html',{'graph_html': graph_html})

def sixteen(request):
    graph_html = chart_view(2016, 0)    
    return render(request, 'main/spring/year_2016.html',{'graph_html': graph_html})

def seventeen(request):
    graph_html = chart_view(2017, 0)    
    return render(request, 'main/spring/year_2017.html',{'graph_html': graph_html})

def eighteen(request):
    graph_html = chart_view(2018, 0)    
    return render(request, 'main/spring/year_2018.html',{'graph_html': graph_html})

def nineteen(request):
    graph_html = chart_view(2019, 0)    
    return render(request, 'main/spring/year_2019.html',{'graph_html': graph_html})

def twenty(request) :
    graph_html = chart_view(2020, 0)    
    return render(request, 'main/spring/year_2020.html',{'graph_html': graph_html})

def twentyone(request) :
    graph_html = chart_view(2021, 0)    
    return render(request, 'main/spring/year_2021.html',{'graph_html': graph_html})

def twentytwo(request) :
    graph_html = chart_view(2022, 0)    
    return render(request, 'main/spring/year_2022.html',{'graph_html': graph_html})

def twentythree(request) :
    graph_html = chart_view(2023, 0)    
    return render(request, 'main/spring/year_2023.html',{'graph_html': graph_html})



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