import flet as ft

# TODO: maybe change to UserControl
class Stats(ft.Column):
    def __init__(self):
        super().__init__()

        self.controls = [
            ft.Text("stats")            
        ]

        self.rehydrate()


    
    def rehydrate(self):
        pass

