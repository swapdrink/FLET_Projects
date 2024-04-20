from flet import ( UserControl, TextField, InputBorder,
                   IconButton, ThemeMode, Page,
                   Text, Icon, icons, ButtonStyle, 
                   colors, ControlEvent, AppBar, app
                 )
from os import path, remove

#from threading import Timer
#from time import sleep             // eksperymentalne


txtfield = TextField( multiline=True,
                      autofocus=True,
                      border=InputBorder.NONE,
                      min_lines=40,
                      content_padding=30,
                      hint_text='Wprowadź tekst',
                      cursor_color='yellow',
                      focused_border_color='pink'
                    )
                 

def main(page: Page) -> None:
    page.title = 'Notepad FLET'
    page.scroll = True
    page.theme_mode = ThemeMode.DARK
    
    def changeTheme(e: ControlEvent) -> None:
        page.theme_mode = (
            ThemeMode.LIGHT
            if page.theme_mode == ThemeMode.DARK
            else ThemeMode.DARK
        )
        change_cursor_color()
        
        toggleButton.selected = not toggleButton.selected
        page.update()
        
    def change_cursor_color() -> None:
        if txtfield.cursor_color == 'yellow': txtfield.cursor_color = 'blue'
        else :                                txtfield.cursor_color = 'yellow'
        
    toggleButton = IconButton( on_click=changeTheme,
                               icon=icons.LIGHT_MODE_OUTLINED,
                               selected_icon='nightlight',
                               style=ButtonStyle(color={'':colors.WHITE, 
                                                        'selected':colors.BLACK})
                             )
    
    def save_text(e: ControlEvent) -> None:
        with open('save.txt', 'w') as f:
            f.write(txtfield.value)
            
            if(txtfield.value == "crash me pls"):
                if path.exists("./save.txt"):
                    f.close()
                    remove("save.txt")
                else:
                    print("Plik nie odnaleziony!")
                  
    def read_text() -> str | None:
        try:
            with open('save.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            txtfield.hint_text = "Witaj w edytorze tekstu!"
            
    txtfield.on_change = save_text
            
    def build() -> TextField:
        txtfield.value = read_text()
        return txtfield
    
    build()
    
    page.add(
        AppBar(
            leading=Icon(icons.TEXT_SNIPPET),
            title=Text("Notepad"),
            actions=[toggleButton],
            bgcolor=colors.SURFACE_VARIANT
        ))
    page.add(txtfield)
    
        

if __name__ == "__main__":
    app(target=main)