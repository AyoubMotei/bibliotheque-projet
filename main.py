from data import utilisateurs,aime_livres
from users import *

majeurs = list(filter(est_majeur, utilisateurs))
print(majeurs)

# noms_majuscules = list(map(format_nom, utilisateurs))
noms_majuscules = list(noms_majuscules)
print (noms_majuscules)

# print(user_books)
print("*************")
print(listeFavoris(aime_livres,utilisateurs))
print(resumeFavoris(aime_livres, utilisateurs))