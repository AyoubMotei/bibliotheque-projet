from data import utilisateurs
from users import est_majeur , noms_majuscules

majeurs = list(filter(est_majeur, utilisateurs))
print(majeurs)

# noms_majuscules = list(map(format_nom, utilisateurs))
noms_majuscules = list(noms_majuscules)
print (noms_majuscules)
