import flet as ft 

class globalVariable():
    def __init__(self,page: ft.Page) -> None:
        self.cStorage = page.client_storage.get("BudgetMate_csvFileStorageLocation")
    