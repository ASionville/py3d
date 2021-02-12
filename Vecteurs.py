from math import sqrt
import Points

class Vecteur():

	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	@classmethod
	def vecteur_unitaire_x(self):
		return Vecteur(1, 0, 0)

	@classmethod
	def vecteur_unitaire_y(self):
		return Vecteur(0, 1, 0)

	@classmethod
	def vecteur_unitaire_z(self):
		return Vecteur(0, 0, 1)

	@classmethod
	def par_points(self, PointA, PointB):
		if isinstance(PointA, Points.Point) and isinstance(PointB, Points.Point):
			self.x = PointB.x - PointA.x
			self.y = PointB.y - PointA.y
			self.z = PointB.z - PointA.z
			return self

		else:
			typeA = PointA.__class__.__name__
			typeB = PointB.__class__.__name__
			raise TypeError(f"Impossible de créer un vecteur à partir de [{typeA}] et [{typeB}]")

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

vecteur_unitaire_x = Vecteur.vecteur_unitaire_x()
vecteur_unitaire_y = Vecteur.vecteur_unitaire_y()
vecteur_unitaire_z = Vecteur.vecteur_unitaire_z()