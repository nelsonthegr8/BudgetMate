import flet as ft
from Controller.CsvDataAccessController import *
from Controller.awsDataAccessController import *
from View.csvStorageLocationView import *
from View.mainMenuView import *
from Model import *
from globalVariable import *

def getMainMenu(page: ft.Page):
    isAwsData=False
    value=None
    
    #we need to check if user is getting data from aws or csv
    if(isAwsData==False):
    #if csv data then grab csv data model
        summaryData=getMainMenuSummaryData(page)
        netWorthData=getMainMenuNetworthData(page)
    
    #pass data model grabbed over to the view to shape the data
    view=mainMenuView(page,netWorthData,summaryData)
    #return view back to the caller
    return view

def getCsvStorageLocationView(page: ft.Page):
    view=csvStorageLocation()
    return view
