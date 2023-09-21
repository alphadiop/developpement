from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

Builder.load_file("layout_exemples.kv")

class StackLayoutExemple(StackLayout):
    """
    ordre d'appel : python puis fichier kv
    """
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(0,150):
            #z = Button(text=str(i+1),size_hint=(.2,.2))
            z = Button(text=str(i + 1), size_hint=(None,None),size = (dp(60),dp(60)))
            self.add_widget(z)



class MainVidget(Widget):
    pass

# class GridLayoutExemple(GridLayout):
#     pass

class AnchorLayoutExemple(AnchorLayout):
    pass


class BoxLayoutExemple(BoxLayout):
    pass
    """
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    """
