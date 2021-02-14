# 3Dpy

Un module python en français, qui vise à simplifier les programmes utilisants de la géométrie 2D ou 3D.

  Il vise à être utilisé par les <b>collégiens, lycéens et étudiants</b> afin de faciliter leurs projets ou leurs démonstration incluant de la géométrie 2D / 3D
  
  
## Installation

  Vous pouvez installer ce module en allant [ici](https://github.com/ASionville/3dpy/releases) puis en téléchargeant le ZIP le plus récent.<br>
  Ensuite, vous n'avez plus qu'à dézipper le tout et à placer le dossier dans votre projet.
  
  >Un package *pip* pour une installation plus simple sera disponible à terme
  
  *Ce qui suit n'est pas nécessaire en installant 3dpy par pip*
  Vous aurez également besoin de ces deux modules : `matplotlib` et `numpy`.
  
  Pour les installer, ouvrez un terminal en mode administrateur et tapez `pip install matplotlib numpy`

## Utilisation

  Nous nous baserons sur un dossier organisé comme ceci :
  
    .                           # Votre dossier de projet
    ├── 3dpy                    # Dossier 3dpy
    │   ├── droites.py
    │   ├── vecteurs.py
    │   └── ...
    ├── code1.py                 # Fichier de code 1
    ├── code2.py                 # Autre code
    └── ...


Nous recommandons de ne **pas** importer les fonctions de cette manière:
```python
from 3dpy import *
```

Mais plutôt de cette manière :
```python
import 3dpy
```

<br>

Example basique d'utilisation :
```python
import 3dpy

#Création de deux vecteurs u et v
u = py3d.Vecteur(0, 0, 1)
v = py3d.Vecteur(0, 0, 10)

#Est ce que les vecteurs sont collinéaires ? -> True
print(py3d.collineaires(u, v))
```
