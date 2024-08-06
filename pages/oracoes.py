import flet as ft
import json
from styles import CustomButtom, TextTitulo, TextOracoes

class OracoesPage:
    def __init__(self):
        with open('oracoes.json', 'r', encoding='utf-8') as f:
            self.oracoes = json.load(f)
        self.container = ft.Container(
            content=ft.Column([
                TextTitulo.create('Orações'),
                CustomButtom.create(self.oracoes['SLourenco']['titulo'], on_click=self.show_Slourenco),
                CustomButtom.create('Oração do Santo Terço', on_click=self.show_Sterco),
                CustomButtom.create(self.oracoes['SMiguel']['titulo'], on_click=self.show_SMiguel),
                
            ]),
            visible=False,
        )
        
    def show_Slourenco(self, e):
        self.container.content.controls = [
            TextTitulo.create(self.oracoes['SLourenco']['titulo']),
            TextOracoes.create(self.oracoes['SLourenco']['oracao']),
            CustomButtom.create('Voltar', on_click=self.show_oracoes_page)
        ]
        e.control.page.update()
        
    def show_SMiguel(self, e):
        self.container.content.controls = [
            TextTitulo.create(self.oracoes['SMiguel']['titulo']),
            TextOracoes.create(self.oracoes['SMiguel']['oracao']),
            CustomButtom.create('Voltar', on_click=self.show_oracoes_page)
        ]
        e.control.page.update()

        
    def show_Sterco(self, e):
        ...
     
    def show_oracoes_page(self, e):
        ...
       
    def show(self):
        self.container.visible = True

    def hide(self):
        self.container.visible = False

    def get_container(self):
        return self.container
