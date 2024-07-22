import flet as ft
from layout import create_layout, create_header, create_footer
import time

def main(page: ft.Page):
    # Layout inicial
    image_layout = ft.Container(
        width=350,
        margin=ft.margin.all(30),
        content=ft.Image(
            src='assets/icon.png',
            width=100,
        )
    )
    page.add(image_layout)
    time.sleep(3)
    page.remove(image_layout)

    # Criação do layout
    header = create_header(page)
    footer = create_footer(page)
    main_content = create_layout(page)

    # Adicionar layout completo à página
    layout = ft.Container(
        width=520,
        margin=ft.margin.all(30),
        content=ft.Column(
            controls=[
                header,
                main_content,
                footer
            ]
        )
    )
    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main)
