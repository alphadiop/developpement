liste_pizza = ("4 fromage","vegetarienne",'Jambon Fromage','GGG')
liste_pizza = ["4 fromage","vegetarienne",'Jambon Fromage']
liste_pizza_vide = ()
def afficher_pizza(collection):
    for pizza in collection :
        print(pizza)
    print()
    print(f"Premiere pizza : {collection[0]}")
    print(f"Derniere pizza : {collection[-1]}")

def afficher_pizza2(collection):
    nb_pizzas = len(collection)
    if nb_pizzas==0:
        print('Aucune Pizza')
        return ## ça veut dire sortir du boucle
    else:
        for pizza in collection :
            print(pizza)
    print()
    print(f"Premiere pizza : {collection[0]}")
    print(f"Derniere pizza : {collection[-1]}")


def afficher_pizza3(collection):
    nb_pizzas = len(collection)
    if nb_pizzas==0:
        print('Aucune Pizza')
    for pizza in collection :
        print(pizza)
    print()
    print(f"Premiere pizza : {collection[0]}")
    print(f"Derniere pizza : {collection[-1]}")

def slice(collection):
    print(f"collection : {collection[:-1]}")


if __name__ == "__main__":
    print(120*'*')
    print(f"collection : {liste_pizza}")
    slice(liste_pizza)
    #afficher_pizza(liste_pizza)
    #afficher_pizza(liste_pizza_vide)
    #afficher_pizza2(liste_pizza_vide)
    #afficher_pizza3(liste_pizza_vide)
