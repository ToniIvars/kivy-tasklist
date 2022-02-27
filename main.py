from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen

# Register Noto Nerd Font
LabelBase.register(
    name = 'Noto',
    fn_regular = 'fonts/Noto Sans Display Regular Nerd Font Complete.ttf',
    fn_bold = 'fonts/Noto Sans Medium Nerd Font Complete.ttf',
)

class CheckButton(Button):
    def remove_task(self):
        # Call the method of the main screen with the Button
        # instance and its id as parameters
        main_screen.remove_task(self, self.task_btn_id)

class TaskLabel(Label):
    pass

class MainScreen(Screen):
    def remove_task(self, task_btn, btn_id):
        # Get the label of the task
        task_label = self.ids.get(f'task_{btn_id}')

        # Remove the task from the GridLayout
        # self.ids.tasks_layout.remove_widget(task_btn)
        # self.ids.tasks_layout.remove_widget(task_label)

        # Strike the label text and change the color
        task_label.color = 0.424, 0.459, 0.49, 1
        task_label.text = f'[s]{task_label.text}[/s]'

class AddTaskScreen(Screen):
    def add_task(self):
        screen_manager.transition.direction = 'right'
        screen_manager.current = 'main_screen'

class TasklistApp(App):
    def build(self):
        global main_screen, screen_manager

        # Make dark background
        Window.clearcolor = (0.204, 0.227, 0.251, 1)

        main_screen = MainScreen(name='main_screen')

        screen_manager = ScreenManager()

        # Add the screens to the manager
        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(AddTaskScreen(name='add_task_screen'))

        return screen_manager

if __name__ == '__main__':
    TasklistApp().run()     