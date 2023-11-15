import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

#side note kivy coordinates start at *bottom* left 0,0
#float layout uses pos_hint which is a dictionary with 6 keys
#    - x, y, top, bottom, left, right
#    - all these keys have a value from 0 to 1
#        - "x":0.5 would move the object 50% to the right

class MyApp(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    MyApp().run()