from data import utilisateurs , livres, aime_livres

def est_majeur(utilisateur):
    age = utilisateur[3]   
    return age >= 18

# def format_nom(utilisateur):
#     prenom = utilisateur[1]   
#     nom = utilisateur[2]      
#     complet = prenom + " " + nom   
#     return complet.upper()  

noms_majuscules = map(lambda u: (u[1] + " " + u[2]).upper(), utilisateurs)


# def listeFavoris(likedBooks,users) :
#     dict_counter ={}
#     for user in users :
#         id, fname,lname,_= user
#         dict_counter[fname] = []
#         for elem in likedBooks :
#             if id == elem[0] :
#                 dict_counter[fname].append(elem[1])
              
#     for element in dict_counter:
#         print(f"{element[0]}") 
#     return dict_counter           

def listeFavoris(likedBooks, users):
    dict_counter = {}
    for user in users:
        user_id, fname, lname, _ = user
        full_name = f"{fname} {lname}"  
        dict_counter[full_name] = []    

        for elem in likedBooks:
            if user_id == elem[0]:
                dict_counter[full_name].append(elem[1])

    return dict_counter
                
def resumeFavoris(likedBooks, users):
    resumes = []
    for user in users:
        user_id, fname, lname, age = user
        full_name = f"{fname.upper()} {lname.upper()}"  

        
        livres_aimes = []
        for elem in likedBooks:
            if user_id == elem[0]:
                livres_aimes.append(elem[1])

       
        if livres_aimes: 
            resume = f"{full_name} ({age} ans) aime : " + ", ".join([f"'{titre}'" for titre in livres_aimes])
        else:  
            resume = f"{full_name} ({age} ans) n'aime aucun livre pour le moment"

        resumes.append(resume)

    return resumes

