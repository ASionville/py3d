import droites, plans, points, vecteurs
from utils import MIN_DELTA

def intersection(ObjetA, ObjetB):
	"""Sert de fonction tampon pour renvoyer l'intersection entre A et B
	"""

	if isinstance(ObjetA, droites.Droite):

		if isinstance(ObjetB, droites.Droite):

			if droites.secantes(ObjetA, ObjetB):
				return intersection_droite_droite(ObjetA, ObjetB)
			else:
				return None

		elif isinstance(ObjetB, plans.Plan):
			if droites.secante_plan(ObjetA, ObjetB):
				return intersection_droite_plan(ObjetA, ObjetB)
			else:
				return None

		else:
			typeA = ObjetA.__class__.__name__
			typeB = ObjetB.__class__.__name__
			raise TypeError(f"Impossible de déterminer l'intersection entre [{typeA}] et [{typeB}]")

	elif isinstance(ObjetA, plans.Plan):

		if isinstance(ObjetB, droites.Droite):

			if droites.secante_plan(ObjetB, ObjetA):
				return intersection_droite_plan(ObjetB, ObjetA)
			else:
				return None

		elif isinstance(ObjetB, plans.Plan):
			if plans.secants(ObjetA, ObjetB):
				return intersection_plan_plan(ObjetA, ObjetB)
			else:
				return None			

	else:
		return None

def intersection_droite_droite(droiteA, droiteB):
	"""Non implémenté
	"""
	v = droiteA.vecteur
	v2 = droiteB.vecteur

	p = droiteA.point
	p2 = droiteB.point

	v3 = vecteurs.Vecteur(p, p2).produit_vectoriel(v2)
	v4 = v.produit_vectoriel(v2)

	scalaire = v4.scalaire(v4)
	if scalaire == 0:
		return None

	alpha = v3.scalaire(v4) / scalaire

	point = points.Point(droiteA.point.x + alpha * droiteA.vecteur.x,
						droiteA.point.y + alpha * droiteA.vecteur.y,
						droiteA.point.z + alpha * droiteA.vecteur.z)

	return point

def intersection_droite_plan(droite, plan):
	"""Non implémenté
	"""
	p = droite.point
	v = droite.vecteur

	dot1 = plan.vecteur_n.scalaire(vecteurs.Vecteur(p.x, p.y, p.z))
	dot2 = plan.vecteur_n.scalaire(v)

	if dot2 == 0:
		return None
	
	d = plan.cartesienne()[1][-1]
	t = -(dot1 - d) / dot2

	return points.Point(p.x + (v.x*t), p.y + (v.y*t), p.z + (v.z*t))

def resoudre_cramer(equa_a, equa_b):
	a, b, c, d = equa_a
	a2, b2, c2, d2 = equa_b

	d, d2 = -d, -d2

	det = b * c2 - 	c * b2
	alpha = (d * c2 - c * d2) / det
	beta = (b * d2 - d * b2) / det
	return alpha, beta

def intersection_plan_plan(planA, planB):
	"""Non implémenté
	"""
	equa_a = planA.cartesienne()[1]
	equa_b = planB.cartesienne()[1]

	vec_a = planA.vecteur_n
	vec_b = planB.vecteur_n

	vec_d = vec_a.produit_vectoriel(vec_b)

	if abs(vec_d.x) > MIN_DELTA:
		#X non nul -> on prend x = 0
		x = 0
		y, z = resoudre_cramer(equa_a, equa_b)

	elif abs(vec_d.y) > MIN_DELTA:
		#Y non nul -> on prend y = 0
		y = 0
		x, z = resoudre_cramer(equa_a, equa_b)

	else:
		#Z non nul -> on prend z = 0
		z = 0
		x, y = resoudre_cramer(equa_a, equa_b)

	point = points.Point(x, y, z)

	d = droites.Droite(point, vec_d)

	return d

__all__ = ("intersection", "intersection_plan_plan", "intersection_droite_plan", "intersection_droite_droite")
