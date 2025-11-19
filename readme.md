# Repository SysWatch & TP

Ce repository contient quelques exercices réalisés en Python qui vont être détaillés.

## SystemInfo.py

    Fichier en python permettant la collecte et l'affichage d'informations système basique. 
    Résultats en CLI.

## CalculPrix.py

    Ce fichier contient une fonction simple permettant d'ajouter la TVA a un prix donné, le taux est arbitrairement fixé à 20%

## FonctionSalutation.py

    Fichier contenant une boucle if simpliste, récupérant l'heure actuelle du système afin de saluer l'utilisateur, selon l'heure.

## ValidPassword

    Fichier python qui, une fois lancé, permet de vérifier la validité basique d'un mot de passe.
    Le mot de passe est entré en clair cependant, attention.
Le mot de passe est considéré valide si :
1. Il contient au moins 8 caractères
2. Il contient au moins 1 minuscule
3. Il contient au moins 1 majuscule
4. Il contient au moins 1 caractère spécial

## Syswatch

Le gros du projet. 
Contient 3 versions du script, ainsi que les modules **traitement** et **collector**. Collector ne fait que collecter les données tandis que Traitement ne fait qu'analyser les données récupérées.

### Syswatch_v1.py
    Premier exemple du script, exécution basique et output dans le terminal.

### Syswatch_v2.py
    Deuxième script, utilise le module collector pour output le résultat dans le terminal.

### Syswatch_v3.py
    Troisième script, utilisant les modules collector et traitement pour output le résultat dans le terminal ainsi que dans un répertoire nommé "Exports".

__Utilisation__ : ```python
python ./SysWatch/syswatch_v3.py --Options
 ```

__Options disponibles__ : 
    1. *--continu* : Effectue un scan en continu.
    2. *--stats* : Fais des moyennes en fonction des fichiers CSV et JSON précédemments exécutés 
    3. *--intervalle* : Spécifie l'intervalle entre deux instantanés des informations
    4. *--nombre* : Spécifie le nombre de fois ou ce scan sera exécuté
    5. *--csv* : Spécifie le format par défaut de l'output. (DEFAULT VALUE)
    6. *--json* : Spécifie le format de sortie par défaut.