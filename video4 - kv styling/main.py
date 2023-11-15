import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

#styling goes in the kv file
#logic goes in the py file
class MyGrid(Widget):
    pass

#note name kv style file the name of the class in lowercase
#unless! that class ends in App which you remove
#so our kv style for this file is called just "my.kv"
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()
