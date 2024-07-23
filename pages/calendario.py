import flet as ft

def create_calendario():
    return ft.Container(
        content=ft.Column([
            ft.Text(
                value='Calendário',
                size=24,
                color='#D82622',
                weight=ft.FontWeight.W_900,
            ),
            
        ]),
        visible=False,
    )

