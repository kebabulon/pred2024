import flet as ft

from router.router import Router
from router.navigator import Navigator

from providers.data_provider import DataProvider
from providers.app_prodiver import AppProvider

def main(page: ft.Page):
    page.title = "CancerAI"

    page.window_min_width = 1250
    page.window_min_height = 760
    
    page.window_width = page.window_min_width
    page.window_height = page.window_min_height

    page.padding = 0

    theme = ft.Theme()
    theme.page_transitions.macos = ft.PageTransitionTheme.CUPERTINO
    theme.page_transitions.linux = ft.PageTransitionTheme.CUPERTINO
    theme.page_transitions.windows = ft.PageTransitionTheme.CUPERTINO
    page.theme = theme
    page.theme_mode = ft.ThemeMode.DARK

    AppProvider.page = page
    DataProvider.initialize()

    router = Router()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.route = top_view.route
        page.update()

    page.on_route_change = router.route_change
    page.on_view_pop = view_pop

    page.go("/dashboard")


ft.app(target=main)