"""Script d'export et collecte continue pour SysWatch.

Fonctions principales:
- exporter_csv(metriques, fichier)
- exporter_json(metriques, fichier)
- collecter_en_continu(intervalle, nombre, fichier_csv)

Utilise le module local `collector` pour récupérer les métriques.
"""
import csv
import json
import os
import time
import sys
from types import SimpleNamespace
import collector
from traitement import calculer_moyennes, detecter_pics


def octets_to_go(octet):
    try:
        return float(octet) / (1024 ** 3)
    except Exception:
        return 0.0


def exporter_csv(metriques, fichier):
    """Exporte les métriques essentielles dans un CSV (append si existe).
    """
    # Préparer dossier
    dossier_export = os.path.dirname(fichier)
    if dossier_export:
        os.makedirs(dossier_export, exist_ok=True)

    systeme_info = metriques.get('systeme', {})
    cpu_info = metriques.get('cpu', {})
    mem_info = metriques.get('memoire', {})

    ligne_csv = {
        'hostname': systeme_info.get('hostname'),
        'cpu_percent': cpu_info.get('utilisation'),
        'mem_total_gb': octets_to_go(mem_info.get('total', 0)),
        'mem_dispo_gb': octets_to_go(mem_info.get('disponible', 0)),
        'mem_percent': mem_info.get('pourcentage'),
    }

    # disk_root_percent : chercher '/' sinon None
    racine_pourcentage_disque = None
    for disque in metriques.get('disques', []):
        if disque.get('point_montage') == '/':
            racine_pourcentage_disque = disque.get('pourcentage')
            break
    if racine_pourcentage_disque is None and metriques.get('disques'):
        racine_pourcentage_disque = metriques.get('disques')[0].get('pourcentage')
    ligne_csv['disk_root_percent'] = racine_pourcentage_disque

    fichier_existe = os.path.exists(fichier)
    with open(fichier, 'a', newline='') as fichier_handle:
        writer = csv.DictWriter(fichier_handle, fieldnames=list(ligne_csv.keys()))
        if not fichier_existe:
            writer.writeheader()
        writer.writerow(ligne_csv)


def exporter_json(metriques, fichier):
    """Sauvegarde les métriques complètes en JSON lisible."""
    dossier_export = os.path.dirname(fichier)
    if dossier_export:
        os.makedirs(dossier_export, exist_ok=True)
    with open(fichier, 'w', encoding='utf-8') as fichier_handle:
        json.dump(metriques, fichier_handle, indent=2, ensure_ascii=False)


def afficher_resume(metriques):
    systeme_info = metriques.get('systeme', {})
    cpu_info = metriques.get('cpu', {})
    mem_info = metriques.get('memoire', {})
    print(f"Relevé: {metriques.get('timestamp')}")
    print(f"Host: {systeme_info.get('hostname')} - OS: {systeme_info.get('os')}")
    print(f"CPU: {cpu_info.get('utilisation')}%")
    print(f"RAM: { octets_to_go(mem_info.get('total',0)):.2f} Go total, {mem_info.get('pourcentage')}% utilisé")


def collecter_en_continu(intervalle=5, nombre=0, fichier_csv='./SysWatch/Exports/syswatch_history.csv'):
    """Collecte en continu les métriques, les affiche et les sauvegarde en CSV.

    nombre=0 -> infini
    """
    compteur = 0
    try:
        while True:
            metrics_collected = collector.collecter_tout()
            afficher_resume(metrics_collected)
            exporter_csv(metrics_collected, fichier_csv)
            compteur += 1
            if nombre and compteur >= nombre:
                break
            time.sleep(intervalle)
    except KeyboardInterrupt:
        print('\nArrêt par l\'utilisateur (Ctrl+C)')


def calculer_stats(fichier_csv):
    return calculer_moyennes(fichier_csv)


def detecter_pics_csv(fichier_csv, seuil_cpu=80.0, seuil_mem=80.0):
    return detecter_pics(fichier_csv, seuil_cpu=seuil_cpu, seuil_mem=seuil_mem)


def main():
    valeurs_defaut = {
        'continu': False,
        'intervalle': 5,
        'nombre': 0,
        'stats': False,
        'csv': './SysWatch/Exports/syswatch_history.csv',
        'json': './SysWatch/Exports/last_metrics.json',
    }

    def lire_arguments(liste_arguments):
        """Lit une liste d'arguments (ex: ['--continu','--intervalle','10'])
        et retourne un objet simple avec les valeurs.
        """
        valeurs = valeurs_defaut.copy()
        index = 0
        while index < len(liste_arguments):
            option = liste_arguments[index]
            if option == '--continu':
                valeurs['continu'] = True
                index += 1
            elif option == '--stats':
                valeurs['stats'] = True
                index += 1
            elif option == '--intervalle' and index + 1 < len(liste_arguments):
                try:
                    valeurs['intervalle'] = int(liste_arguments[index + 1])
                except Exception:
                    pass
                index += 2
            elif option == '--nombre' and index + 1 < len(liste_arguments):
                try:
                    valeurs['nombre'] = int(liste_arguments[index + 1])
                except Exception:
                    pass
                index += 2
            elif option == '--csv' and index + 1 < len(liste_arguments):
                valeurs['csv'] = liste_arguments[index + 1]
                index += 2
            elif option == '--json' and index + 1 < len(liste_arguments):
                valeurs['json'] = liste_arguments[index + 1]
                index += 2
            else:
                index += 1
        return SimpleNamespace(**valeurs)

    options = lire_arguments(sys.argv[1:])

# Nommage des fichiers par défaut
    csv_default_name = './SysWatch/Exports/syswatch_history.csv'
    json_default_name = './SysWatch/Exports/last_metrics.json'
    csv_file = options.csv
    json_file = options.json
    if csv_file.endswith(os.path.basename(csv_default_name)):
        csv_file = csv_file.replace('.csv', f'_{ts}.csv')
    if json_file.endswith(os.path.basename(json_default_name)):
        json_file = json_file.replace('.json', f'_{ts}.json')

    if options.stats:
        stats = calculer_stats(options.csv)
        if stats is None:
            print('Fichier CSV introuvable ou vide:', options.csv)
            return
        print('Statistiques CPU:', stats.get('cpu'))
        print('Statistiques mémoire (%):', stats.get('mem_percent'))
        pics = detecter_pics_csv(options.csv)
        print(f'Pics détectés: {len(pics)}')
        return

    if options.continu:
        collecter_en_continu(intervalle=options.intervalle, nombre=options.nombre, fichier_csv=csv_file)
        return

    # collecte unique
    metrics_collected = collector.collecter_tout()
    afficher_resume(metrics_collected)
    exporter_csv(metrics_collected, csv_file)
    exporter_json(metrics_collected, json_file)


if __name__ == '__main__':
    main()
