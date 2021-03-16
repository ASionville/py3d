"""Module points, contient la classe Point et des fonctions annexes

Attributes:
    origine (Point): Point de coordonnées `(0, 0, 0)`
"""
from math import sqrt
import vecteurs
import droites
import plans

def distance(pointA, pointB):
	"""Donne la distance entre deux points
	
	Args:
	    pointA (Point): Point A
	    pointB (Point): Point B
	
	Returns:
	    float: Distance entre A et B
	
	Raises:
	    TypeError: Si A ou B n'est pas un point
	"""
	if isinstance(pointA, Point) and isinstance(pointB, Point):
		return sqrt((pointB.x - pointA.x)**2 + (pointB.y - pointA.y)**2 + (pointB.z - pointA.z)**2)

	else:
		typeA = pointA.__class__.__name__
		typeB = pointB.__class__.__name__
		raise TypeError(f"Impossible de calculer la distance entre un [{typeA}] et [{typeB}]")


def est_meme_point(pointA, pointB):
	"""Renvoie True si les deux points sont au même endroit, False sinon
	
	Args:
	    pointA (Point): Point A
	    pointB (Point): Point B
	
	Returns:
	    bool: A et B au même endroit ?
	"""
	return distance(pointA, pointB) == 0

def alignes(pointA, pointB, *args):
	"""Renvoie True si les points sont alignés, False sinon
	
	Args:
	    pointA (Point): Point A
	    pointB (Point): Point B
	    *args: Autres points
	
	Returns:
	    bool: Points tous alignés ?
	
	Raises:
	    TypeError: Si les objets donnés ne sont pas tous des points
	"""
	if isinstance(pointA, Point) and isinstance(pointB, Point):

		for pointX in args:
			if isinstance(pointX, Point):
				if ((pointX.y - pointB.y)*(pointB.x - pointA.x) != (pointB.y - pointA.y)*(pointX.x - pointB.x)): 
					return False
			
			else:
				typeA = pointA.__class__.__name__
				typeB = pointX.__class__.__name__
				raise TypeError(f"Impossible de déterminer la collinéarité de points entre [{typeA}] et [{typeB}]")
		
		return True

	else:
		typeA = pointA.__class__.__name__
		typeB = pointB.__class__.__name__
		raise TypeError(f"Impossible de déterminer la colinéarité entre [{typeA}] et [{typeB}]")

class Point():

	"""Classe représentant un point de l'espace
	
	Attributes:
	    x (float): Coordonnée X
	    y (float): Coordonnée Y
	    z (float): Coordonnée Z
	"""
	
	def __init__(self, x=0 , y=0, z=0):
		"""Initialisation du point
		
		Args:
		    x (float): Coordonnée X
		    y (float): Coordonnée Y
		    z (float): Coordonnée Z
		"""
		self.x = x
		self.y = y
		self.z = z

	def distance_origine(self):
		"""Donne la distance à l'origine
		
		Returns:
		    float: Distance entre le point et l'origine
		"""
		return (distance(self, Point(0, 0, 0)))


	def projete_orthogonal(self, *args):
		"""Donne le projeté orthogonal du point sur une droite ou un plan

		Returns:
			Point: Projeté orthogonal
		"""
		if args[0] != None:
			if isinstance(args[0], droites.Droite):
				droite = args[0]
				vec = droite.vecteur
				a = droite.point
				b = Point(	droite.point.x + droite.vecteur.x,
							droite.point.y + droite.vecteur.y,
							droite.point.z + droite.vecteur.z)

				ab = vecteurs.Vecteur(a, b)
				ap = vecteurs.Vecteur(a, self)

				modif_vecteur = (ap.scalaire(ab) / ab.scalaire(ab)) * ab

				return Point(a.x + modif_vecteur.x,
							a.y + modif_vecteur.y,
							a.z + modif_vecteur.z)

			if isinstance(args[0], plans.Plan):
				plan = args[0]
				vec = vecteurs.Vecteur(plan.point, self)

				distance = plan.vecteur_n.scalaire(vec)
				difference = distance * plan.vecteur_n
				return Point(self.x - difference.x,
							self.y - difference.y,
							self.z - difference.z)

			else:
				raise TypeError(f"On ne peut projeter un point que sur une droite ou un plan")

		else:
			raise TypeError(f"Il faut un objet sur lequel projeter le point")


	def __str__(self):
		return f'Point({self.x}, {self.y}, {self.z})'

	def __repr__(self):
		return f'Point({self.x}, {self.y}, {self.z})'

origine = Point(0, 0, 0)

__all__ = ("Point", "origine", "distance", "est_meme_point", "alignes")
