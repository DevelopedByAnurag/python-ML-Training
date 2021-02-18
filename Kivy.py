import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Name: "))  # Add a label widget 
        self.name = TextInput(multiline=False)  # Create a Text input box stored in the name variable
        self.add_widget(self.name)  # Add the text input widget to the GUI


class MyApp(App):
    def build(self):
       return MyGrid()
    pass


if __name__ == "__main__":
    MyApp().run()
