initialistion des données en dur
recuperer des données réseau
se connecter à un serveur pour recuperer des données
ce sont des accès reseaux
format JSON permet de transmettre des données structurées sous forme de texte JSON
version texte de JSON correspond à la version sérialiser
le serveur va sérialiser les données pour les transmettre au format texte : json.dumps()
le client qui va recevoir les données à partir du serveur va déserialiser : json.loads()
Etapes
1. Récuperer les données du serveur
2. remonter les données à la UI+ Gestion d'erreurs
3. sauvegarder les données de maniere persistance

Normalement le programme charge automatiquement le fichier kv
Par exemple : pour une application nommée : PizzaApp(App) alors le fichier kv à créer et qui sera chargé automatiquement est pizza.kv
mais on peut renomer le fichier en optant pour un chargement manuellement afin de gerer l'encodage


http_client.py : ensembles des fonctions permettant d'accèder au réseaux
Faire un accès réseau (serveur) pour récuperer les données
HTTP / JSON



SIte web :
Application Bureau
Application Mobile

requête Reseau : Bibliothèque requests
kivy URLRequests

Format JSON
permet de transmettre sur réseau
le serveur va sérialiser les données JSON par json.dumps() afin d'exploiter les données
le client va déserialiser les données JSOn par json.loads() afin d'afficher à l'écran

Etapes pour recuperer des données sur réseau
1. Récupérer les données du serveur
2. Remonter à la UI + gestion d'érreurs
3. Persistance
