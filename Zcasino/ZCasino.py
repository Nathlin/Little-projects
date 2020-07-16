import math
import random
import positives_numbers
import has_same_parity

#On demande la somme de départ au client
print("Quelle est votre somme de départ ?")
cagnotte_depart = positives_numbers.get_positive_number()
cagnotte = cagnotte_depart

while cagnotte >= 0:

    print("Choisissez un numéro de roulette : ")
    num_roulette = positives_numbers.get_positive_number_with_max_value(49)

    print("Quelle est votre mise ?")
    mise = positives_numbers.get_positive_number_with_max_value(cagnotte)

    valeur_gagnante = random.randrange(0, 49)
     

    print ("Vous avez parié sur le numéro ", num_roulette, ", et c'est le numéro ", valeur_gagnante, "qui est sorti !")

    print("Vos gains/pertes : ")
    
    if valeur_gagnante == num_roulette:
        cagnotte += 3 * mise
        a = 3*mise
        print ("Même chiffre, même couleur ! Vous avez gagné", a, "€, bravo ! Votre cagnotte s'élève désormais à ", cagnotte)
    elif has_same_parity.has_same_parity(valeur_gagnante, num_roulette):
        cagnotte += 0.5 * mise
        b = 0.5*mise
        print ("Pas le même chiffre, mais la même couleur ! Vous avez gagné", b, "€, bravo ! Votre cagnotte s'élève désormais à ", cagnotte)
    else:
        cagnotte -= mise
        print ("Vous avez perdu", mise, "€.! Votre cagnotte s'élève désormais à ", cagnotte)

    # Continuer ?
    choix = input("Voulez-vous continuer ? Y/N : ")
    if choix == "N" or choix == "n":

        if cagnotte > cagnotte_depart :
            print("Vous finissez avec une cagnotte de ", cagnotte, " euros. Félicitations !")
        elif cagnotte == cagnotte_depart :
                print ("Vous n'avez rien gagné ni perdu")
        else : print ("Vous finissez avec une cagnotte de ", cagnotte, "€. Vous avez perdu des sous.")


        cagnotte = -1
