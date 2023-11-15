import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        #the outer grid cols is equal to 1
        #this allows to center the button
        self.cols = 1

        #create an inner grid with 2 cols
        self.inside = GridLayout()
        self.inside.cols = 2

        #adding labes and text entry to the inner grid
        self.inside.add_widget(Label(text="First Name: "))
        self.first_name = TextInput(multiline=False)
        self.inside.add_widget(self.first_name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.last_name = TextInput(multiline=False)
        self.inside.add_widget(self.last_name)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        #add inner grid to outer grid
        self.add_widget(self.inside)

        #add button to outer grid
        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    # defining the function which will occur on button press
    def pressed(self, instance):
        #collecting the inputs from each field
        name = self.first_name.text
        last = self.last_name.text
        email = self.email.text

        #output to the consol
        print("Name: ", name, "Last name: ", last, "Email: ", email)

        #clear the text from the fields
        self.first_name.text = ""
        self.last_name.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()
