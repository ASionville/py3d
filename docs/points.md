Module py3d.points
==================
Module points, contient la classe Point et des fonctions annexes

Attributes:
    origine (Point): Point de coordonnées `(0, 0, 0)`

Functions
---------

    
`alignes(pointA, pointB, *args)`
:   Renvoie True si les points sont alignés, False sinon
    
    Args:
        pointA (Point): Point A
        pointB (Point): Point B
        *args: Autres points
    
    Returns:
        bool: Points tous alignés ?
    
    Raises:
        TypeError: Si les objets donnés ne sont pas tous des points

    
`distance(pointA, pointB)`
:   Donne la distance entre deux points
    
    Args:
        pointA (Point): Point A
        pointB (Point): Point B
    
    Returns:
        float: Distance entre A et B
    
    Raises:
        TypeError: Si A ou B n'est pas un point

    
`est_meme_point(pointA, pointB)`
:   Renvoie True si les deux points sont au même endroit, False sinon
    
    Args:
        pointA (Point): Point A
        pointB (Point): Point B
    
    Returns:
        bool: A et B au même endroit ?

Classes
-------

`Point(x=0, y=0, z=0)`
:   Classe représentant un point de l'espace
    
    Attributes:
        x (float): Coordonnée X
        y (float): Coordonnée Y
        z (float): Coordonnée Z
    
    Initialisation du point
    
    Args:
        x (float): Coordonnée X
        y (float): Coordonnée Y
        z (float): Coordonnée Z

    ### Methods

    `distance_origine(self)`
    :   Donne la distance à l'origine
        
        Returns:
            float: Distance entre le point et l'origine