import flet as ft
from state import liturgia, oracoes, devocoes_carismas, calendario, contatos
from handlers import show_liturgia, show_oracoes, show_devocoes_carismas, show_calendario, show_contatos

def create_layout(page):
    return ft.Container(
        
        width=520,
        margin=ft.margin.all(15),
        content=ft.Column(
            controls=[
                liturgia,
                oracoes,
                devocoes_carismas,
                calendario,
                contatos
            ]
        )
    )

def create_header(page):
    return ft.Container(
        bgcolor='#000000',
        padding=ft.padding.all(15),
        border_radius=ft.border_radius.only(
            top_left=0,
            top_right=0,
            bottom_right=6,
            bottom_left=6,
        ),
        content=ft.ResponsiveRow(
            columns=12,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment='spaceBetween',
            controls=[
                ft.TextButton(
                    col=4,
                    on_click=lambda e: show_liturgia(page),
                    content=ft.Text(
                        value='Liturgia',
                        color='#ffffff',
                        size=12,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ),
                ft.TextButton(
                    col=4,
                    on_click=lambda e: show_oracoes(page),
                    content=ft.Text(
                        value="Orações",
                        color="#ffffff",
                        size=12,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ),
                ft.TextButton(
                    col=4,
                    on_click=lambda e: show_devocoes_carismas(page),
                    content=ft.Text(
                        value='Devoção\ne Carisma',
                        color='#ffffff',
                        size=12,
                        text_align=ft.TextAlign.CENTER,
                    ),
                )
            ]
        )
    )

def create_footer(page):
    return ft.Container(
        bgcolor='#000000',
        padding=ft.padding.all(15),
        border_radius=ft.border_radius.only(
            top_left=6,
            top_right=6,
            bottom_right=0,
            bottom_left=0,
        ),
        content=ft.ResponsiveRow(
            columns=12,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment='spaceBetween',
            controls=[
                ft.TextButton(
                    col=6,
                    on_click=lambda e: show_calendario(page),
                    content=ft.Text(
                        value='Calendário',
                        color='#ffffff',
                        size=12,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ),
                ft.TextButton(
                    col=6,
                    on_click=lambda e: show_contatos(page),
                    content=ft.Text(
                        value='Contatos',
                        color='#ffffff',
                        size=12,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ),
            ]
        )
    )
