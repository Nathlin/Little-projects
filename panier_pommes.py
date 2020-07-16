# On demande Ã  l'utilisateur combien il veut acheter de pommes
print ("Bonjour !")
nb_pommes = ""


while nb_pommes != "Q" and nb_pommes != "q" :

    nb_pommes = input ("Combien souhaitez vous acheter de pommes aujourd'hui ? Vous pouvez quitter en tapant \"Q\" ou \"q\".")

    try :
        nb_pommes = int (nb_pommes)

        if nb_pommes <= 7 :
            print ("Il y Ã  ", nb_pommes, "dans votre panier.")

        if nb_pommes >= 7 :
            # a = panier plein
            a = nb_pommes - 7

            # b = nombre de poches pleines
            b = a//10

            # c = nombre de pommes restantes dans une poche non pleine. 
            c = a%10

        print ("Votre panier est plein, vous avez ", b, " poches pleines, et une poche de ", c, " pomme(s)." )
    except :
        if nb_pommes == "q" or nb_pommes == "Q":
            print ("Au revoir !")
        else :
            print ("Veuillez saisir un nombre valide.")