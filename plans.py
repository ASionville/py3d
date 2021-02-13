import droites
import points
import vecteurs

class Plan:

	def __init__(self, *args):

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
				pass

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
		a = self.vecteur_n.x
		b = self.vecteur_n.y
		c = self.vecteur_n.z

		signe_b = "+ " if b >= 0 else ""
		signe_c = "+ " if c >= 0 else ""

		total_p = a * self.point.x + b * self.point.y + c * self.point.z

		d = -total_p
		signe_d = "+ " if d >= 0 else ""

		return f"{a}x {signe_b}{b}y {signe_c}{c}z {signe_d}{d} = 0"


plan_xy = Plan(0, 0, 1, 0)
plan_yz = Plan(1, 0, 0, 0)
plan_xz = Plan(0, 1, 0, 0)

__all__ = ("Plan", "plan_xy", "plan_yz", "plan_xz")

if __name__ == "__main__":
	u = vecteurs.vecteur_unitaire_x
	v = vecteurs.vecteur_unitaire_y
	p = Plan(1, 1, -1, 1)
	print(p.vecteur_n, p.point)
	print(p.cartesienne())