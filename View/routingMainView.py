import flet as ft
from Controller.mainMenuConrtoller import *

def routingMainView(page: ft.Page):
    page.adaptive = True
    page.title = "Budget Mate"

    def appBar(title):
        sideMenuButton=ft.IconButton(icon=ft.icons.MENU_ROUNDED, 
                                     on_click=lambda _: page.go("/storageLocation_Selection"))
        bar=ft.AppBar(title=ft.Text(title), bgcolor=ft.colors.SURFACE_VARIANT, 
                      center_title=True, leading=sideMenuButton)

        return bar

    def route_change(route):
        globalVr=globalVariable(page)
        value = globalVr.cStorage
        if(value==None):
            page.route = "/storageLocation_Selection"
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    appBar("Budget Mate"),
                    getMainMenu(page),
                ],
            )
        )
        if page.route == "/storageLocation_Selection":
            page.views.append(
                ft.View(
                    "",
                    [
                        appBar("Location Selection"),
                        ft.ElevatedButton("Back", on_click=lambda _: page.go("/")),
                        getCsvStorageLocationView(page)
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)
