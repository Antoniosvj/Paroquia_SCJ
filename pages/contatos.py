import flet as ft

BGCOLOR = ft.colors.GREY_100
TEXT_COLOR = '#D82622'

def create_contatos():
    return ft.Container(
        content=ft.Column([
            ft.Text(
                value='Contatos',
                size=24,
                color=TEXT_COLOR,
                weight=ft.FontWeight.W_900,
            ),
            ft.Row(
                controls=[
                    ft.Image(
                        src='https://img.icons8.com/?size=60&id=Xy10Jcu1L2Su&format=png&color=000000'
                    ),
                    ft.Image(
                        src='https://img.icons8.com/?size=60&id=16712&format=png&color=94D82D'
                    ),
                ]
            )
            
                   
                               
            
        ]),
        visible=False,
    )

