import flet as ft


import json
import requests

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
            title=ft.Text("Комнаты Модеста"),
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
            auto_scroll=True,
        )


        self.controls = [
            self.list_view,
        ]

        req = requests.get("https://olimp.miet.ru/ppo_it_final/date", headers={"X-Auth-Token": "ppo_10_11568"})
        dates = json.loads(req.text)
        for i in dates["message"]:
            test = ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(i),
                        ft.TextButton("Go", on_click=self.go_to_roompage, data=i)
                    ],
                    expand=True,
                ),
                padding=5,
                bgcolor=ft.colors.PRIMARY_CONTAINER,
            )
            self.list_view.controls.append(test)

    def go_to_roompage(self, e):
        DataProvider.date_rn = e.control.data
        Navigator.go(ROUTES.ROOMPAGE_ROUTE, pop=True)
 
