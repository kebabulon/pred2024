import flet as ft
from datetime import datetime
from providers.data_provider import DataProvider

# TODO: maybe change to UserControl
class Analyze(ft.Column):
    def __init__(self):
        super().__init__()

        self.first_name = ft.Text("first")
        self.last_name = ft.Text("last")
        self.byear = ft.Text("byear")

        self.controls = [
            ft.Row(
                controls = [self.first_name],
            ),
            ft.Row(
                controls = [self.last_name],
            ),
            ft.Row(
                controls = [self.byear],
            ),
        ]

        self.rehydrate()

    
    def rehydrate(self):
        patient_info = DataProvider.get_patient_info()
        self.first_name.value = "Имя: {}".format(patient_info[0])
        self.last_name.value = "Фамилия: {}".format(patient_info[1])
        age = datetime.now() - datetime.strptime(patient_info[2]).date()
        self.byear.value = "Дата рождения: {} ({} лет)".format(patient_info[2], age.year)
