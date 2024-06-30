import flet as ft
import time

def main(page:ft.Page):
    
    #layout abertura
    image_layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        content= ft.Image(
            src='icon.png',
            width=100,
        )
    )
#    page.add(image_layout)
    time.sleep(3)

    #controles
    liturgia = ft.Container(
        content = ft.Text(value='Liturgia'),
        visible=True
    )
    Oracoes = ft.Container(
        content = ft.Text(value='Orações'),
        visible=False
    )
    devocoesCarismas = ft.Container(
        content = ft.Text(value='Devoções e Carismas'),
        visible=False
    )
    calendario = ft.Container(
        content = ft.Text(value='Calendário'),
        visible=False
    )
    contatos = ft.Container(
        content = ft.Text(value='Contatos Úteis'),
        visible=False
    )
    #mostrar telas
    def show_calendario():
        pass

    #Cabeçalho
    header = ft.Container(
        bgcolor = '#000000',
        padding = ft.padding.all(15),
        border_radius=ft.border_radius.only(
            top_left=0,
            top_right=0,
            bottom_right=6,
            bottom_left=6,
        ),
        content = ft.ResponsiveRow(
            columns=12,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment='spaceBetween',
            controls=[
                ft.Text(
                    col=4,
                    value='Liturgia',
                    color= '#ffffff',
                    size=12,
                    text_align=ft.TextAlign.CENTER,
                    ),
                ft.Text(
                    col=4,
                    value='Orações',
                    color= '#ffffff',
                    size=12,
                    text_align=ft.TextAlign.CENTER,
                    ),
                ft.Text(
                    col=4,
                    value='Devoções\ne Carismas',
                    color= '#ffffff',
                    size=12,
                    text_align=ft.TextAlign.CENTER,
                    )
            ]
        )
    )
    
    #parte principal
    main_content = ft.Container(
        width=900,
        margin=ft.margin.all(15),
        content= ft.Column(
            controls=[
            liturgia,
            Oracoes,
            devocoesCarismas,
            calendario,
            contatos
            ]
        )
    )
    
    #rodapé
    footer = ft.Container(
        bgcolor = '#000000',
        padding = ft.padding.all(15),
        border_radius=ft.border_radius.only(
            top_left=6,
            top_right=6,
            bottom_right=0,
            bottom_left=0,
        ),
        content = ft.ResponsiveRow(
            columns=12,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            alignment='spaceBetween',
            controls=[
                ft.Text(
                    col=6,
                    value='Calendário',
                    color= '#ffffff',
                    size=12,
                    text_align=ft.TextAlign.CENTER,
                    ),
                ft.Text(
                    col=6,
                    value='Contatos Úteis',
                    color= '#ffffff',
                    size=12,
                    text_align=ft.TextAlign.CENTER,
                    ),
            ]
        )
    )
    
    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        content= ft.Column(
            controls=[
            header,
            main_content,
            footer
            ]
        )
    )
#    page.remove(image_layout)
    page.add(layout)
    
if __name__ == '__main__':
    ft.app(target=main)