import flet as ft
import requests
import json

TITLE_COLOR = '#d82622'
TEXT_COLOR = ft.colors.BLACK

# Consuming API to fetch daily readings
liturgia = requests.get('https://liturgiadiaria.site/')
liturgia = liturgia.json()

primeira_leitura = liturgia['primeiraLeitura']
salmo = liturgia['salmo']
segunda_leitura = liturgia['segundaLeitura']
evangelho = liturgia['evangelho']


def create_liturgia():
    tabs = []

    # Add 1ª Leitura tab
    tabs.append(
        ft.Tab(
            text='1ª Leitura',
            content=ft.Container(
                padding=ft.padding.all(10),
                content=ft.Text(
                    value=f"{primeira_leitura['titulo']} ({primeira_leitura['referencia']})\n{primeira_leitura['texto']}",
                    color=TEXT_COLOR,
                ),
            ),
        )
    )

    # Add Salmo tab
    tabs.append(
        ft.Tab(
            text='Salmo',
            adaptive=True,
            content=ft.Container(
                padding=ft.padding.all(10),
                content=ft.Text(
                    value=f"{salmo['referencia']}\nRefrão: {salmo['refrao']}\n{salmo['texto']}",
                    color=TEXT_COLOR,
                ),
            ),
        )
    )

    # Check if 'segunda_leitura' exists and add tab if found
    if 'titulo' in segunda_leitura:
        tabs.append(
            ft.Tab(
                text='2ª Leitura',
                content=ft.Container(
                    padding=ft.padding.all(10),
                    content= ft.Text(
                    value=f"{segunda_leitura['titulo']} ({segunda_leitura['referencia']})\n{segunda_leitura['texto']}",
                    color=TEXT_COLOR,
                ),
                ),
            )
        )

    # Add Evangelho tab
    tabs.append(
        ft.Tab(
            text='Evangelho',
            content=ft.Container(
                padding=ft.padding.all(10),
                content=ft.Text(
                    value=f"{evangelho['titulo']} ({evangelho['referencia']})\n{evangelho['texto']}",
                    color=TEXT_COLOR,
                ),
            ),
        )
    )

    return ft.Container(
        content=ft.Column([
            ft.Text(
                value='Liturgia',
                size=24,
                color=TITLE_COLOR,
                weight=ft.FontWeight.W_900,
            ),
            ft.Tabs(
                selected_index=0,
                indicator_color=TITLE_COLOR,
                label_color=TITLE_COLOR,
                tabs=tabs,
                unselected_label_color=TEXT_COLOR,
            ),
        ]),
        visible=True,
    )

