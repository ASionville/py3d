"""Module tracer, contient le nécessaire pour l'affichage dans un tracé 3D
"""
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import numpy as np

import points, droites, plans, vecteurs


class Repere3D:

	"""Classe Trace3D, représente le repère 3D
	"""
	
	def __init__(self):
		"""Initialisation du repère
		"""
		#Création du graphique
		self.fig = plt.figure()
		self.ax = self.fig.gca(projection='3d')

	def ajouter(self, objet, couleur=None, longueur=10, label="", grille=0):
		"""Ajoute un objet dans le repère
		
		Args:
		    objet : Objet (Point / Droite / Plan) à ajouter
		    couleur (str, optionnel): Couleur à utiliser (en anglais)
		    longueur (int, optionnel): Longueur totale sur chaque axe (pour les droites)
		    label (str, optionnel): Label à attribuer à l'objet
		    grille (int, optionnel): Mode "grillage", avec {grille} lignes et {grille} colonnes (pour les plans)
		"""
		longueur *= 5

		if isinstance(objet, points.Point):
			if label == "":
				if couleur == None:
					self.ax.scatter(objet.x, objet.y, objet.z, marker="o")
				else:
					self.ax.scatter(objet.x, objet.y, objet.z, marker="o", couleur=couleur)
			else:
				if couleur == None:
					self.ax.scatter(objet.x, objet.y, objet.z, marker="o", label=label)
				else:
					self.ax.scatter(objet.x, objet.y, objet.z, marker="o", label=label, couleur=couleur)

		elif isinstance(objet, droites.Droite):

			#Droites en bleu par défaut
			couleur = "blue" if couleur == None else couleur
			
			x = [-(objet.point.x + objet.vecteur.x * longueur),
				objet.point.x + objet.vecteur.x * longueur]

			y = [-(objet.point.y + objet.vecteur.y * longueur),
				objet.point.y + objet.vecteur.y * longueur]

			z = [-(objet.point.z + objet.vecteur.z * longueur),
				objet.point.z + objet.vecteur.z * longueur]

			if label == "":
				self.ax.plot(x, y, z, couleur)
			else:
				self.ax.plot(x, y, z, couleur, label=label)

		elif isinstance(objet, plans.Plan):

			#Plans en orange par défaut
			couleur = "orange" if couleur == None else couleur

			longueur = int(longueur / 5)
			a, b, c, d = objet.cartesienne()[1]

			if c != 0:
				x = np.linspace(-longueur/2, longueur/2, longueur*10)
				y = np.linspace(-longueur/2, longueur/2, longueur*10)

				X, Y = np.meshgrid(x, y)
				Z = (d - a*X - b*Y) / c


			elif b != 0:
				x = np.linspace(-longueur/2, longueur/2, longueur*10)
				z = np.linspace(-longueur/2, longueur/2, longueur*10)

				X, Z = np.meshgrid(x, z)
				Y = (d - a*X - c*Z) / b


			else:
				y = np.linspace(-longueur/2, longueur/2, longueur*10)
				z = np.linspace(-longueur/2, longueur/2, longueur*10)

				Y, Z = np.meshgrid(y, z)
				X = (d - b*Y - c*Z) / a

			if grille != 0:
				#Mode grillage
				self.ax.plot_wireframe(X, Y, Z, color=couleur, alpha=0.6,
					rcount=grille, ccount=grille)
			else:
				self.ax.plot_surface(X, Y, Z, color=couleur, alpha=0.6)

	def dessiner_axes(self):
		"""Ajoute les axes au repère
		"""
		#Ajout des axes
		self.ax.set_xlabel("Axe X")
		self.ax.set_ylabel("Axe Y")
		self.ax.set_zlabel("Axe Z")

		axe_x = droites.axe_x
		axe_y = droites.axe_y
		axe_z = droites.axe_z
		plt.quiver(axe_x.point.x, axe_x.point.y, axe_x.point.z,
			axe_x.vecteur.x, axe_x.vecteur.y, axe_x.vecteur.z,
			color="red")
		plt.quiver(axe_y.point.x, axe_y.point.y, axe_y.point.z,
			axe_y.vecteur.x, axe_y.vecteur.y, axe_y.vecteur.z,
			color="green")
		plt.quiver(axe_z.point.x, axe_z.point.y, axe_z.point.z,
			axe_z.vecteur.x, axe_z.vecteur.y, axe_z.vecteur.z,
			color="blue")

	def dessiner_origine(self):
		"""Ajoute l'origine au repère
		"""
		#Origine en rouge
		self.ax.scatter(0, 0, 0, color="black", label="Origine")


	def afficher(self):
		"""Affiche le repère et la légende
		"""
		self.dessiner_axes()
		self.dessiner_origine()
		self.ax.legend(framealpha=0.2)
		plt.show()

__all__ = ("Repere3D", )