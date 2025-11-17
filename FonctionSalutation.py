'''
Créez une fonction saluer_personne qui :
Prend en paramètre un nom et une heure (0-23)
Retourne "Bonjour" si l'heure est entre 6 et 12
Retourne "Bon après-midi" si l'heure est entre 12 et 18
Retourne "Bonsoir" si l'heure est entre 18 et 24
Retourne "Bonne nuit" pour les autres heures
'''

from datetime import *
heure_actuelle = datetime.today().strftime("%H:%M:%S")
nom = input("Entrez votre nom ici:")

def saluer(nom):
    if heure_actuelle("%H") > 6 and heure_actuelle("%H") < 12:
        print("bon matin {nom}!")
        return saluer(nom)
    elif heure_actuelle("%H") > 12 and heure_actuelle("%H") < 18:
        print("Bon midi {nom}!")
        return saluer(nom)
    elif heure_actuelle("%H") >= 18 and heure_actuelle("%H") < 24:
        print("Bonne soirée {nom}.")
        return saluer(nom)
    else:
        print("Bonne nuit {nom}.")
        return saluer(nom)

print(saluer(nom))