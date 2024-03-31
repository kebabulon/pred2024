import flet as ft

from urllib.parse import parse_qs, urlparse
from router.routes import ROUTES

from providers.app_prodiver import AppProvider

from pages.login import Login
from pages.dashboard import Dashboard

class Router:
    def __init__(self):
        self.pages = {
            ROUTES.LOGIN_ROUTE: Login,
            ROUTES.DASHBOARD_ROUTE: Dashboard,
        }

    def route_change(self, route):
        _route = urlparse(route.route)
        params = parse_qs(_route.query)
        path = _route.path

        page = AppProvider.page

        # changing page.route triggers on_route_change
        # which we do not want for page popping
        # https://github.com/flet-dev/flet/issues/2776
        # https://stackoverflow.com/questions/77338873/flet-popping-a-view-creates-duplicate-views
        if page.views[-1].route == path:
            return

        is_pop = params.get("pop", [None])[0]
        if not is_pop:
            page.views.clear()

        page.views.append(
            self.pages[path]()
        )

        AppProvider.page.update()