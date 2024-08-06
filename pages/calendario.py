import flet as ft

BGCOLOR = ft.colors.GREY_100
TEXT_COLOR = '#D82622'

class CalendarioPage:
    def __init__(self):
        self.container = ft.Container(
            content=ft.Column([
                ft.Text(
                    value='Calendário',
                    size=24,
                    color=TEXT_COLOR,
                    weight=ft.FontWeight.W_900,
                ),
            ]),
            visible=False,
        )
    
    def show(self):
        self.container.visible = True

    def hide(self):
        self.container.visible = False

    def get_container(self):
        return self.container
