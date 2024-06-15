from typing import Any, List
import flet as ft

def csvStorageLocation(page: ft.Page):
    
    # Open directory dialog
    def get_directory_result(e: ft.FilePickerResultEvent):
        path=e.path if e.path else ""
        chosenLocatonTxt.value = path
        chosenLocatonTxt.update()
        if(chosenLocatonTxt.value==""):
            saveBtn.disabled=True
        else:
            saveBtn.disabled=False
        saveBtn.update()


    def save_directory_data(e):
        budgetMateFolderExt="\\BudgetMateData\\"
        directory=chosenLocatonTxt.value+budgetMateFolderExt
        page.client_storage.set("BudgetMate_csvFileStorageLocation", directory)

    get_directory_dialog = ft.FilePicker(on_result=get_directory_result)

    chooseLocationBtn= ft.ElevatedButton(
                    "Open directory",
                    icon=ft.icons.FOLDER_OPEN,
                    on_click=lambda _: get_directory_dialog.get_directory_path(),
                    disabled=page.web,
                )
    chosenLocatonTxt=ft.Text()
    saveBtn=ft.ElevatedButton(
                    "Save",
                    icon=ft.icons.SAVE_ROUNDED,
                    on_click=save_directory_data,
                )
    saveBtn.disabled=True
    
    card=ft.Card(
        content=ft.ResponsiveRow([
            ft.Container(
                    ft.ListTile(
                        title=ft.Text("Please Choose a location on your device where you would like to store your data. The information is being saved as multiple csv files. I recommed a shared folder like google drive etc. So that you can point back to that folder on different devices and have that data shared on all other devices.")
                    )
            ),
            ft.Container(
                chosenLocatonTxt
            ),
            ft.Container(
                ft.ResponsiveRow([
                        ft.Column(col={"xs": 6,"sm": 3, "md": 2, "xl": 2}, controls=[chooseLocationBtn]),
                        ft.Column(col={"xs": 6,"sm": 3, "md": 2, "xl": 2}, controls=[saveBtn])
                        ],
                        spacing=10,
                        alignment=ft.MainAxisAlignment.END,
                        
                    )
            )
        ]),
        margin=ft.margin.all(5)
    )

    page.overlay.extend([get_directory_dialog])

    view = ft.SafeArea(
            ft.ResponsiveRow([
                ft.Container(
                    card
                )
            ])
        )
    
    return view
