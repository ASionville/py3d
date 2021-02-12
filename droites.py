import points
import vecteurs

class Droite:

	def __init__(self):
		self.point = None
		self.vecteur = None

	@classmethod
	def axe_x(self):
		return Droite().par_points(points.origine, points.Point(1, 0, 0))

	@classmethod
	def axe_y(self):
		return Droite().par_points(points.origine, points.Point(0, 1, 0))

	@classmethod
	def axe_z(self):
		return Droite().par_points(points.origine, points.Point(0, 0, 1))

	@classmethod
	def par_points(self, PointA, PointB):
		if isinstance(PointA, points.Point) and isinstance(PointB, points.Point):
			u = vecteurs.Vecteur().par_points(PointA, PointB)
			self.vecteur = u
			self.point = PointA
			return self
	
	@classmethod
	def par_point_vecteur(self, Point, Vecteur):
		if isinstance(Point, points.Point) and isinstance(Vecteur, vecteurs.Vecteur):
			self.point = Point
			self.vecteur = Vecteur
			return self
		else:
			type_point = Point.__class__.__name__
			type_vector = Vecteur.__class__.__name__
			raise ValueError(f"Il faut un point et un vecteur, vous avez donné un [{type_point}] et un [{type_vector}]")

	def est_sur_droite(self, Point):
		PointA = self.point
		PointB = points.Point(PointA.x + self.vecteur.x, PointA.y + self.vecteur.y, PointA.z + self.vecteur.z)
		return bool(points.collineaire(PointA, PointB, Point))

	def __contains__(self, Point):
		return self.est_sur_droite(Point)

axe_x = Droite.axe_x()
axe_y = Droite.axe_y()
axe_z = Droite.axe_z()

__all__ = ("Droite", "axe_x", "axe_y", "axe_z")
