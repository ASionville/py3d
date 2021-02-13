from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import numpy as np

import points, droites, plans, vecteurs


class Trace3D:

	def __init__(self):
		#Création du graph
		self.fig = plt.figure()
		self.ax = self.fig.gca(projection='3d')

	def plot(self, objet, color="blue", longueur=10, label=""):
		longueur *= 5

		if isinstance(objet, points.Point):
			if label == "":
				self.ax.scatter(objet.x, objet.y, objet.z, marker="o")
			else:
				self.ax.scatter(objet.x, objet.y, objet.z, marker="o", label=label)

		elif isinstance(objet, droites.Droite):

			x = [-(objet.point.x + objet.vecteur.x * longueur),
				objet.point.x + objet.vecteur.x * longueur]
				
			y = [-(objet.point.y + objet.vecteur.y * longueur),
				objet.point.y + objet.vecteur.y * longueur]
				
			z = [-(objet.point.z + objet.vecteur.z * longueur),
				objet.point.z + objet.vecteur.z * longueur]
				
			if label == "":
				self.ax.plot(x, y, z, color)
			else:
				self.ax.plot(x, y, z, color, label=label)

	def draw_axes(self):
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

	def draw_origin(self):
		#Origine en rouge
		self.ax.scatter(0, 0, 0, color="black", label="Origine")


	def show(self):
		self.draw_axes()
		self.draw_origin()
		self.ax.legend(framealpha=0.2)
		plt.show()

trace3d = Trace3D()

d = droites.Droite(points.origine, points.Point(0.1, 0.1, 0.1))

trace3d.plot(d, label="Droite d")
trace3d.show()