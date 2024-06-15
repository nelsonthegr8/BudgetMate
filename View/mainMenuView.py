import flet as ft
from Model.mainMenuNetWorthChartModel import mainMenuNetWorth as nwm
from Model.mainMenuQuickSummaryCardsModel import mainMenuSummary as scm
import numpy as np

def mainMenuView(page: ft.Page, netWorthData: nwm,summaryData: scm):
    nwMonths=netWorthData.month
    nwYear=netWorthData.year
    nwTotals=netWorthData.netWorth
    i=0
    dataPoints = []
    bottomAxisLabels = []
    leftAxisLabels=[
                ft.ChartAxisLabel(
                    value=0,
                    label=ft.Text("0", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=3,
                    label=ft.Text("30K", size=14, weight=ft.FontWeight.BOLD),
                ),
                ft.ChartAxisLabel(
                    value=5,
                    label=ft.Text("50K", size=14, weight=ft.FontWeight.BOLD),
                ),
            ]
    
    dataSum=0

    for j in nwTotals:
        dataPoints.append(ft.LineChartDataPoint(i,nwTotals[i]))
        bottomAxisLabels.append(ft.ChartAxisLabel(value=i,
                                            label=ft.Text(nwMonths[i],size=14, weight=ft.FontWeight.BOLD)))
        dataSum+=nwTotals[i]
        i+=1
    #get 4 values to place on the side of chart
    # leftAxisLabels.append(dataPoints.min())
    # leftAxisLabels.append(dataSum/dataPoints.size+25)
    # leftAxisLabels.append(dataPoints.max()+50)
    # leftAxisLabels.append(dataPoints.max()+150)

    data_1 = [
        ft.LineChartData(
            data_points=dataPoints,
            stroke_width=5,
            color=ft.colors.CYAN,
            curved=True,
            stroke_cap_round=True
        )
    ]
    
    netWorthCard=ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Net Worth: "+str(nwYear),size=32,weight=ft.FontWeight.BOLD),
                    ft.LineChart(
                        data_series=data_1,
                        border=ft.border.all(3, ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE)),
                        horizontal_grid_lines=ft.ChartGridLines(
                            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
                        ),
                        vertical_grid_lines=ft.ChartGridLines(
                            interval=1, color=ft.colors.with_opacity(0.2, ft.colors.ON_SURFACE), width=1
                        ),
                        left_axis=ft.ChartAxis(
                            labels=leftAxisLabels,
                            labels_size=40
                        ),
                        bottom_axis=ft.ChartAxis(
                            labels=bottomAxisLabels,
                            labels_size=32
                        ),
                        tooltip_bgcolor=ft.colors.with_opacity(0.8, ft.colors.BLUE_GREY),
                        #animate=5000,
                        expand=True
                    ),
                ]
            ),
            margin=ft.margin.all(100)
        ),
        margin=ft.margin.all(150)
    )

    view = ft.SafeArea(
        netWorthCard,
        expand=True
    )

    return view