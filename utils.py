"""Module utils : contient des variables globales (WIP)

Attributes:
    CHIFFRES_SIGNIFICATIFS (int): Nombres de chiffres significatifs dans les calculs
    MIN_DELTA (TYPE): Différence max pour que deux chiffres soit considérés égaux
    	(1/CHIFFRES_SIGNIFICATIFS)
"""
CHIFFRES_SIGNIFICATIFS = 10
MIN_DELTA = 1/(10 ** CHIFFRES_SIGNIFICATIFS)

__all__ = ("MIN_DELTA", "CHIFFRES_SIGNIFICATIFS")