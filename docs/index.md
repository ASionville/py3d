Module py3d
===========
Module py3D, pour gérer la géométrie 3D en python

Sub-modules
-----------
* py3d.droites
* py3d.plans
* py3d.points
* py3d.tracer
* py3d.utils
* py3d.vecteurs

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

    
`collineaires(u, *args)`
:   

    
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

`Repere3D()`
:   Classe Trace3D, représente le repère 3D
            
    
    Initialisation du repère

    ### Methods

    `afficher(self)`
    :   Affiche le repère et la légende

    `ajouter(self, objet, couleur=None, longueur=10, label='', grille=0)`
    :   Ajoute un objet dans le repère
        
        Args:
            objet : Objet (Point / Droite / Plan) à ajouter
            couleur (str, optionnel): Couleur à utiliser (en anglais)
            longueur (int, optionnel): Longueur totale sur chaque axe (pour les droites)
            label (str, optionnel): Label à attribuer à l'objet
            grille (int, optionnel): Mode "grillage", avec {grille} lignes et {grille} colonnes (pour les plans)

    `dessiner_axes(self)`
    :   Ajoute les axes au repère

    `dessiner_origine(self)`
    :   Ajoute l'origine au repère

`Vecteur(*args)`
:   

    ### Methods

    `absolue(self)`
    :

    `est_nul(self)`
    :

    `get_coordonnes(self)`
    :

    `normal(self)`
    :

    `normalise(self)`
    :

    `norme(self)`
    :

    `produit_vectoriel(self, vecteurB)`
    :

    `scalaire(self, vecteurB)`
    :