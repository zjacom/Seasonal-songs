from .models import All_chart
import plotly.graph_objects as go
import plotly.io as pio
from itertools import groupby
from django.db.models import Min, Max
import datetime
from collections import defaultdict, OrderedDict
import pandas as pd


def chart_view(year_is, season_is):
    # 데이터베이스에서 주어진 연도와 시즌의 데이터 필터링 및 정렬
    data = All_chart.objects.filter(year=year_is, season=season_is).order_by('title', 'date')
    query = data.values()
    data_list = list(query)
    
    season_name= {0:'봄',1:'겨울'}
    # Pandas DataFrame 생성
    df = pd.DataFrame(data_list)
    data_date = data.values('title').annotate(
            first_date=Min('date'),
            last_date=Max('date')
        )
        
        # 최초 및 최종 등장 날짜의 month와 week 값을 찾기 위해 추가 쿼리 실행
    appearances = []
    for item in data_date:
        first = All_chart.objects.filter(title=item['title'], date=item['first_date']).first()
        last = All_chart.objects.filter(title=item['title'], date=item['last_date']).first()
        
        appearance = {
                'title': item['title'],
                'first_month': first.month if first else None,
                'first_week': first.week if first else None,
                'last_month': last.month if last else None,
                'last_week': last.week if last else None
            }
        appearances.append(appearance)
        
    
    df2 = pd.DataFrame(appearances)
    
    # 전체 최소 및 최대 월/주 계산
    overall_first_month = df2['first_month'].min()
    overall_first_week = df2.loc[df2['first_month'] == overall_first_month, 'first_week'].min()
    overall_last_month = df2['last_month'].max()
    overall_last_week = df2.loc[df2['last_month'] == overall_last_month, 'last_week'].max()

    # 계산 결과를 사전으로 저장
    season_info = {
        'overall_first_month': overall_first_month,
        'overall_first_week': overall_first_week,
        'overall_last_month': overall_last_month,
        'overall_last_week': overall_last_week
        }
    appearances = season_info 

    
    # 데이터를 리스트로 변환하고 'title'로 그룹화
    data_list = list(data.values('date', 'rank', 'title'))
    grouped = groupby(sorted(data_list, key=lambda x: x['title']), key=lambda x: x['title'])
    
    # 새로운 그래프 객체 생성
    fig = go.Figure()
    for title, group in grouped:
        group_list = list(group)
        fig.add_trace(go.Scatter(
            x=[g['date'] for g in group_list],
            y=[g['rank'] for g in group_list],
            mode='lines+markers',
            name=title
        ))

    # 그래프 레이아웃 설정
    fig.update_layout(
        title=f' {year_is}년도 {season_name[season_is]}노래 차트 추이',
        xaxis_title='날짜',
        yaxis_title='순위',
        yaxis=dict(autorange="reversed"),
        legend_title="Songs"
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