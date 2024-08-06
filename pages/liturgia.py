import flet as ft
import requests

TITLE_COLOR = '#d82622'
TEXT_COLOR = ft.colors.BLACK

class LiturgiaPage:
    def __init__(self):
        self.container = ft.Container(
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
                    tabs=self.get_tabs(),
                    unselected_label_color=TEXT_COLOR,
                ),
            ]),
            visible=True,
        )
    
    def get_tabs(self):
        tabs = []

        response = requests.get('https://liturgiadiaria.site/')
        data = response.json()

        primeira_leitura = data['primeiraLeitura']
        salmo = data['salmo']
        segunda_leitura = data.get('segundaLeitura', {})
        evangelho = data['evangelho']

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

        if 'titulo' in segunda_leitura:
            tabs.append(
                ft.Tab(
                    text='2ª Leitura',
                    content=ft.Container(
                        padding=ft.padding.all(10),
                        content=ft.Text(
                            value=f"{segunda_leitura['titulo']} ({segunda_leitura['referencia']})\n{segunda_leitura['texto']}",
                            color=TEXT_COLOR,
                        ),
                    ),
                )
            )

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

        return tabs
    
    def show(self):
        self.container.visible = True

    def hide(self):
        self.container.visible = False

    def get_container(self):
        return self.container
