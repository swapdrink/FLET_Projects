from flet import (UserControl,
                  TextField,
                  InputBorder,
                  Page,
                  ControlEvent,
                  app)
import flet as ft
from threading import Timer
from time import sleep

class TextEditor(UserControl):
    def __init__(self) -> None:
        super().__init__()
        self.textfield = TextField(multiline=True,
                                   autofocus=True,
                                   border=InputBorder.NONE,
                                   min_lines=40,
                                   on_focus = self.save_text,
                                   content_padding=30,
                                   cursor_color='yellow',
                                   focused_border_color = 'PINK '
                                   )
    def save_text(self, e: ControlEvent) -> None:
        sleep(5.0)
        with open('save.txt', 'w') as f:
            f.write(self.textfield.value)
            print("File has been saved!")
            self.save_text(e)
                       
    def read_text(self) -> str | None:
        try:
            with open('save.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            self.textfield.hint_text = "Welcome to the text editor!"
            
    def build(self) -> TextField:
        self.textfield.value = self.read_text()
        return self.textfield
    
      
def hide_button(e: ControlEvent) -> None:
    e.visible = False
         

def main(page: ft.Page) -> None:
    page.title = 'Notepad in Flet'
    page.scroll = True
    
    button = ft.ElevatedButton(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(value="file has been saved", size=20)
                        ]
                    ),
                    padding=ft.padding.all(10)
                ),
                visible=True,
                on_click=hide_button,
            )
    
    st = ft.Stack(
        [
            TextEditor(),
            ft.Container(
                button,
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]
    )
    
    page.add(st)
    # page.add(TextEditor())
        

if __name__ == "__main__":
    ft.app(target=main)