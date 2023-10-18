import os
import subprocess
# Popen : ancienne interface
# run : executer la commande et attendre le resulat

# shell=True : pour préciser qu'il s'agit bien d'une commande
# capture_output=True : on souhaite recuperer le résultat

# os.chdir(...)
# os.getcwd()


# resultat = subprocess.run(args="dir",shell=True,capture_output=True)
# print(resultat.stdout.decode(encoding="utf-8",errors="ignore"))
# return = 0 : ca veut dire que ça s'est bien passé

while True:
    commande = input(os.getcwd() + " > ")
    if commande=="exit":
        break
    command_split = commande.split(" ")
    if len(command_split) == 2 and command_split[0]=="cd":
        try:
            commande = os.chdir(command_split[1])
        except FileNotFoundError as e:
            print(e)
    else:
        resultat = subprocess.run(args=commande,shell=True,capture_output=True,universal_newlines=True)
    # universal_newlines=True : il va decoder le resultat pour donner du texte

        print(resultat.stdout)
        print(resultat.stderr)