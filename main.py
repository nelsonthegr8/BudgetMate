import flet as ft
from Styles.ColorThemeClass import *
from accountsPage import *
from Class.DataAccessClass import *
from Class.BudgetMateApp import *

from flet import (
    Page,
    colors
)
 
if __name__ == "__main__":
 
    def main(page: Page):
 
        page.title = "Flet Trello clone"
        page.padding = 0
        page.bgcolor = colors.BLUE_GREY_200
        app = BudgetMateApp(page)
        page.add(app)
        page.update()
 
    ft.app(target=main, view=ft.FLET_APP)