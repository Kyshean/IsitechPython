'''
Créez une fonction est_mot_de_passe_valide qui :
Prend un mot de passe en paramètre
Retourne True si le mot de passe :
Fait au moins 8 caractères
Contient au moins un chiffre
Contient au moins une lettre majuscule
Retourne False sinon
'''

import re

def mot_de_passe_valide(password):
    """Vérifie l'entrée d'un mot de passe valide

    Args:
        password (str): mot de passe

    Returns:
        bool : mot de passe valide ou non.
    """
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[#&'(-_)=!:;,?./§%*µ$£¤^¨@`|{#~²}]).{8,}$"
    verification_password = bool(re.findall(pattern, password)) # Enregistrement dans un booléen de la vérification par RegEx
    return verification_password

# Exemple d'utilisation :
password = input("Veuillez entrer votre mot de passe : ")
if mot_de_passe_valide(password):
    print("Mot de passe valide !")
else:
    print("Mot de passe invalide.")
