import droites, plans, points, vecteurs
import numpy as np

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

def trouver_point_intersection(zero, a, b, equa_p1, equa_p2):
	normal1 = dict(zip(["x", "y", "z", "d"], equa_p1))
	normal2 = dict(zip(["x", "y", "z", "d"], equa_p2))
	a1 = normal1[a]
	b1 = normal1[b]
	d1 = normal1["d"]

	a2 = normal2[a]
	b2 = normal2[b]
	d2 = normal2["d"]

	A0 = ((b2 * d1) - (b1 * d2)) / ((a1 * b2 - a2 * b1))
	B0 = ((a1 * d2) - (a2 * d1)) / ((a1 * b2 - a2 * b1))

	coords = dict(zip([zero, a, b], [0, A0, B0]))
	return points.Point(coords["x"], coords["y"], coords["z"])

def intersection_plan_plan(planA, planB):
	"""Non implémenté
	"""
	equa_a = planA.cartesienne()[1]
	a, b, c, d = equa_a
	equa_b = planB.cartesienne()[1]
	a2, b2, c2, d2 = equa_b

	vec_a = planA.vecteur_n
	vec_b = planB.vecteur_n


	vec_d = vec_a.produit_vectoriel(vec_b)
	vec_d = vec_d.absolue()

	max_c = max(vec_d.x, vec_d.y, vec_d.z)

	if max_c == vec_d.z:
		print("z")
		point = trouver_point_intersection("z", "x", "y", equa_a, equa_b)
	elif max_c == vec_d.y:
		print("y")
		point = trouver_point_intersection("y", "z", "x", equa_a, equa_b)
	else:
		print("x")
		point = trouver_point_intersection("x", "y", "z", equa_a, equa_b)

	print(point)
	return droites.Droite(point, vec_a.produit_vectoriel(vec_b))