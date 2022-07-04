from kivymd.uix.boxlayout import MDBoxLayout 
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty
from kivy.clock import Clock

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Dashboard(MDBoxLayout):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.ids.toolbar.ids.label_title.font_name = "assets/font/Daniel Davis.ttf"
        self.ids.toolbar.ids.label_title.font_size = '50sp'
    #     Clock.schedule_once(self.set_toolbar_font_name)
    #     Clock.schedule_once(self.set_toolbar_font_size)

    # def set_toolbar_font_name(self, *args):
    #     self.ids.toolbar.ids.label_title.font_name = "assets/font/Daniel Davis.ttf"

    # def set_toolbar_font_size(self, *args):
    #     self.ids.toolbar.ids.label_title.font_size = '50sp'