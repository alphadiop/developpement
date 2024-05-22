# SQLITE : CREATION DE LA TABLE

import sqlite3

# connexion
# executer / curseur : objet intermédiaire
# commit
# fermer

connexion = sqlite3.connect(database="albums.db")
curseur = connexion.cursor()
sql_table_artiste = """
 CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY,
    nom VARCHAR
    );
"""
curseur.execute(sql_table_artiste)
connexion.commit()
connexion.close()


