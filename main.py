from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.core.text import LabelBase

# Register Noto Nerd Font
LabelBase.register(
    name = 'Noto',
    fn_regular = 'fonts/Noto Sans Display Regular Nerd Font Complete.ttf',
    fn_bold = 'fonts/Noto Sans Medium Nerd Font Complete.ttf',
)

class CheckButton(Button):
    def remove_task(self):
        # Get the label of the task
        task_label = main_layout.ids.get(f'task_{self.task_btn_id}')

        # Get the button of the task
        task_btn = self

        # Remove the task from the GridLayout
        # main_layout.ids.tasks_layout.remove_widget(task_btn)
        # main_layout.ids.tasks_layout.remove_widget(task_label)

        # Strike the label text and change the color
        task_label.color = 0.424, 0.459, 0.49, 1
        task_label.text = f'[s]{task_label.text}[/s]'

class TaskLabel(Label):
    pass

class MainLayout(Widget):
    def add_task(self):
        pass

class TasklistApp(App):
    def build(self):
        global main_layout

        # Make dark background
        Window.clearcolor = (0.204, 0.227, 0.251, 1)

        main_layout = MainLayout()
        return main_layout

if __name__ == '__main__':
    TasklistApp().run()     