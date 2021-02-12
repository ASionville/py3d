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
					if not vecteurs.collineaire(a, b):
						print("ok")
					else:
						print(1)
				else:
					print(2)
		else:
			print(3)


p = Plan(vecteurs.Vecteur(0, 1, 0), vecteurs.Vecteur(1, 0, 0))