from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.core.text import LabelBase

LabelBase.register(
    name = 'Noto',
    fn_regular = 'fonts/Noto Sans Display Regular Nerd Font Complete.ttf',
    fn_bold = 'fonts/Noto Sans Medium Nerd Font Complete.ttf',
)

from kivy.uix.button import Button

class CheckButton(Button):
    def click(self):
        print(self.id)

class TaskLabel(Label):
    pass

class MainLayout(Widget):
    def add_task(self):
        print(f'Btn pressed')

class TasklistApp(App):
    def build(self):
        global main_layout
        Window.clearcolor = (0.204, 0.227, 0.251, 1)

        main_layout = MainLayout()
        return main_layout

if __name__ == '__main__':
    TasklistApp().run()     