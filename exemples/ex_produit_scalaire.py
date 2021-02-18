import py3d

#Demander à l'utilisateur les coordonnées de u
u_demande = input("Donner les coordonnées de u, séparées par des espaces")

#Couper le texte à chaque espace (donne la liste des coordonnées)
u_demande = u_demande.split(" ")

#Récupérer les coordonnées
u_x = u_demande[0]
u_y = u_demande[1]
u_z = u_demande[2]


#Faire la même chose avec v
v_demande = input("Donner les coordonnées de v, séparées par des espaces")

#Couper le texte à chaque espace (donne la liste des coordonnées)
v_demande = v_demande.split(" ")

#Récupérer les coordonnées
v_x = v_demande[0]
v_y = v_demande[1]
v_z = v_demande[2]

#Créer u et v
u = py3d.Vecteur(u_x, u_y, u_z)
v = py3d.Vecteur(v_x, v_y, v_z)

#Faire le produit scalaire entre les deux vecteurs
produit_scalaire = u.scalaire(v)

#Donner le résultat
if produit_scalaire == 0:
    print("u et v sont collinéaires : u.v = ", produit_scalaire)

else:
    print("u et v ne sont pas collinéaires : u.v = ", produit_scalaire)
