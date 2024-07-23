import flet as ft
import requests
import json

# Consuming API to fetch daily readings
liturgia = requests.get('https://liturgiadiaria.site/')
liturgia = liturgia.json()

primeira_leitura = liturgia['primeiraLeitura']
salmo = liturgia['salmo']
evangelho = liturgia['evangelho']

def create_liturgia():
    tabs = []

    # Add 1ª Leitura tab
    tabs.append(
        ft.Tab(
            text='1ª Leitura',
            content=ft.Container(
                bgcolor='#ffffff',
                padding=ft.padding.all(10),
                content=ft.Text(
                    value=f"{primeira_leitura['titulo']} ({primeira_leitura['referencia']})\n{primeira_leitura['texto']}",
                    color='#000000',
                ),
            ),
        )
    )

    # Add Salmo tab
    tabs.append(
        ft.Tab(
            text='Salmo',
            content=ft.Container(
                bgcolor='#ffffff',
                padding=ft.padding.all(10),
                content=ft.Text(
                    value=f"{salmo['referencia']}\nRefrão: {salmo['refrao']}\n{salmo['texto']}",
                    color='#000000',
                ),
            ),
        )
    )

    # Check if 'segunda_leitura' exists and add tab if found
    if 'segunda_leitura' in liturgia:
        segunda_leitura = liturgia['segunda_leitura']
        tabs.append(
            ft.Tab(
                text='2ª Leitura',
                content=ft.Container(
                    bgcolor='#ffffff',
                    padding=ft.padding.all(10),
                    content=ft.Text(
                        value=f"{segunda_leitura['titulo']} ({segunda_leitura['referencia']})\n{segunda_leitura['texto']}",
                        color='#000000',
                    ),
                ),
            )
        )

    # Add Evangelho tab
    tabs.append(
        ft.Tab(
            text='Evangelho',
            content=ft.Container(
                bgcolor='#ffffff',
                padding=ft.padding.all(10),
                content=ft.Text(
                    value=f"{evangelho['titulo']} ({evangelho['referencia']})\n{evangelho['texto']}",
                    color='#000000',
                ),
            ),
        )
    )

    return ft.Container(
        content=ft.Column([
            ft.Text(
                value='Liturgia',
                size=24,
                color='#D82622',
                weight=ft.FontWeight.W_900,
            ),
            ft.Tabs(
                selected_index=0,
                indicator_color='#d82622',
                label_color='#d82622',
                tabs=tabs,
            ),
        ]),
        visible=True,
    )

