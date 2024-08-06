import flet as ft
from state import liturgia, oracoes, devocoes_carismas, calendario, contatos
from handlers import show_liturgia, show_oracoes, show_devocoes_carismas, show_calendario, show_contatos
from styles import CustomButtonNav
import time

BGCOLOR_BAR = ft.colors.BLACK

def main(page: ft.Page):
    page.bgcolor = ft.colors.GREY_200
    page.adaptive = True
    
    # Layout inicial
    image_layout = ft.Container(
        width=350,
        margin=ft.margin.all(30),
        bgcolor= ft.colors.WHITE,
        expand=True,
        content= ft.Image(
            src='assets/logo.png',
            width=350,
        ),
    )
    
    page.add(image_layout)
    time.sleep(3)
    page.remove(image_layout)
    
    page.appbar = ft.AppBar(
        bgcolor=BGCOLOR_BAR,
        actions=[
            CustomButtonNav.create('Liturgia', lambda _: show_liturgia(page)),
            CustomButtonNav.create('Orações', lambda _: show_oracoes(page)),
            CustomButtonNav.create('Devoções e Carismas', lambda _: show_devocoes_carismas(page)),
        ]
    )
    
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=BGCOLOR_BAR,
        content=ft.Row(
            controls=[
                CustomButtonNav.create('Calendário', lambda _: show_calendario(page)),
                ft.Container(expand=True),
                CustomButtonNav.create('Contatos', lambda _: show_contatos(page)),
            ]
        )
    )

    # Adicionar layout completo à página
    layout = ft.Container(
        width=520,
        margin=ft.margin.all(30),
        content=ft.Column(
            controls=[
                liturgia.get_container(),
                oracoes.get_container(),
                devocoes_carismas.get_container(),
                calendario.get_container(),
                contatos.get_container()
            ]
        )      
    )
    
    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)
