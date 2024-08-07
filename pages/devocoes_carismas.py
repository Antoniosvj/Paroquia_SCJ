import flet as ft
import json
from styles import CustomButtom, TextTitulo, TextOracoes

class DevocoesCarismasPage:
    def __init__(self):
        with open('devocoes.json', 'r', encoding='utf-8') as f:
            self.devocoes = json.load(f)
        
        self.container = ft.Container(
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                controls=[]
            ),
            visible=False
        )
        self.set_inicial_content()
        
    def set_inicial_content(self):
        self.container.content.controls = [
            TextTitulo.create('Devoções e Carismas'),
            CustomButtom.create(self.devocoes['SCJesus']['titulo'], on_click=self.show_SCJesus),
            CustomButtom.create('Santo do Dia', on_click=self.show_SantoDia),
            
        ]
        
    def show_SCJesus(self, e):
        self.container.content.controls = [
            TextTitulo.create(self.devocoes['SCJesus']['titulo']),
            TextOracoes.create(self.devocoes['SCJesus']['devocao'])
        ]
        e.control.page.update()
    
    def show_SantoDia(self, e):
        self.container.content.controls = [
            TextTitulo.create('Santo do dia'),
        ]
        e.controls.page.update()
        
    def show_devocoes_page(self, e):
        self.set_inicial_content()
        e.control.page.update()
    
    def show(self):
        self.container.visible = True

    def hide(self):
        self.container.visible = False

    def get_container(self):
        return self.container
