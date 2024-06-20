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

def detectionCellulesVivantes(grille, position):
    cellulesVivantes = 0

    if position[0] == 0:
        if position[1] == 0:
            cellulesVivantes += grille[0][1] + grille[1][0] + grille[1][1]

        elif position[1] == len(grille) - 1:
            cellulesVivantes += grille[len(grille) - 2][0] + grille[len(grille) - 1][1] + grille[len(grille) - 2][1]

        else:
            cellulesVivantes += grille[position[1] + 1][0] + grille[position[1] - 1][0]

            for posY in range(-1, 2):
                cellulesVivantes += grille[position[1] + posY][1]
    
    elif position[0] == len(grille[0]) - 1:
        if position[1] == 0:
            cellulesVivantes += grille[0][len(grille[0]) - 2] + grille[1][len(grille[0]) - 1] + grille[1][len(grille[0]) - 2]

        elif position[1] == len(grille) - 1:
            cellulesVivantes += grille[len(grille) - 2][len(grille[0]) - 2] + grille[len(grille) - 1][len(grille[0]) - 2] + grille[len(grille) - 2][len(grille[0]) - 1]

        else:
            cellulesVivantes += grille[position[1] + 1][len(grille[0]) - 1] + grille[position[1] - 1][len(grille[0]) - 1]

            for posY in range(-1, 2):
                cellulesVivantes += grille[position[1] + posY][len(grille[0]) - 2]

    else:
        if position[1] == 0:
            cellulesVivantes += grille[0][position[0] + 1] + grille[0][position[0] - 1]

            for posX in range(-1, 2):
                cellulesVivantes += grille[1][position[0] + posX]
            
            return 

        elif position[1] == len(grille) - 1:
            cellulesVivantes += grille[len(grille) - 1][position[0] + 1] + grille[len(grille) - 1][position[0] - 1]

            for posX in range(-1, 2):
                cellulesVivantes += grille[len(grille) - 2][position[0] + posX]

        else:
            cellulesVivantes += grille[position[1]][position[0] + 1] + grille[position[1]][position[0] - 1]

            for posX in range(-1, 2):
                cellulesVivantes += grille[position[1] + 1][position[0] + posX] + grille[position[1] - 1][position[0] + posX]

    return cellulesVivantes


clear()

tailleGrille = [20, 20, 10]

# Change le centre de la grille
allerA([-100, -100], [0, 0])

creerGrille(tailleGrille)
allerA([1, 5], [(tailleGrille[0] + 1) * tailleGrille[2], tailleGrille[1] * tailleGrille[2]])
dessinerGrille(tailleGrille, [[True, False], [True, True]])
