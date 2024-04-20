from .models import *
import plotly.graph_objects as go
import plotly.io as pio
from itertools import groupby
from django.db.models import Min, Max
import datetime
from collections import defaultdict, OrderedDict
import pandas as pd
# 날짜 형식 변환 함수
def format_date(date):
    # 'date'는 datetime 객체이어야 합니다.
    return date.strftime('%#m월 %#d일')

def chart_view(year_is, season_is):
    # 데이터베이스에서 주어진 연도와 시즌의 데이터 필터링 및 정렬
    data = All_chart.objects.filter(year=year_is, season=season_is).order_by('date','title' )
    query = data.values()
    data_list = list(query)
    starting_day = query.first()['date']
    starting_month = query.first()['month']
    starting_week = query.first()['week']
    ending_month = query.last()['month']    
    ending_week = query.last()['week']
    #온도 구하기
    temperature =  Monthly_temp.objects.filter(year=year_is, month=starting_month).values('temp')
    temperature =temperature[0]['temp']
    #개화,첫눈 날짜 가져오기
    weather_staus  = Yearly_weather.objects.filter(year=year_is).values('first_bloom', 'first_snow')
    if  season_is == 0:
        differentday =  starting_day - weather_staus[0]['first_bloom']
        differentday = differentday.days
        weather_staus = weather_staus[0]['first_bloom'].strftime('%#m월 %#d일')
        
    else:
        differentday =  starting_day - weather_staus[0]['first_snow']
        differentday = differentday.days
        weather_staus = weather_staus[0]['first_snow'].strftime('%#m월 %#d일')
        
    #D-day날짜 구하기
    
    season_name= {0:'봄',1:'겨울'}    
    season_info = {
        'overall_first_month': starting_month,
        'overall_first_week': starting_week,
        'overall_last_month': ending_month,
        'overall_last_week': ending_week,
        'temperature': temperature,
        'weather_staus': weather_staus,
        'differentday' : differentday
        }
    appearances = season_info
    
    # 데이터를 리스트로 변환하고 'title'로 그룹화
    data_list = list(data.values('date', 'rank', 'title','singer'))
    grouped = groupby(sorted(data_list, key=lambda x: (x['title'], x['singer'])), 
                      key=lambda x: (x['title'], x['singer']))
    
    all_dates = sorted({g['date'] for g in data_list})
    tick_vals = [date.strftime('%Y-%m-%d') for date in all_dates]
    tick_texts = [date.strftime('%m월 %d일') for date in all_dates]    
    
    
    # 새로운 그래프 객체 생성
    fig = go.Figure()
    for (title,singer), group in grouped:
        group_list = list(group)
        fig.add_trace(go.Scatter(
            x=[g['date'] for g in group_list],
            y=[g['rank'] for g in group_list],
            mode='lines+markers',
            name=title,
            hovertemplate=' %{x} <br>'+ '순위 : %{y}위',
            line_shape='linear'
            )            
        )
    
        
    fig.update_xaxes(title_text="날짜",
            title_font=dict(family="Arial, sans-serif", size=18, color="RebeccaPurple"),
            tickvals=tick_vals,  # 날짜 데이터를 기준으로 틱을 설정
            ticktext=tick_texts,  # 날짜 형식을 '월 일'로 설정
            tickangle=-45,  # 라벨의 기울기를 -45도로 설정
            autorange=True
            )
    fig.update_yaxes(title_text="순위",
            title_font=dict(family="Arial, sans-serif", size=18, color="RebeccaPurple"))

    # 그래프 레이아웃 설정
    fig.update_layout(
        title=f' {year_is}년도 {season_name[season_is]}노래 차트 추이',
        xaxis_title='날짜',
        yaxis_title='순위',
        yaxis=dict(autorange="reversed"),
        legend_title="노래",
        template="simple_white"
        
        
    )
    

    # 그래프 HTML과 appearances 딕셔너리 반환
    graph_html = pio.to_html(fig, full_html=False)
    return graph_html, appearances 



def parse_data_for_table(chart, year_): #그 해 노래 리스트 
    dic = defaultdict(list)
    for instance in chart:
        years_str = instance.years.strip("[]")
        years_list = years_str.split(",")

        for year in years_list:
            if year.strip() == year_:
                dic[instance.title] = instance.singer
    return dic