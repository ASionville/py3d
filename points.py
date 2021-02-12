from math import sqrt
import vecteurs

def distance(PointA, PointB):
	if isinstance(PointA, Point) and isinstance(PointB, Point):
		return sqrt((PointB.x - PointA.x)**2 + (PointB.y - PointA.y)**2 + (PointB.z - PointA.z)**2)

	else:
		typeA = PointA.__class__.__name__
		typeB = PointB.__class__.__name__
		raise TypeError(f"Impossible de calculer la distance entre un [{typeA}] et [{typeB}]")


def est_meme_point(PointA, PointB):
	return distance(PointA, PointB) == 0

def collineaire(PointA, PointB, *args):
	if isinstance(PointA, Point) and isinstance(PointB, Point):

		for PointX in args:
			if isinstance(PointX, Point):
				if ((PointX.y - PointB.y)*(PointB.x - PointA.x) != (PointB.y - PointA.y)*(PointX.x - PointB.x)): 
					return False
			
			else:
				typeA = PointA.__class__.__name__
				typeB = PointX.__class__.__name__
				raise TypeError(f"Impossible de déterminer la collinéarité de points entre [{typeA}] et [{typeB}]")
		
		return True

	else:
		typeA = PointA.__class__.__name__
		typeB = PointB.__class__.__name__
		raise TypeError(f"Impossible de déterminer la colinéarité entre [{typeA}] et [{typeB}]")

class Point():

	def __init__(self, x=0 , y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	@classmethod
	def origine(self):
		return Point(0, 0, 0)

	def distance_origine(self):
		return (distance(self, Point(0, 0, 0)))

origine = Point.origine()

__all__ = ("Point", "origin")
