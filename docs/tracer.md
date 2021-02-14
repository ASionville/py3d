Module py3d.tracer
==================
Module tracer, contient le nécessaire pour l'affichage dans un tracé 3D

Classes
-------

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