'''
Instructions du TP

Créez une fonction calculer_prix_ttc qui :
Prend en paramètre un prix HT et un taux de TVA (par défaut 20%)
Calcule et retourne le prix TTC
Arrondit le résultat à 2 décimales
'''

# TVA 20% correspond à multiplier le prix par 0.2 environ

prix_ht = float(input("Entrez le prix :"))

def calculer_ttc(prix_ht):
    tva_ajoutee = prix_ht*0.2
    prix_ttc = prix_ht + tva_ajoutee
    return prix_ttc

print (f"Le prix comprenant la TVA s'élève à: {round(calculer_ttc(prix_ht), 2)} €")