import flet as ft

def create_contatos():
    return ft.Container(
        content=ft.Column([
            ft.Text(
                value='Contatos',
                size=24,
                color='#D82622',
                weight=ft.FontWeight.W_900,
            ),
            ft.Image(
               src='https://img.icons8.com/?size=70&id=Xy10Jcu1L2Su&format=png&color=000000'
            ),
            ft.Image(
                src='https://img.icons8.com/?size=70&id=16712&format=png&color=94D82D'
            ),
                   
                               
            
        ]),
        visible=False,
    )

