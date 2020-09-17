from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from pathlib import Path
from kivy.uix.label import Label

class MainPageScreen(Screen):
    pass

class TasksScreen(Screen):
    pass

class CalendarScreen(Screen):
    pass

class TaskApp(App):
    tasks = ["1","2","3","4","5","6","7"]

    def build(self):
        self.pathToKVFile = str(Path("./kv/taskApp.kv")) ## for cross platform file paths
        return Builder.load_file(self.pathToKVFile)

    def change_screen(self,screen_name): #Tested and it works well
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
        if screen_name == "TasksScreen":
            self.populateTasks()

    def populateTasks(self):
        for t in self.tasks:
            self.root.ids.TasksScreen.ids.gL.add_widget(Label(text=str(t)))

if __name__ == "__main__":
    TaskApp().run()