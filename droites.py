import points
import vecteurs
from fractions import Fraction

def parallelles(d, *args):
	if isinstance(d, Droite):

		for d2 in args:
			if isinstance(d2, Droite):
				if not(vecteurs.collineaires(d.vecteur, d2.vecteur)):
					return False
		return True

	else:
		typeA = u.__class__.__name__
		typeB = v.__class__.__name__
		raise TypeError(f"Impossible de déterminer le parallélisme entre [{typeA}] et [{typeB}]")

def secantes(d, *args):
	raise NotImplementedError

def orthogonales(droite1, droite2):
	raise NotImplementedError 

class Droite:

	def __init__(self, *args):
		self.point = None
		self.vecteur = None

		if len(args) == 2:
			a, b = args

			if isinstance(a, points.Point) and isinstance(a, points.Point):
				u = vecteurs.Vecteur(a, b)
				self.vecteur = u
				self.point = a
		
			elif isinstance(a, points.Point) and isinstance(b, vecteurs.Vecteur):
				self.point = a
				self.vecteur = b
				
			else:
				raise ValueError(f"Une droite est créée à partir de deux points, ou d'un point et d'un vecteur")
		
		else:
			raise ValueError(f"Une droite est créée à partir de deux points, ou d'un point et d'un vecteur")

	@classmethod
	def axe_x(self):
		return Droite(points.origine, points.Point(1, 0, 0))

	@classmethod
	def axe_y(self):
		return Droite(points.origine, points.Point(0, 1, 0))

	@classmethod
	def axe_z(self):
		return Droite(points.origine, points.Point(0, 0, 1))

	def est_sur_droite(self, point):
		if isinstance(point, point.Point):
			pointA = self.point
			pointB = points.Point(pointA.x + self.vecteur.x, pointA.y + self.vecteur.y, pointA.z + self.vecteur.z)
			return bool(points.alignes(pointA, pointB, point))
		type_ = point.__class__.__name__
		raise TypeError(f"Impossible de déterminer l'appartenance entre droite et [{type_}]")

	def parametrique(self):
		xp = Fraction(str(self.point.x))
		yp = Fraction(str(self.point.y))
		zp = Fraction(str(self.point.z))

		xu = Fraction(str(self.vecteur.x))
		yu = Fraction(str(self.vecteur.y))
		zu = Fraction(str(self.vecteur.z))
		
		return f"x = {xp} + {xu}t\ny = {yp} + {yu}t\nz = {zp} + {zu}t"

	def __contains__(self, point):
		return self.est_sur_droite(point)

axe_x = Droite.axe_x()
axe_y = Droite.axe_y()
axe_z = Droite.axe_z()

__all__ = ("Droite", "axe_x", "axe_y", "axe_z")
d = Droite(points.Point(0.25, 0, 0), points.Point(0, 0, 0))
print(d.parametrique())
print(parallelles(d, axe_x))