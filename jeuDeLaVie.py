import random
# import turtle

def verifierTailleGrille(tailleGrille):
    assert type(tailleGrille) == list
    assert len(tailleGrille) == 3

    for elem in tailleGrille:
        assert type(elem) == int
        assert elem > 0
        
    return True

def allerA(cible, position):
    pu()

    fd(cible[0] - position[0])
    lt(90)
    fd(cible[1] - position[1])
    rt(90)

    pd()

def creerGrille(tailleGrille):
    if verifierTailleGrille(tailleGrille):
        for posY in range(tailleGrille[1] + 1):
            fd(tailleGrille[1] * tailleGrille[2])
            allerA([0, (posY + 1) * tailleGrille[2]], [tailleGrille[1] * tailleGrille[2], posY * tailleGrille[2]])

        rt(90)
        pu()
        fd(tailleGrille[2])
        pd()
    
        for posX in range(tailleGrille[1] + 1):
            fd(tailleGrille[0] * tailleGrille[2])
            allerA([0, (posX + 1) * tailleGrille[2]], [tailleGrille[0] * tailleGrille[2], posX * tailleGrille[2]])

        lt(90)


def dessinerGrille(tailleGrille, grille):
    position = [1, 5]

    pensize(8)
    pu()

    for ligne in grille:
        for elem in ligne:
            if elem:
                pencolor(1, 0, 0)
                pd()
                fd(tailleGrille[2] - 2)
                pu()
                fd(2)

            else:
                pencolor(1, 1, 1)
                pd()
                fd(tailleGrille[2] - 2)
                pu()
                fd(2)

            position[0] += tailleGrille[2]            

        allerA([1, position[1] + tailleGrille[2]], position)
        position[0] = 1
        position[1] += tailleGrille[2]

clear()

tailleGrille = [20, 20, 10]

# Change le centre de la grille
allerA([-100, -100], [0, 0])

creerGrille(tailleGrille)
allerA([1, 5], [(tailleGrille[0] + 1) * tailleGrille[2], tailleGrille[1] * tailleGrille[2]])
dessinerGrille(tailleGrille, [[True, False], [True, True]])
