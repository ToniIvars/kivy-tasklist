from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty

import tasks_handler

# Register Noto Nerd Font
LabelBase.register(
    name = 'Noto',
    fn_regular = 'fonts/Noto Sans Display Regular Nerd Font Complete.ttf',
    fn_bold = 'fonts/Noto Sans Medium Nerd Font Complete.ttf',
)

class CheckButton(Button):
    task_btn_id = NumericProperty()

    def remove_task(self):
        # Call the method of the main screen with the Button
        # instance and its id as parameters
        main_screen.remove_task(self, self.task_btn_id)

class TaskLabel(Label):
    pass

class MainScreen(Screen):
    def setup(self):
        # Get tasks from the json
        tasks = tasks_handler.get_tasks()

        if tasks:
            for index, text in tasks:
                # Pick the GridLayout
                layout = self.ids.tasks_layout

                # Add the CheckButton for the task
                layout.add_widget(CheckButton(task_btn_id=index))

                # Add the TaskLabel for the task
                task_label = TaskLabel(text=text)
                layout.add_widget(task_label)

                # Update the ids dictionary with the new task
                self.ids[f'task_{index}'] = task_label

        else:
            screen_manager.current = 'add_task_screen'

    def remove_task(self, task_btn, btn_id):
        print(btn_id, self.ids)
        # Get the label of the task
        task_label = self.ids.get(f'task_{btn_id}')

        # Remove the task from the GridLayout
        # self.ids.tasks_layout.remove_widget(task_btn)
        # self.ids.tasks_layout.remove_widget(task_label)

        # Strike the label text and change the color
        task_label.color = 0.424, 0.459, 0.49, 1
        task_label.text = f'[s]{task_label.text}[/s]'

        # Remove task from the json
        tasks_handler.remove_task(btn_id)
        task_btn.disabled = True

    def add_task(self, task_text):
        # Pick the GridLayout
        layout = self.ids.tasks_layout

        # Get the last task id
        new_id = self.get_last_id() + 1

        # Add the CheckButton for the task
        layout.add_widget(CheckButton(task_btn_id=new_id))

        # Add the TaskLabel for the task
        task_label = TaskLabel(text=task_text)
        layout.add_widget(task_label)

        # Update the ids dictionary with the new task
        self.ids[f'task_{new_id}'] = task_label

        # Add task to the json
        tasks_handler.add_task(new_id, task_text)

        print(self.ids)

    def get_last_id(self) -> int:
        if len(self.ids) <= 1:
            return 0

        # Get last key and then its id
        last_task_key = list(self.ids.keys())[-1]
        last_task_id = int(last_task_key.split('_')[-1])

        # Return the id
        return last_task_id

class AddTaskScreen(Screen):
    def add_task(self):
        # Get the text input
        inp = self.ids.new_task_name
        inp_text = inp.text.strip()

        if inp_text:
            # Call the method of the main screen with the text as parameter
            main_screen.add_task(inp_text)

        # Clear the text input
        inp.text = ''

        # Return to the main screen
        screen_manager.transition.direction = 'right'
        screen_manager.current = 'main_screen'

class TasklistApp(App):
    def build(self):
        global main_screen, screen_manager

        # Make dark background
        Window.clearcolor = (0.204, 0.227, 0.251, 1)

        screen_manager = ScreenManager()        

        # Initialize the main screen class
        main_screen = MainScreen(name='main_screen')

        # Add the screens to the manager
        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(AddTaskScreen(name='add_task_screen'))

        # Make the initial setup
        main_screen.setup()

        return screen_manager

if __name__ == '__main__':
    TasklistApp().run()     