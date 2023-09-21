Normalement le programme charge automatiquement le fichier kv
Par exemple : pour une application nommée : PizzaApp(App) alors le fichier kv à créer et qui sera chargé automatiquement est pizza.kv
mais on peut renomer le fichier en le chargean manuellement pour gerer l'encodage



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
