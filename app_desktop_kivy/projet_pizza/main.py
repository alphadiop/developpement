from kivy.app import App
from kivy.lang import Builder
from kivy.properties import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior
from kivy.uix.widget import Widget

from storage_manager import StorageManager
from http_client import HttpClient
from models import Pizza


class PizzaWidget(BoxLayout):
    nom = StringProperty()
    ingredients = StringProperty()
    prix = NumericProperty()
    vegetarienne = BooleanProperty()


# initialisation du model
class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str = StringProperty("")


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        """self.pizzas = [
            Pizza("4 Fromages","Chèvre, Emmental, Brie",9.5,True),
            Pizza("Chorizo", "Tomates, Chorizo, Parmesan", 9.5, False),
            Pizza("Chevres", "Chèvre, Emmental, Brie", 9.5, True),
            Pizza("Calzone", "Fromage, Jambon, Chamignons", 9.5, False)
        ]"""
        #HttpClient().get_pizzas(self.on_server_data)
        HttpClient().get_pizzas(self.on_server_data,self.on_server_error) # c'est une méthode pour récuperer des données réseaux

    def on_parent(self,widget,parent):
        #pizzas_dict = [pizza.get_dictionary() for pizza in self.pizzas]
        pizzas_dict = StorageManager().load_data(data_name = "pizzas")
        if pizzas_dict:
            self.recycleView.data = pizzas_dict


    def on_server_data(self,pizzas_dict):
        self.recycleView.data = pizzas_dict
        StorageManager().save_data(data_name="pizzas",data_content=pizzas_dict)

    def on_server_error(self,error):
        print("ERREUR :" + error)
        self.error_str = "ERREUR :" + error




# application
with open("pizza_scr.kv",encoding='utf8') as f:
    Builder.load_string(f.read())
class PizzaApp(App):
    """
    Maintenant que le fichier kv a été renommé
    Faut dire à l'application de charger l'interface principale qui est MainWidget
    """
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    PizzaApp().run()
