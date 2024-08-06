import flet as ft
from styles import CustomButtom, TextTitulo

def SCJesus():
    print("Clicou no Sagrado Coração de Jesus")

def SantoDia():
    print("Clicou no Santo do Dia")

class DevocoesCarismasPage:
    def __init__(self):
        self.container = ft.Container(
            content=ft.Column([
                TextTitulo.create('Devoções e Carismas'),
                CustomButtom.create('Sagrado Coração de Jesus', SCJesus),
                CustomButtom.create('Santo do Dia', SantoDia),
            ]),
            visible=False
        )
    
    def show(self):
        self.container.visible = True

    def hide(self):
        self.container.visible = False

    def get_container(self):
        return self.container
