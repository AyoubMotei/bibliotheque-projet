#books.py
from data import aime_livres, livres, utilisateurs

# fonction : Trier les livres par année de publication
def trier_book_annee(livres):
    return sorted(livres, key=lambda livre: livre["année"])

# fonction : Identifier le plus ancien et le plus récent.
def identifier_ancien_recent(livres):
    livres_tries = trier_book_annee(livres)
    return livres_tries[0], livres_tries[-1]

# fonction : construire un dictionnaire
def liste_favorise(liste_name, liste_aime):
    for index in liste_name:
        new_list = list(filter(lambda i: i[0] == index ,liste_aime))

    return new_list

# fonction : construire un dictionnaire des livres aimés
def liste_favorise(aime_livres):
    dict_count = {}
    for _, titre in aime_livres: 
        if titre in dict_count:
            dict_count[titre] += 1
        else:
            dict_count[titre] = 1
    return dict_count

def pagination(list_name):
    page = 1
    items_per_page = 0
    while items_per_page < len(list_name):
        print(f"\n--- Page {page} --- \n{list_name[items_per_page:items_per_page + 2]}")
        items_per_page += 1
        page += 1
    
def recherche_par_auteur(list_name, auteur):
    return list(filter(lambda livre: livre['auteur'] == auteur, list_name))

def recherche_par_titre(list_name, titre):
    return list(filter(lambda livre: livre['titre'] == titre, list_name))

def recherche_par_annee(list_name, annee):
    return list(filter(lambda livre: livre['année'] == annee, list_name))
