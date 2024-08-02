import flet as ft

BGCOLOR = ft.colors.GREY_100
TEXT_COLOR = '#D82622'

def create_calendario():
    return ft.Container(
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

