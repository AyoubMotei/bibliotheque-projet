from books import *
from data import livres, aime_livres

def affichage(nom_liste):
    print("\n---------------- Liste des livres disponibles : ----------------")
    for livre in nom_liste:
        print(f"Livre : {livre['titre']} | Auteur : {livre['auteur']} | Année : {livre['année']}")



def menu():
    print("\n======= Gestion des livres =======")
    print("1 -> Trier les livres par année de publication")
    print("2 -> Identifier le plus ancien et le plus récent")
    print("3 -> Fiche des favoris")
    print("4 -> Afficher les livres")
    print("0 -> Quitter")
    
    
while True:
    menu()
    choix = input("\nVotre choix : ")

    if choix == "1":
        print("\nLa liste des livres triés par année de publication :")
        affichage(trier_book_annee(livres))

    elif choix == "2":
        print("\nVoici le livre le plus ancien et le plus récent :")
        Aide = identifier_ancien_recent(livres)
        affichage(list(Aide))

    elif choix == "3":
        print("\nVoici la liste des livres favorisés :")
        favoris = liste_favorise(aime_livres)
        for titre, count in favoris.items():
            print(f"Livre : {titre} | Nombre d'utilisateurs qui aiment : {count}")

    elif choix == "4":
        print("\nVoici les livres disponibles :")
        affichage(livres)

    elif choix == "0":
        print("Au revoir !")
        break

    else:
        print("\nChoix invalide !")
