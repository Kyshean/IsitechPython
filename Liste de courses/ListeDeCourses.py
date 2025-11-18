"""
Créez un petit programme avec les fonctions suivantes :
afficher_liste(courses) : affiche tous les articles
ajouter_article(courses, article) : ajoute un article à la liste
retirer_article(courses, article) : retire un article de la liste
compter_articles(courses) : retourne le nombre d'articles

Ajoutez des feature permettant d'enregistrez le fichier dans un fichier texte pour la vérifier.
"""
with open("Liste de courses/Liste.txt") as courses:
    lignes = courses.readline()

def afficher_liste(courses):
    print("\nListe des courses :")
    if not courses:
        print("La liste est vide.")
    else:
        print (courses.read())

def ajouter_article(courses, article):
        with open("Liste de courses/Liste.txt", "a") as courses:
            courses.write(f"{article} \n")
        print(f"L'article '{article}' a été ajouté.")

def retirer_article(courses, article):
        with open("Liste de courses/Liste.txt", "w") as courses:
            article_trouve = False
            for ligne in lignes:
                if ligne.strip() != article:
                    courses.write(ligne)
                    article_trouve = True
                else:
                    break
        if article_trouve:
            print(f"l'article {article} a été retiré avec succès")
        else:
            print(f"Votre liste de courses ne comporte pas {article}")


def compter_articles(courses):
    return len(courses)

def menu():
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