import random
# import turtle

def verifierTailleGrille(tailleGrille):
    if type(tailleGrille) != list:
        print("[ERREUR] : tailleGrille n'est pas de type list")
        return False
    
    if len(tailleGrille) != 3:
        print("[ERREUR] : tailleGrille n'a pas la bonne taille")

    for elem in tailleGrille:
        if type(elem) == float:
            print("[ERREUR] : " + str(elem) + " n'est pas de type int")
            return False
        
        if elem <= 0:
            print("[ERREUR] : " + str(elem) + " est inférieur à 0")
            return False
        
    return True

def decallage(x, taille):
    pu()
    bk(x)
    lt(90)
    fd(taille)
    rt(90)
    pd()

def creerGrille(tailleGrille):
    clear()

    if verifierTailleGrille(tailleGrille):
        for posX in range(tailleGrille[0] + 1):
            fd(tailleGrille[0] * tailleGrille[2])
            decallage(tailleGrille[0] * tailleGrille[2], tailleGrille[2])

        rt(90)
        pu()
        fd(tailleGrille[2])
        pd()
    
        for posY in range(tailleGrille[1] + 1):
            fd(tailleGrille[1] * tailleGrille[2])
            decallage(tailleGrille[0] * tailleGrille[2], tailleGrille[2]) 

creerGrille([10, 10, 10])