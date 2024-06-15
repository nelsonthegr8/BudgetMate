import flet as ft
import pandas as pd

def initCsvDatabase(page: ft.Page):
    storageLocation=page.client_storage.get("BudgetMate_csvFileStorageLocation")

    