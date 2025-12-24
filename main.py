from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class MainScreen(BoxLayout):
    status_text = StringProperty("Очікування...")

    def update_status(self, btn_text):
        self.status_text = f"Натиснуто: {btn_text}"


class SuperApp(App):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    SuperApp().run()
