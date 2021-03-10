import unittest
import droites, plans, points, repere, utils, vecteurs

class TestsPoints(unittest.TestCase):

	def test_coords(self):

		#Origine
		p = points.origine
		self.assertEqual(p.x, 0)
		self.assertEqual(p.y, 0)
		self.assertEqual(p.z, 0)

		#Point random
		p = points.Point(3, -7, 5.3)
		self.assertEqual(p.x, 3)
		self.assertEqual(p.y, -7)
		self.assertEqual(p.z, 5.3)

		#Point sans Z
		p = points.Point(3, -7)
		self.assertEqual(p.z, 0)

	def test_distance(self):

		#Distance point-origine
		a = points.origine
		b = points.Point(1, 1, 1)
		self.assertEqual(points.distance(a, b), 3**0.5)

		#Distance point positif - point positif
		a = points.Point(2, 3, 4)
		b = points.Point(1, 1, 1)
		self.assertEqual(points.distance(a, b), ((2-1)**2 + (3-1)**2 + (4-1)**2)**0.5)

	def test_distance_origine(self):

		#Origine
		p = points.origine
		self.assertEqual(p.distance_origine(), 0)

		#Point random
		p = points.Point(4, 2, 3)
		self.assertEqual(p.distance_origine(), (4**2 + 2**2 + 3**2)**0.5)


	def test_projete_sur_droite(self):

		#Origine -> Droite x=t, y=0, z=1
		p = points.origine
		d = droites.Droite(points.Point(0, 0, 1), points.Point(1, 0, 1))
		projete = p.projete_orthogonal(d)
		self.assertEqual(projete.x, 0)
		self.assertEqual(projete.y, 0)
		self.assertEqual(projete.z, 1)


		#Point random sur droite inclinée
		#...

	def test_projete_sur_plan(self):
		pass
