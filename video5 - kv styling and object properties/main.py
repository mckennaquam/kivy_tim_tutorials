import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

#styling goes in the kv file
#logic goes in the py file

# in the kv file when writing object properties the left
# is the name you will refernce in py and the right is
# the id name for the kv file
class MyGrid(Widget):
    #setting up the varibles
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    #defining the function which will be bound to the button
    #note in the kv file we say "on_pressed: root.btn()" as MyGrid
    #is the root class for the styling
    def btn(self):
        print("Name: ", self.name.text, "Email: ", self.name.text)
        self.name.text = ""
        self.email.text = ""

#note name kv style file the name of the class in lowercase
#unless! that class ends in App which you remove
#so our kv style for this file is called just "my.kv"
class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()
