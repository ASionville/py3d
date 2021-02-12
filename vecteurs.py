from math import sqrt
import points

def collineaire(u, *args):
	if isinstance(u, Vecteur) and isinstance(v, Vecteur):

		for v in args:
			if isinstance(v, Point):
				if abs(abs(u * v) - u.norme() * v.norme()) >= get_eps():
					return False
		return True

	else:
		typeA = u.__class__.__name__
		typeB = v.__class__.__name__
		raise TypeError(f"Impossible de déterminer la colinéarité entre [{typeA}] et [{typeB}]")

class Vecteur():

	def __init__(self, *args):

		if len(args) == 2:
			a, b = args
			if isinstance(a, points.Point) and isinstance(b, points.Point):
				self.x = b.x - a.x
				self.y = b.y - a.y
				self.z = b.z - a.z
				return self

			if all(isinstance(coord, int) or isinstance(coord, float) for coord in args):
				a, b = args
				self.x = a
				self.y = b
				self.z = 0
				return self

			else:
				typeA = a.__class__.__name__
				typeB = b.__class__.__name__
				raise TypeError(f"Impossible de créer un vecteur à partir de [{typeA}] et [{typeB}]")

		elif len(args) == 3:
			if all(isinstance(coord, int) or isinstance(coord, float) for coord in args):
				x, y ,z = args
				self.x = x
				self.y = y
				self.z = z
			else:
				raise TypeError("Les coordonnées d'un vecteur doivent être des nombres")

		else:
			raise ValueError("Un vecteur est créé à partir de deux points ou de coordonnées")

	def scalaire(self, VectorB):
		if isinstance(VectorB, Vecteur):
			return self.x * VectorB.x + self.y * VectorB.y + self.z * VectorB.z
		else:
			type_ = VectorB.__class__.__name__
			raise TypeError(f"Impossible de faire le produit scalaire entre [Vecteur] et [{type_}]")

	def norme(self):
		return sqrt((self.x)**2 + (self.y)**2 + (self.z)**2)

	def absolue(self):
		return Vecteur(abs(self.x), abs(self.z), abs(self.z))

	def normal(self):
		if self.z == 0:
			return Vecteur(self.y, -self.x, 0)
		elif self.y == 0:
			return Vecteur(-self.z, 0, self.x)
		elif self.x == 0:
			return Vecteur(0, self.z, -self.y)
		else:
			raise ValueError("L'implémentation du vecteur normal à un Vecteur 3D non effectuée")
		return Vecteur(-self.y, self.x, 0)

	def get_coordonnes(self):
		return (self.x, self.y, self.z)

	def est_nul(self):
		return self.x == 0 and self.y == 0 and self.z == 0

	def __add__(self, VectorB):
		if isinstance(VectorB, Vecteur):
			return Vecteur(self.x + VectorB.x, self.y + VectorB.y, self.z + VectorB.z)
		else:
			type_ = VectorB.__class__.__name__
			raise TypeError(f"Impossible d'additioner [Vecteur] et [{type_}]")

	def __radd__(self, VectorB):
		if VectorB == 0:
			return self
		else:
			return self.__add__(VectorB)

	def __neg__(self):
		return Vecteur(-self.x, -self.y, -self.z)

	def __sub__(self, VectorB):
		return self.__add__(-VectorB)

	def __rsub__(self, VectorB):
		return self.__radd__(-VectorB)

	def __mul__(self, valeur):
		if isinstance(valeur, int) or isinstance(valeur, float):
			return Vecteur(self.x * valeur, self.y * valeur, self.z * valeur)
		else:
			type_ = valeur.__class__.__name__
			raise TypeError(f"Impossible de multiplier [Vecteur] et [{type_}]")

	def __rmul__(self, valeur):
		return self.__mul__(valeur)

	def __str__(self):
		return f"Vecteur ({self.x}, {self.y}, {self.z})"

vecteur_unitaire_x = Vecteur(1, 0, 0)
vecteur_unitaire_y = Vecteur(0, 1, 0)
vecteur_unitaire_z = Vecteur(0, 0, 1)
vecteur_nul = Vecteur(0, 0, 0)

__all__ = ("Vecteur", "vecteur_unitaire_x", "vecteur_unitaire_y", "vecteur_unitaire_z", "vecteur_nul")
