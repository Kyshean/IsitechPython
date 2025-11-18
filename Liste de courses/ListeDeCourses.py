"""
Créez un petit programme avec les fonctions suivantes :
afficher_liste(courses) : affiche tous les articles
ajouter_article(courses, article) : ajoute un article à la liste
retirer_article(courses, article) : retire un article de la liste
compter_articles(courses) : retourne le nombre d'articles

Ajoutez des feature permettant d'enregistrez le fichier dans un fichier texte pour la vérifier.
"""

def afficher_liste(courses):
    """Affiche l'entièreté de la liste de courses

    Args:
        courses (fichier): Correspond à la liste de courses
    """
    print("\nListe des courses :")
    with open("Liste de courses/Liste.txt") as courses:
        if not courses:
            print("La liste est vide.")
        else:
            print (courses.read())

def ajouter_article(courses, article):
    """
    Ajout d'un article à la liste de courses

    Args:
        courses (fichier): Contient la liste des articles
        article (str): article à ajouter
    """
    with open("Liste de courses/Liste.txt", "a") as courses:
            courses.write(f"{article} \n")
            print(f"L'article '{article}' a été ajouté.")

def retirer_article(courses, article):
    """Retrait d'un article de la liste de courses

    Args:
        courses (fichier): Liste des articles
        article (str): L'article à retirer
    """
    with open("Liste de courses/Liste.txt") as f:
        lignes = f.readlines()
    with open("Liste de courses/Liste.txt", "w") as f:
        article_trouve = False
        for ligne in lignes:
            if ligne.strip() != article:
                f.write(ligne)
            else:
                article_trouve = True
    if article_trouve:
        print(f"L'article '{article}' a été retiré avec succès.")
    else:
        print(f"Votre liste de courses ne comporte pas '{article}'.")


def compter_articles(courses):
    with open("Liste de courses/Liste.txt",) as f:
            lignes = f.readlines()
            return len([ligne for ligne in lignes if ligne.strip()])

def menu():
    """Définition basique d'un menu
    """
    courses = open("Liste de courses/Liste.txt")
    while True:
        print("\n--- Menu Liste de Courses ---")
        print("1. Afficher la liste")
        print("2. Ajouter un article")
        print("3. Retirer un article")
        print("4. Compter les articles")
        print("5. Quitter")

        choix = input("Choisissez une option (1-5) : ")

        if choix == "1":
            afficher_liste(courses)
        elif choix == "2":
            article = input("Entrez le nom de l'article à ajouter : ")
            ajouter_article(courses, article)
        elif choix == "3":
            article = input("Entrez le nom de l'article à retirer : ")
            retirer_article(courses, article)
        elif choix == "4":
            print(f"\nNombre d'articles dans la liste : {compter_articles(courses)}")
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Lancer le menu
if __name__ == "__main__":
    menu()