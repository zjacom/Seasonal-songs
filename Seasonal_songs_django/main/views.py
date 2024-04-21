from django.shortcuts import render
from .models import *
from collections import defaultdict, OrderedDict
from django.http import JsonResponse
from .graph import *
import json

# Create your views here.
def parse_data_for_table(chart, year_):
    dic = defaultdict(list)
    for instance in chart:
        years_str = instance.years.strip("[]")
        years_list = years_str.split(",")

        for year in years_list:
            if year.strip() == year_:
                dic[instance.title] = instance.singer
    return dic


def index(request) :
    graph_html,appearances =chart_view(2023, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2023")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/spring/base_child.html',context)

def winter(request) :
    graph_html,appearances =chart_view(2023, 1)
    dic = parse_data_for_table(Winter_Modal_chart.objects.all(), "2023")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/winter/winter_child.html',context)

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
            if year.strip() == "2010" or year.strip() == "2011":
                continue
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
        for i in range(len(years_list)):
            years_list[i] = years_list[i].strip()
        while "2010" in years_list:
            years_list.remove("2010")
        while "2011" in years_list:
            years_list.remove("2011")
        dic[instance.title] = len(years_list)
    
    sorted_dict = OrderedDict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    # 상위 3개 항목 추출
    top_3_items = dict(list(sorted_dict.items())[:3])
    return JsonResponse(top_3_items, safe=False)

def exam2(request):
    this_year = 2021
    this_season = 0
    graph_html,appearances = chart_view(this_year, this_season)
    this_spring_list = All_chart.objects.filter(year=this_year, season=this_season)
    data_list = list(this_spring_list.values( 'title','singer'))
        
    return render(request, 'exam2.html',{'graph_html': graph_html, 'appearances': appearances})

def twelve(request):
    graph_html,appearances =chart_view(2012, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2012")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/spring/base_child.html',context)

def thirteen(request):
    graph_html,appearances =chart_view(2013, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2013")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/spring/base_child.html',context)

def fourteen(request):
    graph_html,appearances =chart_view(2014, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2014")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/spring/base_child.html',context)

def fifteen(request):    
    graph_html,appearances =chart_view(2015, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2015")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/spring/base_child.html',context)

def sixteen(request):
    graph_html,appearances =chart_view(2016, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2016")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/spring/base_child.html',context)

def seventeen(request):
    graph_html,appearances =chart_view(2017, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2017")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/spring/base_child.html',context)

def eighteen(request):
    graph_html,appearances =chart_view(2018, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2018")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/spring/base_child.html',context)

def nineteen(request):
    graph_html,appearances =chart_view(2019, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2019")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/spring/base_child.html',context)

def twenty(request) :
    graph_html,appearances =chart_view(2020, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2020")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/spring/base_child.html',context)

def twentyone(request) :
    graph_html,appearances =chart_view(2021, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2021")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/spring/base_child.html',context)

def twentytwo(request) :
    graph_html,appearances =chart_view(2022, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2022")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/spring/base_child.html',context)

def twentythree(request) :
    graph_html,appearances =chart_view(2023, 0)
    dic = parse_data_for_table(Spring_Modal_chart.objects.all(), "2023")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/spring/base_child.html',context)



def twelve_w(request):
    graph_html,appearances =chart_view(2012, 1)
    dic = parse_data_for_table(Winter_Modal_chart.objects.all(), "2012")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/winter/winter_child.html',context)

def thirteen_w(request):
    graph_html,appearances =chart_view(2013, 1)
    dic = parse_data_for_table(Winter_Modal_chart.objects.all(), "2013")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/winter/winter_child.html',context)

def fourteen_w(request):
    graph_html,appearances =chart_view(2014, 1)
    dic = parse_data_for_table(Winter_Modal_chart.objects.all(), "2014")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/winter/winter_child.html',context)

def fifteen_w(request):
    graph_html,appearances =chart_view(2015, 1)
    dic = parse_data_for_table(Winter_Modal_chart.objects.all(), "2015")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/winter/winter_child.html',context)

def sixteen_w(request):
    graph_html,appearances =chart_view(2016, 1)
    dic = parse_data_for_table(Winter_Modal_chart.objects.all(), "2016")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/winter/winter_child.html',context)

def seventeen_w(request):
    graph_html,appearances =chart_view(2017, 1)
    dic = parse_data_for_table(Winter_Modal_chart.objects.all(), "2017")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/winter/winter_child.html',context)

def eighteen_w(request):
    graph_html,appearances =chart_view(2018, 1)
    dic = parse_data_for_table(Winter_Modal_chart.objects.all(), "2018")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/winter/winter_child.html',context)

def nineteen_w(request):
    graph_html,appearances =chart_view(2019, 1)
    dic = parse_data_for_table(Winter_Modal_chart.objects.all(), "2019")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/winter/winter_child.html',context)

def twenty_w(request) :
    graph_html,appearances =chart_view(2020, 1)
    dic = parse_data_for_table(Winter_Modal_chart.objects.all(), "2020")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/winter/winter_child.html',context)

def twentyone_w(request) :
    graph_html,appearances =chart_view(2021, 1)
    dic = parse_data_for_table(Winter_Modal_chart.objects.all(), "2021")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/winter/winter_child.html',context)

def twentytwo_w(request) :
    graph_html,appearances =chart_view(2022, 1)
    dic = parse_data_for_table(Winter_Modal_chart.objects.all(), "2022")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/winter/winter_child.html',context)

def twentythree_w(request) :
    graph_html,appearances =chart_view(2023, 1)
    dic = parse_data_for_table(Winter_Modal_chart.objects.all(), "2023")
    context = { 'graph_html':graph_html,'dic' : dict(dic),'appearances': appearances }
    return render(request, 'main/winter/winter_child.html',context)