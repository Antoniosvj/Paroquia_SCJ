import flet as ft
import time
from liturgia import pagina_liturgia 

def main(page:ft.Page):
    
    #layout abertura
    image_layout = ft.Container(
        width=350,
        margin=ft.margin.all(30),
        content= ft.Image(
            src='icon.png',
            width=100,
        )
    )
    #page.add(image_layout)
    time.sleep(3)

    #controles
    liturgia = ft.Container(
        content = ft.Container(
            #carregarconteudo liturgia
            ft.Text(value='Liturgia'),
        ),
        visible=True
    )
    oracoes = ft.Container(
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
    def show_liturgia(e):
        liturgia.visible = True
        oracoes.visible = False
        devocoesCarismas.visible = False
        calendario.visible = False
        contatos.visible = False
        page.update()

        
    def show_oracoes(e):
        liturgia.visible = False
        oracoes.visible = True
        devocoesCarismas.visible = False
        calendario.visible = False
        contatos.visible = False
        page.update()
    
    def show_devocoes_carismas(e):
        liturgia.visible = False
        oracoes.visible = False
        devocoesCarismas.visible = True
        calendario.visible = False
        contatos.visible = False
        page.update()
        
    def show_calendario(e):
        liturgia.visible = False
        oracoes.visible = False
        devocoesCarismas.visible = False
        calendario.visible = True
        contatos.visible = False
        page.update()
    
    def show_contatos(e):
        liturgia.visible = False
        oracoes.visible = False
        devocoesCarismas.visible = False
        calendario.visible = False
        contatos.visible = True
        page.update()    

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
                ft.TextButton(
                    col=4,
                    on_click=show_liturgia,
                    content = ft.Text(
                        value='Liturgia',
                        color= '#ffffff',
                        size=12,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ),
                ft.TextButton(
                    col=4,
                    on_click=show_oracoes,
                    content = ft.Text(
                        value="Orações",
                        color="#ffffff",
                        size=12,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ),
                ft.TextButton(
                    col=4,
                    on_click=show_devocoes_carismas,
                    content = ft.Text(
                        value='Devoção\ne Carisma',
                        color='#ffffff',
                        size=12,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    
                    )
            ]
        )
    )
    
    #parte principal
    main_content = ft.Container(
        width=520,
        margin=ft.margin.all(15),
        content= ft.Column(
            controls=[
            liturgia,
            oracoes,
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
                ft.TextButton(
                    col=6,
                    on_click=show_calendario,
                    content = ft.Text(
                        value='Calendário',
                        color= '#ffffff',
                        size=12,
                        text_align=ft.TextAlign.CENTER,
                    ),
                ),
                ft.TextButton(
                    col=6,
                    on_click=show_contatos,
                    content = ft.Text(
                        value='Contatos',
                        color= '#ffffff',
                        size=12,
                        text_align=ft.TextAlign.CENTER,
                        ),
                ),
            ]
        )
    )
    
    layout = ft.Container(
        width=520,
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