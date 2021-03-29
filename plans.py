"""Module plans, contient la classe Plan et des fonctions annexes

Attributes:
    plan_xy (Plan): Plan d'équation z = 0 (horizontal)
    plan_xz (Plan): Plan d'équation y = 0 (vertical)
    plan_yz (Plan): Plan d'équation x = 0 (vertical)
"""
import droites
import vecteurs


def parallelles(planA, *args):
	"""Renvoie True si les plans donnés sont parallèles, False sinon
	
	Args:
	    planA (Plan): Plan de référence
	    *args: Autres plans
	
	Returns:
	    bool: Plans tous parallelles ?
	
	Raises:
	    TypeError: Si les objets donnés ne sont pas tous des plans
	"""
	if isinstance(planA, Plan):

		for planX in args:
			if isinstance(planX, Plan):
				if not(planX.vecteur_normal() == planA.vecteur_normal()):
					return False
			else:
				typeA = planA.__class__.__name__
				typeB = planX.__class__.__name__
				raise TypeError(f"Impossible de déterminer le parallélisme entre [{typeA}] et [{typeB}]")

		return True

	else:
		typeA = planA.__class__.__name__
		planX = args[0]
		typeB = planX.__class__.__name__
		raise TypeError(f"Impossible de déterminer le parallélisme entre [{typeA}] et [{typeB}]")

def secants(planA, *args):
	"""Renvoie True si les plans donnés sont sécants, False sinon
	
	Args:
	    planA (Plan): Plan de référence
	    *args: Autres plans
	
	Returns:
	    bool: Plans tous sécants ?
	
	Raises:
	    TypeError: Si les objets donnés ne sont pas tous des plans
	"""
	return not parallelles(planA, *args)

def plans_orthogonaux(planA, *args):
	"""Renvoie True si les plans donnés sont sécants, False sinon
	
	Args:
	    planA (Plan): Plan de référence
	    *args: Autres plans
	
	Returns:
	    bool: Plans tous sécants ?
	
	Raises:
	    TypeError: Si les objets donnés ne sont pas tous des plans
	"""
	if isinstance(planA, Plan):

		for planX in args:
			if isinstance(planX, Plan):
				if secants(planA, planX):
					if not(planX.vecteur_normal().scalaire(planA.vecteur_normal())) != 0:
						return False
				else:
					return False
			else:
				typeA = planA.__class__.__name__
				typeB = planX.__class__.__name__
				raise TypeError(f"Impossible de déterminer le parallélisme entre [{typeA}] et [{typeB}]")

		return True

	else:
		typeA = planA.__class__.__name__
		planX = args[0]
		typeB = planX.__class__.__name__
		raise TypeError(f"Impossible de déterminer le parallélisme entre [{typeA}] et [{typeB}]")


class Plan:

	"""Classe représentant un plan de l'espace
	
	Attributes:
	    point (points.Point): Point d'origine du plan
	    vecteur_n (vecteurs.Vecteur): Vecteur normal au plan
	"""
	
	def __init__(self, *args):
		"""Initialisation du plan :

			- Un point + un vecteur normal

			- Deux droites

			- Un point + deux vecteurs non colinéaires

			- Trois points
		
		Args:
		    *args: Arguments de définition du plan
		
		Raises:
		    TypeError: Les types passés sont incorrects
		    ValueError: Le vecteur normal est nul, les deux vecteurs sont colinéaires ou les trois points sont alignés
		"""
		import points
		if len(args) == 2:

			a, b = args

			#Point + Vecteur Normal
			if isinstance(a, points.Point) and isinstance(b, vecteurs.Vecteur):
				if not b.est_nul():
					self.point = a
					self.vecteur_n = b
				else:
					raise ValueError("Le vecteur normal d'un plan ne peut pas être nul")

			#Deux droites
			elif isinstance(a, droites.Droite) and isinstance(b, droites.Droite):
				raise NotImplementedError("La création d'un plan par deux droites n'est pas encore disponible")

			else:
				typeA = a.__class__.__name__
				typeB = b.__class__.__name__
				raise TypeError(f"Impossible de créer un plan à partir de [{typeA}] et [{typeB}]")

		elif len(args) == 3:

			a, b ,c = args

			#Point + Deux vecteurs
			if isinstance(a, points.Point) and (b, vecteurs.Vecteur) and isinstance(c, vecteurs.Vecteur):
				if not(b.est_nul() or c.est_nul()):
					if not vecteurs.collineaires(b, c):
						self.vecteur_n = b.produit_vectoriel(c)
						self.point = a
					else:
						raise ValueError("Deux vecteurs collinéaires ne peuvent pas engendrer un plan")
				else:
					raise ValueError("Impossible de générer un plan à partir d'un vecteur nul")

			#Trois points
			elif all(isinstance(x, points.Point) for x in args):
				ab = vecteurs.Vecteur(a, b)
				ac = vecteurs.Vecteur(b, c)

				if not(ab.est_nul() or ac.est_nul()):
					if not vecteurs.collineaires(ab, ac):
						self.vecteur_n = ab.produit_vectoriel(ac)
						self.point = a
					else:
						raise ValueError("Trois points alignés ne peuvent pas engendrer un plan")
				else:
					raise ValueError("Impossible de générer un plan : les points ne sont pas distincts")

			else:
				typeA = a.__class__.__name__
				typeB = b.__class__.__name__
				typeC = c.__class__.__name__
				raise TypeError(f"Impossible de créer un plan à partir de [{typeA}], [{typeB}] et [{typeC}]")

		elif len(args) == 4:
			pass
			a, b, c, d = args

			#Equation cartesienne
			if all(isinstance(x, int) or isinstance(x, float) for x in args):
				if not(a == 0 and b == 0 and c == 0):
					self.vecteur_n = vecteurs.Vecteur(a, b, c)

					if c != 0:
						self.point = points.Point(0, 0, -d/c)

					elif b != 0:
						self.point = points.Point(0, -d/b, 0)

					elif a != 0:
						self.point = points.Point(-d/a, 0, 0)

				else:
					raise ValueError("Impossible de générer un plan à partir d'un vecteur nul")
			else:
				raise TypeError("Les paramètres de l'équation cartésienne doivent être des chiffres")

	def cartesienne(self):
		"""Renvoie l'équation cartésienne du plan, et les coefficients dans un tuple
		
		Returns:
		    tuple:

		    - Equation cartésienne (str)

		    - Tuple avec les coefficients a b c d pour `ax + by + cz + d = 0`

		"""
		a = self.vecteur_n.x
		b = self.vecteur_n.y
		c = self.vecteur_n.z

		signe_b = "+ " if b >= 0 else ""
		signe_c = "+ " if c >= 0 else ""

		total_p = a * self.point.x + b * self.point.y + c * self.point.z

		d = -total_p
		signe_d = "+ " if d >= 0 else ""

		str_equation = f"{a}x {signe_b}{b}y {signe_c}{c}z {signe_d}{d} = 0"
		return (str_equation, (a, b, c, d))

	def vecteur_normal(self):
		"""Renvoie le vecteur normal au plan
		
		Returns:
		    vecteurs.Vecteur: Vecteur normal
		"""
		return self.vecteur_n

	def __contains__(self, point):
		if isinstance(point, points.Point):
			projete = point.projete_orthogonal(self)
			return points.est_meme_point(point, projete)

plan_xy = Plan(0, 0, 1, 0)
plan_yz = Plan(1, 0, 0, 0)
plan_xz = Plan(0, 1, 0, 0)

__all__ = ("Plan", "plan_xy", "plan_yz", "plan_xz")