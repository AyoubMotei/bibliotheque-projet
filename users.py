from data import utilisateurs

def est_majeur(utilisateur):
    age = utilisateur[3]   
    return age >= 18

# def format_nom(utilisateur):
#     prenom = utilisateur[1]   
#     nom = utilisateur[2]      
#     complet = prenom + " " + nom   
#     return complet.upper()  

noms_majuscules = map(lambda u: (u[1] + " " + u[2]).upper(), utilisateurs)
