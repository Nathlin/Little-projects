def reponse_user () :

    rep_user = 'a'
    while rep_user != 'N' or rep_user != 'Y' :
        rep_user = input (": ")
        rep_user = rep_user.upper()
        if rep_user != 'N' or rep_user != 'Y' :
            print ("Ce n'est pas une réponse valable.")

return rep_user
    


