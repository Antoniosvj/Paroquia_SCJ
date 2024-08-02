import flet as ft

BGCOLOR = ft.colors.GREY_100
TEXT_COLOR = '#D82622'

def create_devocoes_carismas():
    return ft.Container(
        content= ft.Column([
            ft.Text(
                value='Devoções e Carismas',
                size=24,
                color=TEXT_COLOR,
                weight=ft.FontWeight.W_900,
            ),
            ft.ElevatedButton(
                text='Sagrado Coração de Jesus',
                color=TEXT_COLOR,
                bgcolor=BGCOLOR,
                style=ft.ButtonStyle(side=ft.BorderSide(1, TEXT_COLOR))
            ),
            ft.ElevatedButton(
                text='Santo do Dia',
                color=TEXT_COLOR,
                bgcolor=BGCOLOR,
                style=ft.ButtonStyle(side=ft.BorderSide(1, TEXT_COLOR))
            ),
        ]),
        visible=False
    )
