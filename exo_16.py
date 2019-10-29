def distance_hamming(mot1,mot2) :       #fonction distance hamming
    distance=0                          #intier la distance a 0
    if len(mot1)==len(mot2) :           #si le mot1 et mot2 son de la meme longueur avec fonction len
        for i in range (0 , len(mot1)): #boucle passant les lettres une par une
            if mot1[i]!=mot2[i]:        #compare si les lettres des deux mots de même longueur sont différentes
                distance+=1             #si oui ajoute +1 la distance
        print("la distance de hamming entre vos deux mots est de :", distance,mot1,mot2)
    else:
        print("saisir deux mot de meme longeur svp") #si les mots ne sont pas de la même longueur alors recommencer

mot1=input("saisir le premier mot que vous voulez comparer ")
mot2=input("saisir le deuxieme mot de meme longeur que vous voulez comparer ")
distance_hamming(mot1,mot2)
