from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.gridlayout import GridLayout

Builder.load_file("widget_exemples.kv")


class WidgetsExemple(GridLayout):
    #obligatoire de passer par les proprietes afin de les utiliser dans kv
    mon_texte = StringProperty("1")
    compteur = 1
    compteur_actif = BooleanProperty(False)
    slider_value_txt = StringProperty("1")
    text_input_str = StringProperty("toto")
    def on_button_click(self):
        if self.compteur_actif:
            self.compteur = self.compteur+1
            self.mon_texte = str(self.compteur)


    def on_toggle_button_state(self,widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.compteur_actif = False
        else:
            widget.text = "ON"
            self.compteur_actif = True


    def on_switch_activate(self,widget):
        print(str(widget.active))


    def on_slider_value(self,widget):
        self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self,widget):
        self.text_input_str = widget.text