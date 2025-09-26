#books.py

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

