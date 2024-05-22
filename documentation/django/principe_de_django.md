Frame work = cadre de travail
migration sur django = modifier la structure interne de la base de données

python manage.py startapp main
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
compte : diop
email : alphadiop@gmail.com
Mdp : Ibrahima1

django admin change language
add django.middleware.locale.LocaleMiddleware in setting.py and in MIDDLEWARE

bien afficher la base dans interface admin

definir une classe PizzaAdmin
list_display = ('nom', 'ingredients', 'vegetarienne', 'prix')
search_fields = ['nom']

comment charger un fichier html ?
render : permet d'appeler un template

templates >> Menu >> index.html


static >> Menu >> style.css
comment charger un fichier css depuis html ??
mot clé : html load css file

<head>
    <meta charset="UTF-8">
    <link rel = "stylesheet" href="{% static 'menu/style.css' %}"/>
</head>


liste html : <u> <li> p1</li> </u>

.main_logo{} : main_logo est le nom d'une div du coté css

Mot cle : 
css body adapt screen
css body background overlay
css center div on page


lien
app_name = "menu" dans urls.py de l'application
<a href="{% url 'menu:index' %}"> voir le menu </a>

publication du projet django
=====================================================================================
date : 17-09-2021
python anywhere
compte utilisateur : aoudiop
Email: alphadiop@gmail.com
Mdp : Ibrahima@1diop
url du site : https://aoudiop.pythonanywhere.com/
url du site : aoudiop.pythonanywhere.com

ALLOWED_HOSTS = ["aoudiop.pythonanywhere.com"]
une fois que ALLOWED_HOSTS  est renseigné, on ne peut plus lancer le projet en local

ajouter à la fin de setting.py
STATIC_ROOT = os.path.join(BASE_DIR,"static")

zippzer le projet en .zip
aller dans pythonanywhere
dans file et uploader le zip
https://www.pythonanywhere.com/user/aoudiop/

dans console
taper : ls
taper : unzip ProjetPizzaMama.zip

copier ce chemin à partir de la console
etape 5 : /home/aoudiop/ProjetPizzaMama : chemin du code source du projet


installer django
Attention : pizzamama-virtualenv
mkvirtualenv --python=/usr/bin/python3.8 pizzamama-virtualenv
pip install django

aller dans l'onglet : web

Attention: si les fichiers static ne sont pas visible 
taper : python manage.py collectstatic
urls du site : https://aoudiop.pythonanywhere.com/menu/

====================================================================================
API
https://jsoneditoronline.org/#right=local.yacoro


publier les mises à jours
rm -rf ProjetPizzaMama.zip
rm -rf ProjetPizzaMama
unzip ProjetPizzaMama.zip
ls
cd ProjetPizzaMama
python ./manage.py migrate
python ./manage.py collectstatic



