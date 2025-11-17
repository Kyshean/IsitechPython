'''
Créez une fonction saluer_personne qui :
Prend en paramètre un nom et une heure (0-23)
Retourne "Bonjour" si l'heure est entre 6 et 12
Retourne "Bon après-midi" si l'heure est entre 12 et 18
Retourne "Bonsoir" si l'heure est entre 18 et 24
Retourne "Bonne nuit" pour les autres heures
'''

from datetime import *

heure_actuelle = int(datetime.today().strftime("%H")) # On passe l'heure en tant que entier pour pouvoir mieux les utiliser dans la comparaison.
nom = input("Entrez votre nom ici: ")

def saluer_personne(nom): # On compare l'heure directement dans la fonction et l'appel de celle ci.
    if 6 <= heure_actuelle < 12:
        return f"bon matin {nom}!"
    elif 12 <= heure_actuelle < 18:
        return f"bonne après-midi {nom}!"
    elif 18 <= heure_actuelle() < 24:
        return f"Bonne soirée {nom}"
    else:
        return f"Bonne nuit {nom}"

print(saluer_personne(nom))