import flet as ft
from flet import Page, Row, Text, KeyboardEvent

def main(page: ft.Page) -> None:
    page.title = "Keyboard Detector"
    page.spacing = 30
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    
    key: Text = Text('Key', size=30)    
    shift: Text = Text('Shift', size=30, color='red')    
    ctrl: Text = Text('Control', size=30, color='blue')    
    alt: Text = Text('Alt', size=30, color='green')    
    meta: Text = Text('Meta', size=30, color='yellow')    

    def on_keyboard(e: KeyboardEvent,) -> None:
        key.value = e.key
        if (key.value == " "): key.value = "Space"
        shift.visible = e.shift
        ctrl.visible = e.ctrl
        alt.visible = e.alt
        meta.visible = e.meta
        print(e.data)
        
        page.update()
        
    page.on_keyboard_event = on_keyboard
    
    page.add(
        Text('Press any combination of keys...'),
        Row(controls=[key,shift,ctrl,alt,meta],
            alignment=ft.MainAxisAlignment.CENTER),
    )
    


if __name__ == "__main__":
    ft.app(target=main)