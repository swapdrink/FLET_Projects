import flet as ft
from flet import UserControl, Text, Row, Page, ControlEvent, MainAxisAlignment, ElevatedButton

class IncrementCounter(UserControl):
    def __init__(self, text: str, start_number: int = 0) -> None:
        super().__init__()
        self.text = text
        self.counter = start_number
        self.text_number: Text = Text(value=str(start_number), size=(start_number // 10) * 8 + 15)
        
    def increment(self, e: ControlEvent) -> None:
        self.counter += 1
        self.text_number.value = str(self.counter)
        if(self.counter % 10 == 0): 
            self.text_number.size += 8
        self.update()

    def build(self) -> Row:
        return Row(controls=[ElevatedButton(self.text, on_click=self.increment),
                             self.text_number],
                   alignment=MainAxisAlignment.SPACE_BETWEEN,
                   width=300)



def main(page: ft.Page):
    page.title = 'Increment Counter Using Multiple Classes'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False
    
    
    page.add(IncrementCounter('Ludzie'))
    page.add(IncrementCounter('Kamyki', 13))
    page.add(IncrementCounter('Słonie', 38))

if __name__ == '__main__':
    ft.app(target=main)