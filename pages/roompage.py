import flet as ft

import requests
import json

from router.routes import ROUTES
from router.navigator import Navigator

from providers.data_provider import DataProvider
from providers.app_prodiver import AppProvider

class RoomPage(ft.View):
    def __init__(self):
        super().__init__(route=ROUTES.ROOMPAGE_ROUTE)

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

        self.scroll=ft.ScrollMode.ALWAYS

        self.floor_column = ft.Column(
            spacing=5,
        )

        dday, dmonth, dyear = DataProvider.date_rn.split("-")

        p = "https://olimp.miet.ru/ppo_it_final/?day={}&month={}&{}".format(dday, dmonth, dyear)
        print(p)

        req = requests.get("https://olimp.miet.ru/ppo_it_final?day={}&month={}&year={}".format(dday, dmonth, dyear), headers={"X-Auth-Token": "ppo_10_11568"})
        info = json.loads(req.text)
        info = info["message"]
        print(info)
        room_count_per_floor = info["flats_count"]["data"]
        windows_for_room = info["windows_for_flat"]["data"]
        print(room_count_per_floor)
        print(windows_for_room)

        self.controls = [
            ft.Text(DataProvider.date_rn, size=20),
            ft.Text("Количество комнат на этаже: {}".format(room_count_per_floor), size=15),
            ft.Text("Количество комнат на этаже: {}".format(" ".join(map(str, windows_for_room))), size=15),
            ft.Container(
                self.floor_column,
                expand=True,
            )
        ]


        floor_rn = 1
        for floor in info["windows"]["data"]:
            f = info["windows"]["data"][floor]
            print(f)
            floor_row = ft.Row(
                controls=[],
                spacing=5
            ) 
            counter = windows_for_room.copy()
            rn = 0
            for i in f:
                counter[rn] -= 1
                c = ft.colors.WHITE
                if i:
                    c = bgcolor=ft.colors.AMBER
                floor_row.controls.append(
                    ft.Container(
                        content=ft.Text(
                            floor_rn,
                            color=ft.colors.BLACK
                        ),
                        bgcolor=c,
                        width=50,
                        height=50,
                        alignment=ft.alignment.center
                    )
                )
                if counter[rn] == 0:
                    rn += 1
                    floor_rn += 1

            self.floor_column.controls.append(floor_row)
        self.floor_column.controls = self.floor_column.controls[::-1]




 
