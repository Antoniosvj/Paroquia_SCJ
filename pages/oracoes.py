import flet as ft

def create_oracoes():
    return ft.Container(
        content=ft.Column([
            ft.Text(
                value='Orações',
                size=24,
                color='#D82622',
                weight=ft.FontWeight.W_900,
            ),
            ft.ElevatedButton(
                text='Oração a São Lourenço',
                color='#d82622',
            ),
            ft.ElevatedButton(
                text='Santo Terço',
                color='#d82622',
            ),
        ]),
        visible=False,
    )

