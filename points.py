from math import sqrt
import vecteurs

def distance(pointA, pointB):
	if isinstance(pointA, Point) and isinstance(pointB, Point):
		return sqrt((pointB.x - pointA.x)**2 + (pointB.y - pointA.y)**2 + (pointB.z - pointA.z)**2)

	else:
		typeA = pointA.__class__.__name__
		typeB = pointB.__class__.__name__
		raise TypeError(f"Impossible de calculer la distance entre un [{typeA}] et [{typeB}]")


def est_meme_point(pointA, pointB):
	return distance(pointA, pointB) == 0

def alignes(pointA, pointB, *args):
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

	def __init__(self, x=0 , y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	@classmethod
	def origine(self):
		return Point(0, 0, 0)

	def distance_origine(self):
		return (distance(self, Point(0, 0, 0)))

	def __str__(self):
		return f'Point({self.x}, {self.y}, {self.z})'

	def __repr__(self):
		return f'Point({self.x}, {self.y}, {self.z})'

origine = Point.origine()

__all__ = ("Point", "origine", "distance", "est_meme_point", "alignes")
