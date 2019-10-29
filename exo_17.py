def palindrome (mot):                          # fonction palindrome
    new=""                                     # variable du mots qui va etre retourné
    for i in range (len(mot)-1 , -1 , -1):     # boucle for avec fonction Len, -1 pour finir à 0, -1 pour inclure le 0, et -1 pour décreémenter
        new+=mot[i]                            # ajouter les lettres dans new
    if mot==new:                               # comparer les deux mots
        print("c'est un palindrome", new ,mot) # si égale
    else:
        print("Pas un palindrome",mot,new)     # sinon


test=input("entrer votre mot")                 # demande un mot
palindrome(test)                               # utilisation de la fonction
