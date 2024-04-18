from django.shortcuts import render
from .models import All_chart
import plotly.graph_objects as go
import plotly.io as pio
from itertools import groupby

def chart_view(year_is, season_is):
    # 데이터베이스에서 주어진 연도와 시즌의 데이터 필터링 및 정렬
    data = All_chart.objects.filter(year=year_is, season=season_is).order_by('title', 'date')
    
    # 데이터를 리스트로 변환
    data_list = list(data.values('date', 'rank', 'title'))
    
    # 'title'로 그룹화
    grouped = groupby(data_list, key=lambda x: x['title'])
    
    # 새로운 그래프 객체 생성
    fig = go.Figure()

    # 각 그룹(노래)별로 다른 색상의 선 그래프 생성
    for title, group in grouped:
        group_list = list(group)
        fig.add_trace(go.Scatter(
            x=[g['date'] for g in group_list],
            y=[g['rank'] for g in group_list],
            mode='lines+markers',
            name=title  # 범례에 표시될 노래 제목
        ))

    # 그래프 레이아웃 설정
    fig.update_layout(
        title=f'Ranking Changes in {year_is} with Season {season_is}',
        xaxis_title='Date',
        yaxis_title='Rank',
        yaxis=dict(autorange="reversed"),  # 랭킹 높은 순으로 정렬
        legend_title="Songs"
    )

    # 그래프를 HTML로 변환하여 반환
    return pio.to_html(fig, full_html=False)
