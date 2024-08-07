import flet as ft
import json
from styles import CustomButtom, TextTitulo, TextOracoes

class OracoesPage:
    def __init__(self):
        with open('oracoes.json', 'r', encoding='utf-8') as f:
            self.oracoes = json.load(f)
        self.container = ft.Container(
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
                controls=[]        
            ),
            visible=False, 
        )
        self.set_inicial_content()
        
    def set_inicial_content(self):
        self.container.content.controls = [
            TextTitulo.create('Orações'),
            CustomButtom.create(self.oracoes['SLourenco']['titulo'], on_click=self.show_Slourenco),
            CustomButtom.create(self.oracoes['STerco']['titulo'], on_click=self.show_Sterco),
            CustomButtom.create(self.oracoes['SMiguel']['titulo'], on_click=self.show_SMiguel),
            CustomButtom.create(self.oracoes['Apostolado']['titulo'], on_click=self.show_apostolado),    
        ]
    
    def show_apostolado(self, e):
        self.container.content.controls = [
            TextTitulo.create(self.oracoes['Apostolado']['titulo']),
            TextOracoes.create(self.oracoes['Apostolado']['oracao']),
            CustomButtom.create('Voltar', on_click=self.show_oracoes_page)
        ]
        e.control.page.update()
    
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
        self.container.content.controls = [
            TextTitulo.create(self.oracoes['STerco']['titulo']),
            TextOracoes.create(self.oracoes['STerco']['inicio']),
            TextOracoes.create(self.oracoes['STerco']['misterios']),
            TextOracoes.create(self.oracoes['STerco']['final']),
            CustomButtom.create('Voltar', on_click=self.show_oracoes_page),
            ft.Tabs(
                selected_index=0,
                indicator_color='#d82622',
                label_color='#d82622',
                tabs=self.get_tabs(),
                unselected_label_color=ft.colors.BLACK,
            )          
        ]
        e.control.page.update()

    def get_tabs(self):
        tabs = [
            ft.Tab(
                text=self.oracoes['STerco']['contemplacoes']['misteriosGozosos']['misterio'],
                content=ft.Column(
                    controls=[
                        ft.Text(value=self.oracoes['STerco']['contemplacoes']['misteriosGozosos']['dia']),
                        ft.Text(value=self.oracoes['STerco']['contemplacoes']['misteriosGozosos']['contemplacao']),
                    ]
                ),
            ),
            ft.Tab(
                text=self.oracoes['STerco']['contemplacoes']['misteriosDolorosos']['misterio'],
                content=ft.Column(
                    controls=[
                        ft.Text(value=self.oracoes['STerco']['contemplacoes']['misteriosDolorosos']['dia']),
                        ft.Text(value=self.oracoes['STerco']['contemplacoes']['misteriosDolorosos']['contemplacao']),
                    ]
                ),
            ),
            ft.Tab(
                text=self.oracoes['STerco']['contemplacoes']['misteriorGloriosos']['misterio'],
                content=ft.Column(
                    controls=[
                        ft.Text(value=self.oracoes['STerco']['contemplacoes']['misteriorGloriosos']['dia']),
                        ft.Text(value=self.oracoes['STerco']['contemplacoes']['misteriorGloriosos']['contemplacao']),
                    ]
                ),
            ),
            ft.Tab(
                text=self.oracoes['STerco']['contemplacoes']['misteriosLuminosos']['misterio'],
                content=ft.Column(
                    controls=[
                        ft.Text(value=self.oracoes['STerco']['contemplacoes']['misteriosLuminosos']['dia']),
                        ft.Text(value=self.oracoes['STerco']['contemplacoes']['misteriosLuminosos']['contemplacao']),
                    ]
                ),
            )
        ]
        return tabs
         
    def show_oracoes_page(self, e):
        self.set_inicial_content()
        e.control.page.update()
       
    def show(self):
        self.container.visible = True

    def hide(self):
        self.container.visible = False

    def get_container(self):
        return self.container
