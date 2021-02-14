Module py3d.droites
===================
Module droites, contient la classe Droite et des fonctions annexes

Attributes:
    axe_x (Droite): Droite de l'axe X
    axe_y (Droite): Droite de l'axe Y
    axe_z (Droite): Droite de l'axe Z

Functions
---------

    
`orthogonales(droite1, droite2)`
:   Non implémenté

    
`parallelles(d, *args)`
:   Renvoie True si les droites données sont parallèles, False sinon
    
    Args:
        d (Droite): Droite de référence
        *args: Autres droite
    
    Returns:
        bool: Droites toutes parallèles ?
    
    Raises:
        TypeError: Si les objets donnés ne sont pas tous des droites

    
`secantes(d, *args)`
:   Non implémenté

Classes
-------

`Droite(*args)`
:   Classe représentant une droite de l'espace
    
    Attributes:
        point (points.Point): Un point appartenant à la droite
        vecteur (vecteurs.Vecteur): Vecteur directeur de la droite
    
    Initialisation de la droite
    
            - Deux points
    
            - Un point + un vecteur
    
    Args:
        *args: Arguments de définition de la droite
    
    Raises:
        TypeError: Les types passés sont incorrects
        ValueError: Les deux points son identiques ou le vecteur directeur est nul

    ### Methods

    `est_sur_droite(self, point)`
    :   Renvoie True si le point est sur la droite, False sinon
        
        Args:
            point (points.Point): Point quelconque
        
        Returns:
            bool: Point sur la droite ?
        
        Raises:
            TypeError: Si l'objet donné n'est pas un point

    `parametrique(self)`
    :   Renvoie l'équation paramétrique de la droite, et les coefficients dans un tuple
                
                Returns:
                    tuple:
        
                    - Equation paramétrique (str)
        
                    - Tuple avec les coefficients xp, yp, zp, xu, yu, zu pour
        
        
        \begin{equation}
                x= xp + x\overrightarrow{u}
        \end{equation}
        
        \begin{equation}
                y= y + y\overrightarrow{u}
        \end{equation}
        
        \begin{equation}
                z= zp + z\overrightarrow{u}
        \end{equation}