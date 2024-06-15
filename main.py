import flet as ft
from View.routingMainView import *
from View.scratchPadView import *
 
if __name__ == "__main__":
 
    def main(page: ft.Page):
        page.adaptive = True
        #page.add(getMainMenu(page))

    ft.app(target=routingMainView, view=ft.FLET_APP)