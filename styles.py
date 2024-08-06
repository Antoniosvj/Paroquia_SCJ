import flet as ft

BGCOLOR = ft.colors.GREY_50
TITLE_COLOR = '#D82622'
TEXT_COLOR = ft.colors.BLACK

class CustomButtonNav:
    @staticmethod
    def create(text, on_click):
        return ft.TextButton(
            text=text,
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
            ),
            on_click=on_click
        )

class CustomButtom:
    @staticmethod
    def create(text, on_click):
        return ft.ElevatedButton(
            text=text,
            on_click=on_click,
            color=TITLE_COLOR,
            bgcolor=BGCOLOR,
            style=ft.ButtonStyle(side=ft.BorderSide(1, TITLE_COLOR))
        )
        
class TextTitulo:
    @staticmethod
    def create(value):
        return ft.Text(
                    value=value,
                    size=24,
                    color=TITLE_COLOR,
                    weight=ft.FontWeight.W_900,
                )

class TextOracoes:
    @staticmethod
    def create(value):
        return ft.Text(
                value=value,
                color = TEXT_COLOR
        )
 