def get_positive_number () :

    number = -1

    while number < 0 or number == 0 :
        
        try : 
            number = float(input(": "))
            if number < 0 or number == 0 :
                print ("Vous ne pouvez pas entrer un nombre négatif ou égal à 0.")
        except : 
            print ("Nombre invalide !")

    return number 




def tri_coupure_min (b, L, coupure_min_user) :

    index_liste_coupure_min = L.index(coupure_min_user)
    for i in L[index_liste_coupure_min:] :
# a prend la valeur du nombre de pièces / billets qui vont être données à l'utilisateur 
        a = int(b // i)
                        
# b prend la valeur du reste, qui va être réutilisé par la suite                     
        b = round (b % i, 2) 
                    

# c est l'indicateur de pièces ou billets
        if i in [500, 200, 100, 50, 20, 10, 5] :
            c = "billet(s)"
        else : c = "pièce(s)"

# Si aucune coupure, on n'affiche pas
        if a != 0 :
            print (a, c, "de", i, "€.")
        else : pass 

# On donne a "a" la valeur du reste, pour le rediviser
        a = b


def tri (b, L) :

    for i in L :
            
        # a prend la valeur du nombre de pièces / billets qui vont être données à l'utilisateur 
        a = int(b // i)
            
            
        # b prend la valeur du reste, qui va être réutilisé par la suite 
        b = round(b % i, 2)
            

        # c est l'indicateur de pièces ou billets

        if i in [500, 200, 100, 50, 20, 10, 5] :
            c = "billet(s)"
        else : c = "pièce(s)"

        # Si aucune coupure, on n'affiche pas
        if a != 0 :
            print (a, c, "de", i, "€.")
        else : pass 

        # On donne a "a" la valeur du reste, pour le rediviser
        a = b 

    return a


def verifier_si_coupure_min_dans_liste (coupure_min_user, L, b) :

    if coupure_min_user in L and b > coupure_min_user :
        coupure_demandée_ok = True 
    else : 
        coupure_demandée_ok = False 

    return coupure_demandée_ok


def inverser_nombres_liste (L2, a, b) :

    if L2 [a] < L2 [b] :
        e = L2[a]
        L2[a] = L2[b]
        L2[b] = e