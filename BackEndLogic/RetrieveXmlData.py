import flet as ft

def RetrieveXmlData(page: ft.Page):
    value=page.client_storage.get("saveFileLocation")

    if(value==None):
        print("no key value")