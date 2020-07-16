def get_positive_number():
    number = -1
    while number < 0:
        try:
            number = int(input("Valeur : "))
            if number < 0:
                print("Erreur : nombre < 0")
        except:
            print("Nombre invalide !")
    return number




def get_positive_number_with_max_value(max):
    number = max+1
    while number > max :
        print("Entrez un nombre supérieur à 0 et inférieur à ", max, " : ")
        number = get_positive_number()
    return number



