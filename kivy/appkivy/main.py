from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
#apllications.appkivy.
from canvas_exemples import *
from navigation_screen_manager import NavigationSreenManager


# from kivy.config import Config
# Config.set("kivy", "log_level", "error")
# Config.write()

class MyScreenManager(NavigationSreenManager):
    pass
class LelabApp(App):# le fichier kv doit avoir comme nom "Lelab.kv"
    """
    application
    """
    manager = ObjectProperty(None)
    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        #return CanvasExemple1()
        #return CanvasExemple2()
        #return CanvasExemple3()
        #return CanvasExemple4()
        #return CanvasExemple5()
        #return CanvasExemple6()
        #return CanvasExemple7()

LelabApp().run()