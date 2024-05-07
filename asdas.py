from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        l1 = Label(text='Login', font_size=100, font_name='Arial')

        layout.add_widget(l1)

        return layout

if __name__ == '__main__':
    MinhaApp().run()
