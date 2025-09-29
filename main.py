from books import *
from users import *
from data import livres, aime_livres,utilisateurs

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
    print("5 -> Filtrer les utilisateurs majeurs")
    print("6 -> Formater les noms complet en majescule")
    print("7 -> Dictionnaire asspciant utilisateur a ses livres aimés ")
    print("8 -> Rappoprt des utilisateurs")



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
    
    elif choix == "5":
        print("\nVoici les utilisateurs majeurs:")
        majeurs = list(filter(est_majeur, utilisateurs))
        print(majeurs)
    
    elif choix == "6":
        print("\nVoici les noms complet en majescule:")
        noms_majuscules = list(noms_majuscules)
        print (noms_majuscules)
    
    elif choix == "7":
        print("\nVoici le dictionnaire associant l'utilisateur a ses livres aimées:")
        print(listeFavoris(aime_livres,utilisateurs))
        
    elif choix == "8":
        print("\nVoici un rapport des utilisateur:")
        print(resumeFavoris(aime_livres, utilisateurs))
    
    elif choix == "0":
        print("Au revoir !")
        break

    else:
        print("\nChoix invalide !")


