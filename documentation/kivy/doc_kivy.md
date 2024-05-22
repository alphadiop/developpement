https://kivy.org/
https://jsoneditoronline.org
une liste de dictionnaire = json

https://cegedim-france.udemy.com/course/developpeur-python-formation-complete/learn/lecture/20825396#overview

Section 53 de la formation
Developpement d'application bureau, mobile pour un même code source python
Editerur : Visual Studio Code
Installation kiv : pip install kivy attention, conda install ne marche pas
liste des packages installés : pip list
pip install pylint


python -m pip install --upgrade pip

Etape apprentissage kivy
1. Création du projet et structure de base
2. Affichage des contrôles (Widgets)
	1. BoxLayout
	2. AnchorLayout
	3. GridLayout
	4. StackLayout
	5. ScrollView
	6. PageLayout
3. Stratégie de placement (Layouts)


Faut toujours que le nom de la class heritant la classe App du coté python soit le meme pour le nom du fichier kv
Exemple :
main.py
class LelabApp(App):
    pass

Lelab.kv
dans ce fichier, les ecrants eligibles à ecran principale sont : MainVidget ou BoxLayoutExemple
autrement dit, il faut toujours definir un ecarn principal dans le fichier kv
par MainVidget : ou BoxLayoutExemple:

class MainVidget(Widget):
    pass

class BoxLayoutExemple(BoxLayout):
    pass


