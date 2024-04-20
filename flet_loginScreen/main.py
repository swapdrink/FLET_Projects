import flet as ft
from flet import TextField, Text, Row, Column, Checkbox, ElevatedButton
from flet_core.control_event import ControlEvent


def main(page: ft.Page) -> None:
    page.title = "Rejestracja"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False
    
    text_username: TextField = TextField(label='Login', text_align=ft.TextAlign.LEFT, width=200, autofocus=False)
    text_password: TextField = TextField(label='Hasło', text_align=ft.TextAlign.LEFT, width=200, password=True, can_reveal_password=True)
    checkbox_signup: Checkbox = Checkbox(label='Zgadzam się na {warunki usługi}', value=False)
    button_submit: ElevatedButton = ElevatedButton(text='Zarejestruj się', width=200, disabled=True)
    
    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
            
        page.update()
        
    def submit(e: ControlEvent) -> None:
        print(f'Login', text_username.value)
        print(f'Hasło', text_password.value)
        
        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Witaj: {text_username.value}, {text_password.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        
    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit
        
    page.add(
        Row(
             controls=[
                  Column(
                     [text_username,
                      text_password,
                      checkbox_signup,
                       button_submit],
                  )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
        
        



if __name__ == '__main__':
    ft.app(target=main) 