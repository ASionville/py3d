Module py3d.plans
=================
Module plans, contient la classe Plan et des fonctions annexes

Attributes:
    plan_xy (Plan): Plan d'équation z = 0 (horizontal)
    plan_xz (Plan): Plan d'équation y = 0 (vertical)
    plan_yz (Plan): Plan d'équation x = 0 (vertical)

Classes
-------

`Plan(*args)`
:   Classe représentant un plan de l'espace
    
    Attributes:
        point (points.Point): Point d'origine du plan
        vecteur_n (vecteurs.Vecteur): Vecteur normal au plan
    
    Initialisation du plan :
    
            - Un point + un vecteur normal
    
            - Deux droites
    
            - Un point + deux vecteurs non colinéaires
    
            - Trois points
    
    Args:
        *args: Arguments de définition du plan
    
    Raises:
        TypeError: Les types passés sont incorrects
        ValueError: Le vecteur normal est nul, les deux vecteurs sont colinéaires ou les trois points sont alignés

    ### Methods

    `cartesienne(self)`
    :   Renvoie l'équation cartésienne du plan, et les coefficients dans un tuple
        
        Returns:
            tuple:
        
            - Equation cartésienne (str)
        
            - Tuple avec les coefficients a b c d pour `ax + by + cz + d = 0`

    `vecteur_normal(self)`
    :   Renvoie le vecteur normal au plan
        
        Returns:
            vecteurs.Vecteur: Vecteur normal