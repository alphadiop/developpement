import json
"""
personne = {"nom":"paul",
            "age":25,
            "amis":["sophie","Marie","Jean"]
            }
personne_json = json.dumps(personne)
print(f"personne_json : {personne_json}")
f = open("file_json.txt","w")
f.write(personne_json)
f.close()
"""

f = open("file_json.txt","r")
donnees_json = f.read()
f.close()

personne = json.loads(donnees_json)
print(personne)
