"""Module droites, contient la classe Droite et des fonctions annexes

Attributes:
    axe_x (Droite): Droite de l'axe X
    axe_y (Droite): Droite de l'axe Y
    axe_z (Droite): Droite de l'axe Z
"""
import points
import vecteurs
from fractions import Fraction

def parallelles(d, *args):
	"""Renvoie True si les droites données sont parallèles, False sinon
	
	Args:
	    d (Droite): Droite de référence
	    *args: Autres droites
	
	Returns:
	    bool: Droites toutes parallèles ?
	
	Raises:
	    TypeError: Si les objets donnés ne sont pas tous des droites
	"""
	if isinstance(d, Droite):

		for d2 in args:
			if isinstance(d2, Droite):
				if not(vecteurs.collineaires(d.vecteur, d2.vecteur)):
					return False
			else:
				typeA = u.__class__.__name__
				typeB = v.__class__.__name__
				raise TypeError(f"Impossible de déterminer le parallélisme entre [{typeA}] et [{typeB}]")
				
		return True

	else:
		typeA = u.__class__.__name__
		v = args[0]
		typeB = v.__class__.__name__
		raise TypeError(f"Impossible de déterminer le parallélisme entre [{typeA}] et [{typeB}]")

def secantes(d, *args):
	"""Renvoie True si les droites données sont sécantes, False sinon
	
	Args:
	    d (Droite): Droite de référence
	    *args: Autres droites
	
	Returns:
	    bool: Droites toutes sécantes ?
	
	Raises:
	    TypeError: Si les objets donnés ne sont pas tous des droites
	"""
	if isinstance(d, Droite):
		
		for d2 in args:
			if isinstance(d2, Droite):
				produit = d.vecteur.produit_vectoriel(d2.vecteur)
				vect_deplacement = vecteurs.Vecteur(d.point, d2.point)
				if produit.scalaire(vect_deplacement) != 0:
					return False
			else:
				typeA = d.__class__.__name__
				typeB = d2.__class__.__name__
				raise TypeError(f"Impossible de déterminer l'intersection entre [{typeA}] et [{typeB}]")

		return True

	else:
		typeA = d.__class__.__name__
		d2 = args[0]
		typeB = d2.__class__.__name__
		raise TypeError(f"Impossible de déterminer l'intersection entre [{typeA}] et [{typeB}]")


def secante_plan(droite, plan):
	"""Renvoie True si la droite donnée est sécante avec le plan, False sinon
	
	Args:
	    droite (Droite): Droite
	    plan (Plan): Plan
	
	Returns:
	    bool: Droite et plan sécants ?
	
	Raises:
	    TypeError: Si les objets donnés ne sont pas une droite et un plan
	"""
	import plans
	if isinstance(droite, Droite):
		
		if isinstance(plan, plans.Plan):
			if droite.vecteur.scalaire(plan.vecteur_n) == 0:
				return False
		else:
			typeA = d.__class__.__name__
			typeB = plan.__class__.__name__
			raise TypeError(f"Impossible de déterminer l'intersection entre [{typeA}] et [{typeB}]")
		
		return True

	else:
		typeA = droite.__class__.__name__
		typeB = plan.__class__.__name__
		raise TypeError(f"Impossible de déterminer l'intersection entre [{typeA}] et [{typeB}]")


def orthogonales(droite1, droite2):
	"""Renvoie True si les droites données sont orthogonales, False sinon
	
	Args:
	    droite1 (Droite): Droite 1
	    droite2 (Droite): Droite 2
	
	Returns:
	    bool: Droites orthogonales ?
	
	Raises:
	    TypeError: Si les objets donnés ne sont pas tous des droites
	"""
	if isinstance(droite1, Droite):
		if isinstance(droite2, Droite):
			if secantes(droite1, droite2):
				if vecteurs.orthogonaux(droite1.vecteur, droite2.vecteur):
					return True
			return False

		else:
			typeA = droite1.__class__.__name__
			typeB = droite2.__class__.__name__
			raise TypeError(f"Impossible de déterminer l'intersection entre [{typeA}] et [{typeB}]")

	else:
		typeA = droite1.__class__.__name__
		typeB = droite2.__class__.__name__
		raise TypeError(f"Impossible de déterminer l'intersection entre [{typeA}] et [{typeB}]")


class Droite:

	"""Classe représentant une droite de l'espace
	
	Attributes:
	    point (points.Point): Un point appartenant à la droite
	    vecteur (vecteurs.Vecteur): Vecteur directeur de la droite
	"""
	
	def __init__(self, *args):
		"""Initialisation de la droite

			- Deux points

			- Un point + un vecteur
		
		Args:
		    *args: Arguments de définition de la droite
		
		Raises:
		    TypeError: Les types passés sont incorrects
		    ValueError: Les deux points son identiques ou le vecteur directeur est nul
		"""
		self.point = None
		self.vecteur = None

		if len(args) == 2:
			a, b = args

			if isinstance(a, points.Point) and isinstance(b, points.Point):
				if not points.est_meme_point(a, b):
					u = vecteurs.Vecteur(a, b)
					self.vecteur = u
					self.point = a
				else:
					raise ValueError("Les deux points ne doivent pas être identiques")
		
			elif isinstance(a, points.Point) and isinstance(b, vecteurs.Vecteur):
				if not b.est_nul():
					self.point = a
					self.vecteur = b
				else:
					raise ValueError("Le vecteur directeur ne doit pas être nul")
				
			else:
				raise TypeError(f"Une droite est créée à partir de deux points, ou d'un point et d'un vecteur")
		
		else:
			raise TypeError(f"Une droite est créée à partir de deux points, ou d'un point et d'un vecteur")

	def est_sur_droite(self, point):
		"""Renvoie True si le point est sur la droite, False sinon
		
		Args:
		    point (points.Point): Point quelconque
		
		Returns:
		    bool: Point sur la droite ?
		
		Raises:
		    TypeError: Si l'objet donné n'est pas un point
		"""
		if isinstance(point, point.Point):
			pointA = self.point
			pointB = points.Point(pointA.x + self.vecteur.x, pointA.y + self.vecteur.y, pointA.z + self.vecteur.z)
			return bool(points.alignes(pointA, pointB, point))

		type_ = point.__class__.__name__
		raise TypeError(f"Impossible de déterminer l'appartenance entre droite et [{type_}]")

	def parametrique(self):
		"""Renvoie l'équation paramétrique de la droite, et les coefficients dans un tuple
		
		Returns:
		    tuple:

		    - Equation paramétrique (str)

		    - Tuple avec les coefficients xp, yp, zp, xu, yu, zu pour


        \\begin{equation}
        	x= xp + x\\overrightarrow{u}
        \\end{equation}

        \\begin{equation}
        	y= y + y\\overrightarrow{u}
        \\end{equation}

        \\begin{equation}
        	z= zp + z\\overrightarrow{u}
        \\end{equation}
		"""
		xp = Fraction(str(self.point.x))
		yp = Fraction(str(self.point.y))
		zp = Fraction(str(self.point.z))

		xu = Fraction(str(self.vecteur.x))
		yu = Fraction(str(self.vecteur.y))
		zu = Fraction(str(self.vecteur.z))

		signe_xu = "+ " if xu >= 0 else ""
		signe_yu = "+ " if yu >= 0 else ""
		signe_zu = "+ " if zu >= 0 else ""
		
		str_parametrique = f"x = {xp} {signe_xu}{xu}t\ny = {yp} {signe_yu}{yu}t\nz = {zp} {signe_zu}{zu}t"
		return (str_parametrique, (xp, yp, zp, xu, yu, zu))

	def __contains__(self, point):
		return self.est_sur_droite(point)

	def __str__(self):
		return self.paramétrique[0]

	def __repr__(self):
		return self.paramétrique[0]

axe_x = Droite(points.origine, points.Point(1, 0, 0))
axe_y = Droite(points.origine, points.Point(0, 1, 0))
axe_z = Droite(points.origine, points.Point(0, 0, 1))

__all__ = ("Droite", "axe_x", "axe_y", "axe_z", "parallelles", "secantes", "orthogonales")