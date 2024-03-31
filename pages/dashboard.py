import flet as ft

from router.routes import ROUTES
from router.navigator import Navigator

from providers.data_provider import DataProvider
from providers.app_prodiver import AppProvider

class Dashboard(ft.View):
    def __init__(self):
        super().__init__(route=ROUTES.DASHBOARD_ROUTE)

        # add logout button
        # show med's name in the top right corner near logout button
        self.appbar = ft.AppBar(
            title=ft.Text("CancerAI"),
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
        )

        self.list_view = ft.ListView(
            expand=1,
            spacing=10,
            padding=20,
            auto_scroll=True
        )

        test = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text("room 1"),
                    ft.TextButton("Go")# , on_click=button_clicked, data=0)
                ],
                expand=True,
            ),
            padding=5,
            bgcolor=ft.colors.PRIMARY_CONTAINER,
        )
        self.list_view.controls.append(test)

        self.controls = [
            self.list_view,
        ]
 
