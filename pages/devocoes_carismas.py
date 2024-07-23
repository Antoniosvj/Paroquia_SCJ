import flet as ft

def create_devocoes_carismas():
    return ft.Container(
        content= ft.Column([
            ft.Text(
                value='Devoções e Carismas',
                size=24,
                color='#D82622',
                weight=ft.FontWeight.W_900,
            ),
            ft.ElevatedButton(
                text='Sagrado Coração de Jesus',
                color='#d82622',
            ),
            ft.ElevatedButton(
                text='Santo do Dia',
                color='#d82622',
            ),
        ]),
        visible=False
    )
