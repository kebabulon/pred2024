import flet as ft

from router.routes import ROUTES
from router.navigator import Navigator

from providers.data_provider import DataProvider
from providers.app_prodiver import AppProvider

from compontents.dashboard.stats import Stats
from compontents.dashboard.analyze import Analyze


class Dashboard(ft.View):
    def __init__(self):
        super().__init__(route=ROUTES.DASHBOARD_ROUTE)

        self.stats = Stats()
        self.analyze = Analyze()

        self.active_view = ft.Container(
            content=self.stats
        )

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

        self.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(
                    icon=ft.icons.PERSON,
                    label="Журнал",
                ),
                 ft.NavigationDestination(
                    icon=ft.icons.SEARCH,
                    label="Анализ",
                ),
           ]
        )

        self.navigation_bar.on_change = self.nav_bar_on_change

        self.controls = [
            self.active_view,
        ]
    
    def nav_bar_on_change(self, _):
        if self.navigation_bar.selected_index == 0:
            self.active_view.content = self.stats
        elif self.navigation_bar.selected_index == 1:
            self.active_view.content = self.analyze
        self.active_view.update()

    def rehydrate(self):
        # update stats from pop up using page.views[0]
        self.stats.update()
        pass
