import flet as ft
from flet import TextField
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:
    page.title = "Increment Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = "dark"
    
    text_number: ft.Text = ft.Text(value=0, text_align=ft.TextAlign.CENTER, 
                                   color=ft.colors.RED, width=100, size=33)
    
    def decrement(e: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) - 1)
        change_color_number(e)
        page.update()

    def increment(e: ControlEvent) -> None:
        text_number.value = str(int(text_number.value) + 1)
        change_color_number(e)
        page.update()
        
    def change_color_number(e: ControlEvent) -> None:
        if int(text_number.value) % 7 == 0 : text_number.color = ft.colors.RED
        if int(text_number.value) % 7 == 1 : text_number.color = ft.colors.TEAL
        if int(text_number.value) % 7 == 2 : text_number.color = ft.colors.PINK
        if int(text_number.value) % 7 == 3 : text_number.color = ft.colors.GREEN
        if int(text_number.value) % 7 == 4 : text_number.color = ft.colors.PURPLE  
        if int(text_number.value) % 7 == 5 : text_number.color = ft.colors.BLUE
        if int(text_number.value) % 7 == 6 : text_number.color = ft.colors.YELLOW
    
    
    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, icon_size=40, on_click = decrement),
                text_number,
                ft.IconButton(ft.icons.ADD, icon_size=40, on_click = increment)
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


if __name__ == "__main__":
    ft.app(target=main,
         # view=ft.AppView.WEB_BROWSER
        )