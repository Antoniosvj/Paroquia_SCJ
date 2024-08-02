import flet as ft

BGCOLOR = ft.colors.GREY_100
TEXT_COLOR = '#D82622'

#orações
def oracaoSLourenco():
    pass

def create_oracoes():
    return ft.Container(
        content=ft.Column([
            ft.Text(
                value='Orações',
                size=24,
                color=TEXT_COLOR,
                weight=ft.FontWeight.W_900,
            ),
            ft.ElevatedButton(
                text='Oração a São Lourenço',
                color=TEXT_COLOR,
                bgcolor=BGCOLOR,
                style=ft.ButtonStyle(side=ft.BorderSide(1, TEXT_COLOR)),
                on_click= oracaoSLourenco,
            ),
            ft.ElevatedButton(
                text='Santo Terço',
                color=TEXT_COLOR,
                bgcolor=BGCOLOR,
                style=ft.ButtonStyle(side=ft.BorderSide(1, TEXT_COLOR))

            ),
        ]),
        visible=False,
    )

