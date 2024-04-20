from .models import All_chart
import plotly.graph_objects as go
import plotly.io as pio
from itertools import groupby
from django.db.models import Min, Max
import datetime
from collections import defaultdict, OrderedDict
import pandas as pd
# 날짜 형식 변환 함수
def format_date(date):
    if isinstance(date, str):
        # 문자열 날짜를 datetime 객체로 변환
        date_obj = datetime.datetime.strptime(date, '%b %d, %Y')
    elif isinstance(date, datetime.date):
        # 이미 datetime.date 객체인 경우 직접 사용
        date_obj = date
    else:
        raise TypeError("Unsupported date type")
    # 원하는 형식으로 문자열로 다시 변환
    return date_obj.strftime('%m월 %d일')

def chart_view(year_is, season_is):
    # 데이터베이스에서 주어진 연도와 시즌의 데이터 필터링 및 정렬
    data = All_chart.objects.filter(year=year_is, season=season_is).order_by('date','title' )
    query = data.values()
    data_list = list(query)
    starting_month = query.first()['month']
    starting_week = query.first()['week']
    ending_month = query.last()['month']    
    ending_week = query.last()['week']    
    
    season_name= {0:'봄',1:'겨울'}    
    season_info = {
        'overall_first_month': starting_month,
        'overall_first_week': starting_week,
        'overall_last_month': ending_month,
        'overall_last_week': ending_week
        }
    appearances = season_info
    
    # 데이터를 리스트로 변환하고 'title'로 그룹화
    data_list = list(data.values('date', 'rank', 'title'))
    grouped = groupby(sorted(data_list, key=lambda x: x['title']), key=lambda x: x['title'])
    
    # 새로운 그래프 객체 생성
    fig = go.Figure()
    for title, group in grouped:
        group_list = list(group)
        formatted_dates = [format_date(g['date']) for g in group_list]
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
            title_font=dict(family="Arial, sans-serif", size=18, color="RebeccaPurple"))
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