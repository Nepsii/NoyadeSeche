def trouver () :
    # Les ADN :
    moutarde = "CCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGC"
    rose = "CTCCTGATGCTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGG"
    Pervenche = "AAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGTACTCCGCGCGCCGGGACAGAATGCC"
    Leblanc = "CTGCAGGAACTTCTTCTGGAAGTACTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAG"
    a=0
    b=0
    c=0
    d=0
    # Les codes :
    code = "CATA"
    code2 = "ATGC"
    suspects = [moutarde, rose, Pervenche, Leblanc]
    name = ["moutarde", "rose", "Pervenche", "Leblanc"]
    resultat =[a,b,c,d]
    lescodes =[code, code2]

    for y in range(len(suspects)):
        adn = suspects [y]
        print (adn)
        for x in range(len(lescodes)):
            coupable = lescodes[x]
            #print (coupable)
            if coupable in adn:
                for i in range(len(adn) - len(coupable)):
                    if adn[i] == coupable[0]:
                        code_in_sequence = adn[i: i + len(coupable)]
                        #print (code_in_sequence)
                        #print("V_", code_in_sequence)
                        if code_in_sequence == coupable:
                            print (coupable + ": ok")
                            resultat[y]+=1
                            if resultat[y]==2:
                                print (name[y]+" est le coupable ")
                                break




trouver()
