import droites
import points
import vecteurs

class Plan:

	def __init__(self, *args):

		if len(args) == 2:

			a, b = args
			#Deux vecteurs
			if isinstance(a, vecteurs.Vecteur) and isinstance(b, vecteurs.Vecteur):
				if not(a.est_nul() or b.est_nul()):
					if not vecteurs.collineaires(a, b):
						

u = vecteurs.vecteur_unitaire_x
v = vecteurs.vecteur_unitaire_y
p = Plan(u, v)