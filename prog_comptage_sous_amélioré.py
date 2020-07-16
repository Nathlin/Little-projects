# Programme comptage de sous 
import positive_number
import math
import reponse_user


# On crée la liste de billets et pièces disponibles
L = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 1]

# Demande de la somme à l'utilisateur
print ("Bonjour ! Quelle est la somme que vous voulez trier ?")
print ("Nous avons à notre des disposition des billets de 500, 200, 100, 50, 20, 10, 5, et des pièces de 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, et 0.01.")
somme = positive_number.get_positive_number()
b = somme

# Découpage particulier ou découpage basique ?


print("Voulez vous un découpage particulier de votre somme ? \'Y/N\'")
rep_user = reponse_user.reponse_user()

# Découpage basique somme
if rep_user == 'N' :
    print ("Votre somme a été décomposée en :")
    positive_number.tri(b, L)


# Si découpe particulière : 
elif rep_user == 'Y' :
    print ("Quelle est la coupure minimale que vous souhaitez ?")

    verif_coupure_min = False
    while verif_coupure_min == False :

        #on vérifie avec une fonction si la coupure demandée est bonne (dans L et inférieure à la somme)
        coupure_min_user = positive_number.get_positive_number()
        verif_coupure_min = positive_number.verifier_si_coupure_min_dans_liste(coupure_min_user, L, b)

        if verif_coupure_min == False :
            print ("Ce n'est pas une réponse valable. (Coupure inexistante ou coupure supérieure à la somme.)")

        else : #On créé une liste et on lui demande direct si il veut une seconde coupure
            L2 = []
            L2.append(coupure_min_user)
            L2.append('0')
            print ("Souhaitez vous une seconde coupure ?")
            seconde_coupure_user = reponse_user.reponse_user()

            # Si non, tri basique avec une coupure minimale
            if seconde_coupure_user == 'N' :
                positive_number.tri_coupure_min(b, L, coupure_min_user)

            # Si oui, on va utiliser la liste2
            else :
                verif_coupure_min2 = False
                while verif_coupure_min2 == False :
                    print ("Quelle est la valeur de la SECONDE coupure ?")
                    coupure_min_user2 = positive_number.get_positive_number()
                    verif_coupure_min2 = positive_number.verifier_si_coupure_min_dans_liste(coupure_min_user2, L, b)

                    if verif_coupure_min2 == True :
                        L2[1] = coupure_min_user2
                        
                        #On inverse si les L2[0] < L2[1]
                        if L2[0] < L2[1] :
                            positive_number.inverser_nombres_liste(L2, 0, 1)
                        elif L2[0] == L2[1] :
                            verif_coupure_min2 = False 
                            print ("Vous ne pouvez pas entrer la même valeur.")

                    else : 
                        print ("Cette coupure n'existe pas ou est supérieure à la somme.")

                        # Ensuite on passe à notre opération
                reste = positive_number.tri(b, L2)
                positive_number.tri(reste, L)
