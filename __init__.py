"""Module py3D, pour gérer la géométrie 3D en python
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from droites import *
from plans import *
from points import *
from repere import *
from utils import *
from vecteurs import *
from calculs import *

__all__ = ("Droite", "axe_x", "axe_y", "axe_z", "parallelles", "secantes", "orthogonales",
	"Plan", "plan_xy", "plan_yz", "plan_xz",
	"Point", "origine", "distance", "est_meme_point", "alignes",
	"Repere3D",
	"MIN_DELTA", "CHIFFRES_SIGNIFICATIFS",
	"Vecteur", "vecteur_unitaire_x", "vecteur_unitaire_y", "vecteur_unitaire_z", "vecteur_nul", "collineaires", "orthogonaux",
	"intersection", "intersection_plan_plan", "intersection_droite_plan", "intersection_droite_droite")
