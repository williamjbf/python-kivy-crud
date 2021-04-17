from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Principal(BoxLayout):
    pass

class Crud(App):
    def build(self):
        return Principal()

Crud().run()
