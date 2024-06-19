import random
# import turtle

def verifierTailleGrille(tailleGrille):
    assert type(tailleGrille) == list
    assert len(tailleGrille) == 3

    for elem in tailleGrille:
        assert type(elem) == int
        assert elem > 0
        
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