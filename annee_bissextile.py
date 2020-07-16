# On vérifie si l'annee tapée par l'utilisateur est valide. Sinon, on reboucle jusqu'à ce que l'année soit valide.
var_annee = False
continuer = False

while var_annee == False:

    annee = (input("Veuillez saisir une année, ou vous pouvez quitter le programme en tapant \"Q\"."))

# On test le type de "annee", si il est pas bon on recommence. Avec un "si", l'erreur se produirait avant car erreur de type
    try:
        annee = int (annee)
        var_annee = True
        continuer = True
    except :
        if annee == "q" or annee == "Q":
            var_annee = True
            continuer = False
            print ("Au revoir !")
        else :
            print ("Joue pas au con avec moi et tape un nombre.")


# On intègre une booléenne continuer pour poursuivre ou non notre programme après l'entrée de variable  
   
while continuer == True:

# Calcul de l'année bissextile ou non
    if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
        print ("L'année est bissextile.")
    else : print ("L'année n'est pas bissextile.")

# Autre année ?
    var_annee2 = False
    while var_annee2 == False:
        annee = input("Tapez une autre annee pour continuer, ou 'Q' pour quitter le programme.")

        if annee == "Q" or annee == "q":
            print ("Au revoir !")
            continuer = False
            var_annee2 = True
        else :
            try :
                annee = int(annee)
                var_annee2 = True
                continuer = True
            except ValueError:
                print("Tu m'emmerdes avec tes lettres, j'ai dit un chiffre !")
                var_annee2 = False


