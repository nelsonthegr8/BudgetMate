import flet as ft
from Styles.ColorThemeClass import *
from Views.AccountsView     import * 

def accountsPage(page: ft.page):
    colorScheme = ColorTheme('Light')
    accountsView=AccountsView()

    page.add(accountsView)

