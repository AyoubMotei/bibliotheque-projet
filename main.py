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
    
    
while True :
    menu()    
    choix = input("\nVotre choix : ")
    
    if choix == 1:
        print("\nLa liste des livres tries par annee de publication :")
        print(trier_book_annee(livres))
        
    elif choix == 2:
        print("\nVoici livre le plus ancien et le plus recent : ")
        Aide = identifier_ancien_recent(livres)
        print(affichage(Aide))
        
    elif choix == 3:
        print("\nVoici la liste des livres favorises: ")
        Aide = liste_favorise(livres, aime_livres)
        print(affichage(Aide))
        
    elif choix == 4:
        print("\nVoici les livres disponibles : ")
        print(affichage(livres))
        
    elif choix == 0:
        print(" Au revoir !")
        break
    
    else:
        print("\nVous devez choisir entre 0 et 4 !")
