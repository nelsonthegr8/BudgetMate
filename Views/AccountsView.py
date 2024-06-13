import flet as ft

class AccountsView(ft.UserControl):
    isExpense = False


    def build(self):

        self.textField=ft.TextField(width=350)
        self.addBtn=ft.FloatingActionButton(icon=ft.icons.ADD,
                                            on_click=self.addClick)
        self.AccountsData = ft.Column()
        accountsRow = ft.Column(controls=[
            ft.Row(controls=[self.textField, self.addBtn]),
        self.AccountsData])
        return accountsRow

    
    def addClick(self, e):
        pass

    def deleteClick(self, e):
        pass