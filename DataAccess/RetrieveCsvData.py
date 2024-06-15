import flet as ft
import pandas as pd
import os.path
from DataAccess.InitializeCsvDatabase import *
import csv
import json
import globalVariable as gv

def RetrieveCsvMMSummaryData(page: ft.Page):
    globalVr=gv.globalVariable(page)
    storageLocation=globalVr.cStorage

    if(os.path.isfile(storageLocation+"mainMenuSummaryData.csv")):
        file1=pd.read_csv(storageLocation+"mainMenuSummaryData.csv")
        print("Here1")
        print(storageLocation)
        print(file1)
        data = {}
        with open(file1) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows['summaryName']
                data[id] = rows

        return data
    else:
        initCsvDatabase(page)
        return 
    
def RetrieveCsvMMNetWorthData(page: ft.Page):
    globalVr=gv.globalVariable(page)
    storageLocation=globalVr.cStorage

    if(os.path.isfile(storageLocation+"mainMenuNetWorthData.csv")):
        file1=pd.read_csv(storageLocation+"mainMenuNetWorthData.csv")
        print("Here1")
        print(storageLocation)
        print(file1)
        data = {}
        with open(file1) as csvFile:
            csvReader = csv.DictReader(csvFile)
            for rows in csvReader:
                id = rows['summaryName']
                data[id] = rows

        return data
    else:
        initCsvDatabase(page)
        return 
    
    