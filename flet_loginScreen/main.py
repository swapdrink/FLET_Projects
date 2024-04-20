import flet as ft
from flet import TextField, Text, Row, Column, Checkbox, ElevatedButton, TextButton
from flet_core.control_event import ControlEvent


def main(page: ft.Page) -> None:
    page.title = "Rejestracja"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 400
    page.window_resizable = False
    
    Warunki_Usługi : ft.Container = ft.Container(
                    content=ft.Text("Warunki Usługi"),
                    ink=True,
                    on_click=lambda e: rules()
    )
    
    text_username: TextField = TextField(label='Login', text_align=ft.TextAlign.LEFT, width=200, autofocus=False)
    text_password: TextField = TextField(label='Hasło', text_align=ft.TextAlign.LEFT, width=200, password=True, can_reveal_password=True)
    checkbox_signup: Checkbox = Checkbox(label=f'Zgadzam się na', value=False)
    button_submit: ElevatedButton = ElevatedButton(text='Zarejestruj się', width=200, disabled=True)
    
    company_rules: Text = Text(text_align=ft.TextAlign.LEFT, width=350)
    button_close_rules: TextButton = TextButton(text='Zapoznałem się z treścią regulaminu :)', width=350)
    
    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            button_submit.disabled = False
        else:
            button_submit.disabled = True
            
        page.update()
        
    def submit(e: ControlEvent) -> None:
        print(f'Login: ', text_username.value)
        print(f'Hasło: ', text_password.value)
        
        page.clean()
        page.add(
            Row(
                controls=[Text(value=f'Sukces!! \n\nLogin: {text_username.value} \nHasło: {text_password.value}', size=20, )],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        
    def rules() -> None:
        page.clean()
        with open('regulamin.txt', 'r', encoding='utf-8') as Company_Policy:
            company_rules.value = (Company_Policy.read())
            page.add(
                Row(controls=[
                    Column(controls=[
                        company_rules,
                        button_close_rules
                        ]
                    )],
                    alignment=ft.MainAxisAlignment.CENTER      
                )
            )

    def login(e:ControlEvent = None) -> None: 
        page.clean() 
        page.add(
            Row(controls=[
                Column(controls=[ 
                        text_username,
                        text_password,
                        Row(controls=[
                            checkbox_signup,
                            Warunki_Usługi
                            ],
                        ),
                        button_submit
                    ])
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
        
    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    button_submit.on_click = submit
    
    button_close_rules.on_click = login
    
    login()
    

if __name__ == '__main__':
    ft.app(target=main) 