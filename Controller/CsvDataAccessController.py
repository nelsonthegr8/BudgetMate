from DataAccess.InitializeCsvDatabase import *
from DataAccess.RetrieveCsvData import *
from DataAccess.StoreCsvData import *
from Model.mainMenuNetWorthChartModel import *
from Model.mainMenuQuickSummaryCardsModel import *
import pandas as pd
import flet as ft

def getMainMenuSummaryData(page: ft.Page):
    data=RetrieveCsvMMSummaryData(page)
    
    if(data!=None):
        json_object = json.load(data)
        print(json_object)
    else:
        summary=mainMenuSummary()
        return summary
    
def getMainMenuNetworthData(page: ft.Page):
    data=RetrieveCsvMMNetWorthData(page)

    if(data!=None):
        json_object = json.load(data)
        print(json_object)
    else:
        summary=mainMenuNetWorth()
        return summary