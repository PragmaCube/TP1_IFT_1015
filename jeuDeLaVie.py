###################################################################
# IFT-1015 Programmation 1
# Fichier : jeuDeLaVie.py
# Auteurs : Ariyan Adabzadeh (20218141) et Raphaël Pothier (20244742)
# Programme simulant le jeu de la vie de John Conway dans une grille
# de taille finie.

import random

def allerA(cible, position):
    """
    Fonction permettant de déplacer le curseur vers une cible
    depuis une position connue à l'avance. La direction de
    départ a un impact sur le référentiel :
    - Vers la droite : aucun impact sur le référentiel
    - Vers le haut   : le référentiel subit une rotation de pi / 2
    - Vers la gauche : le référentiel subit une rotation de pi
    - Vers le bas    : le référentiel subit une rotation de - pi / 2

    Avant chaque utilisation, il est conseillé de fixer la droite 
    comme direction du curseur.
    """
    pu()

    fd(cible[0] - position[0])
    lt(90)
    fd(cible[1] - position[1])
    rt(90)

    pd()

def creerGrille(tailleGrille):
    """
    Fonction dessinant la grille en fonction des paramètres
    initiaux.
    """

    for posY in range(tailleGrille.ny + 1):
        fd(tailleGrille.nx * tailleGrille.largeur)
        allerA([0, (posY + 1) * tailleGrille.largeur], [tailleGrille.nx * tailleGrille.largeur, posY * tailleGrille.largeur])

    rt(90)
    pu()
    fd(tailleGrille.largeur)
    pd()

    for posX in range(tailleGrille.nx + 1):
        fd(tailleGrille.ny * tailleGrille.largeur)
        allerA([0, (posX + 1) * tailleGrille.largeur], [tailleGrille.ny * tailleGrille.largeur, posX * tailleGrille.largeur])

    lt(90)

def genererGrille(tailleGrille):
    """
    Fonction permettant de générer un tableau 2D initialisé
    avec des False (cellule morte).
    """
    ligne = [False] * tailleGrille.nx

    grille = []

    for i in range(tailleGrille.ny):
        # Il est nécessaire d'instancier à chaque itération
        # une nouvelle liste pour éviter que chaque élément
        # de grille ne pointe vers la même variable.
        grille.append(list(ligne))

    return grille

def init(grille):
    """
    Fonction diposant de manière aléatoire les cellules
    vivantes à l'état initial.
    """

    # La fonction f : [0, 1] -> [0, 0.5] définie par
    # f(x) = 0.4x + 0.1 est une bijection, ce qui assure
    # de générer des nombres entre 0 et 0.5 de manière
    # aléatoire.
    pourcentageCellulesVivantes = random.random() * 0.4 + 0.1

    nbrCellulesVivantes = round(pourcentageCellulesVivantes * len(grille) * len(grille[0]))
    compteur = 0

    # Tant que les cellules vivantes ne sont pas complètement
    # disposées, on parcours la grille et on détermine, au hasard,
    # si chaque cellule est vivante.
    while compteur != int(nbrCellulesVivantes):
        for posY in range(len(grille)):
            for posX in range(len(grille[0])):
                if random.random() <= nbrCellulesVivantes / (len(grille) * len(grille[0])) and not grille[posY][posX]:
                    grille[posY][posX] = True
                    compteur += 1

                if compteur == int(nbrCellulesVivantes):
                    return grille

    return grille

def dessinerGrille(tailleGrille, grille):
    """
    Fonction coloriant la grille en fonction de l'état
    actuel donné par grille.
    """

    position = [1, 5]

    pensize(8)
    pu()

    for ligne in grille:
        for elem in ligne:
            if elem:
                pencolor(1, 0, 0)
                pd()
                fd(tailleGrille.largeur - 2)
                pu()
                fd(2)

            else:
                pencolor(1, 1, 1)
                pd()
                fd(tailleGrille.largeur - 2)
                pu()
                fd(2)

            position[0] += tailleGrille.largeur            

        allerA([1, position[1] + tailleGrille.largeur], position)
        position[0] = 1
        position[1] += tailleGrille.largeur

def detectionCellulesVivantes(grille, position):
    """
    Fonction permettant de détecter le nombre de cellules vivantes
    autour d'une position connue en fonction d'une grille de booléens.
    """
    cellulesVivantes = 0

    for posX in range(max(0, position[0] - 1), min(len(grille[0]) - 1, position[0] + 1) + 1):
        for posY in range(max(0, position[1] - 1), min(len(grille) - 1, position[1] + 1) + 1):
            if position != [posX, posY]:
                cellulesVivantes += grille[posY][posX]

    return cellulesVivantes

def tests():
    """
    Fonction de tests unitaires pour les fonctions supplémentaires.
    """

    # Tests vérifiant si les détections de cellules vivantes fonctionnent
    # peu importe la position choisie (coin, bord, autre).
    assert detectionCellulesVivantes([[True, False, True], [False, True, False], [True, False, True]], [1, 1]) == 4
    assert detectionCellulesVivantes([[True, False, True], [False, True, False], [True, False, True]], [1, 0]) == 3
    assert detectionCellulesVivantes([[True, False, True], [False, True, False], [True, False, True]], [0, 0]) == 1

    # Test vérifiant le bon déplacement du curseur selon la fonction allerA
    # Ce test est uniquement visuel.
    allerA([-100, -100], [0, 0])


def jouer(tailleGrille):
    """
    Fonction affichant indéfiniment la grille et la mettant à
    jour selon les règles précisées. Il est possible de mettre
    un délai d'affichage entre chaque itération.
    """

    grille = init(genererGrille(tailleGrille))
    
    ht()

    # Change le centre de la grille
    allerA([-100, -100], [0, 0])

    creerGrille(tailleGrille)
    allerA([1, 5], [(tailleGrille.nx + 1) * tailleGrille.largeur, tailleGrille.ny * tailleGrille.largeur])

    while True:        
        dessinerGrille(tailleGrille, grille)

        for posY in range(len(grille)):
            for posX in range(len(grille[0])):
                if detectionCellulesVivantes(grille, [posX, posY]) < 2:
                    grille[posY][posX] = False

                elif detectionCellulesVivantes(grille, [posX, posY]) > 3:
                    grille[posY][posX] = False

                elif detectionCellulesVivantes(grille, [posX, posY]) == 3:
                    grille[posY][posX] = True

        allerA([1, 5], [1, tailleGrille.nx * tailleGrille.largeur + 5])
        pd()

        # Ajuster au besoin pour distinguer plus nettement chaque
        # état.
        sleep(0.1)



tailleGrille = struct(nx = 20, ny = 20, largeur = 10)

jouer(tailleGrille)
###################################################################