'''
Instructions du TP

Créez une fonction calculer_prix_ttc qui :
Prend en paramètre un prix HT et un taux de TVA (par défaut 20%)
Calcule et retourne le prix TTC
Arrondit le résultat à 2 décimales
'''

# TVA 20% correspond à multiplier le prix par 0.2 environ

try:
    prix_ht = float(input("Entrez le prix :"))
    erreur = False
except ValueError:
    erreur = True
    print("Vous devez entrer un nombre, entier ou décimal.")
except TypeError:
    erreur = True

def calculer_ttc(prix_ht):
    tva_ajoutee = prix_ht*0.2
    prix_ttc = prix_ht + tva_ajoutee
    return prix_ttc

if erreur:
    print("Arrêt du calcul.")
elif prix_ht <=0:
    print("Arrêt du calcul. Veuillez entrer un nombre positif.")
else:
    print (f"Le prix comprenant la TVA s'élève à: {round(calculer_ttc(prix_ht), 2)} €") # Fonction round(calculer_ttc), 2) permet de limiter les décimales à 2