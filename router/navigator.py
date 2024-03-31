import flet as ft

from providers.app_prodiver import AppProvider

class Navigator:
    @classmethod
    def go(self, path, **params):
        page = AppProvider.page
        page.go(path, **params)
