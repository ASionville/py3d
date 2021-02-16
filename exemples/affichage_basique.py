import py3d

#Création d'un point A de coordonnées (1, 1, 1)
pointA = py3d.Point(1, 1, 1)

#Création d'une droite passant par A et l'origine
d = py3d.Droite(py3d.origine, pointA)

#Création du plan z=0 (plan xy)
plan = py3d.plan_xy

#Création du repère 3D
repere = py3d.Repere3D()

#Ajout du plan divisé en une grille de 20x20
repere.ajouter(plan, grille=20)
#Ajout de la droite violette avec une étiquette
repere.ajouter(d,longueur=1, couleur="purple", label="Droite d x = y = z")
#Ajout du point A
repere.ajouter(pointA, label="Point A")

#Affichage du repère
repere.afficher()
