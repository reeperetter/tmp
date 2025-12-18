from kivy.uix.actionbar import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

def my_callback(dt):
    print("Working!!!")

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="User Name"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text="Password"))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

    event = Clock.schedule_once(my_callback, 3)
    trigger = Clock.create_trigger(my_callback)
    trigger()


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        btn = Button(text="Button 1")
        btn.bind()
        self.add_widget(btn)
        self.add_widget(Button(text="Button 2"))
    
    def btn_pressed(self, instance, pos):
        print('pos: printed from root widget: {pos}'.format(pos=.pos))


class MyApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MyApp().run()
