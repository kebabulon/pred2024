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
            title=ft.Text(DataProvider.date_rn),
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

        floor_rn = 1
        room_count = 0
        all_room_count = 1
        room_arr = []
        for floor in info["windows"]["data"]:
            f = info["windows"]["data"][floor]
            print(f)
            floor_row = ft.Row(
                controls=[],
                spacing=5
            ) 
            counter = windows_for_room.copy()
            rn = 0
            lighted = False
            for i in f:
                counter[rn] -= 1
                c = ft.colors.WHITE
                if i:
                    lighted = True
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
                    if lighted:
                        room_count += 1
                        room_arr.append(all_room_count)
                    rn += 1
                    all_room_count += 1
                    floor_rn += 1
                    lighted = False
            self.floor_column.controls.append(floor_row)

        self.floor_column.controls = self.floor_column.controls[::-1]

        self.ans_text = ft.Text(size=15)
        self.update_ans(DataProvider.get_ans(DataProvider.date_rn))

        self.controls = [
            ft.Text("Входные данные", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("Количество комнат на этаже: {}".format(room_count_per_floor), size=15),
            ft.Text("Количество комнат на этаже: {}".format(" ".join(map(str, windows_for_room))), size=15),
            ft.Container(
                self.floor_column,
            ),
            ft.Text("Ответ", size=20, weight=ft.FontWeight.BOLD),
            ft.Text("Количество комнат: {}".format(room_count), size=15),
            ft.Text("Номера комнат: {}".format(", ".join(map(str, room_arr))), size=15),
            ft.TextButton("Проверить ответ", on_click=self.check, data=[room_count, room_arr]),
            self.ans_text,
        ]
    
    def check(self, e):
        d = e.control.data
        inp = {
            "message": {
                "data": {
                    "count": d[0],
                    "rooms": d[1]
                },
                "date": DataProvider.date_rn
            }
        } 
        print(inp)
        inpj = json.dumps(inp) #.replace('"', "'")
        print(inpj)

        req = requests.post("https://olimp.miet.ru/ppo_it_final", headers={"X-Auth-Token": "ppo_10_11568", 'Content-type': 'application/json'}, json=inpj)
        print(req.text)
        print(req.status_code)
        print(req.headers)

        # Update db code
        # ans = 1
        # DataProvider.change_ans(DataProvider.date_rn, ans)
    
    def update_ans(self, res):
        t = ""
        if res == 0:
            t = "Не пройдена"
            self.ans_text.color = ft.colors.RED
        elif not res:
            t = "Отсутствует"
            self.ans_text.color = ft.colors.WHITE
        else:
            t = "Пройдена"
            self.ans_text.color = ft.colors.GREEN

        self.ans_text.value = "Результат проверки: {}".format(t)







 
