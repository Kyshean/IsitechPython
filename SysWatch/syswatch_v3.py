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
import argparse
from datetime import datetime

import collector
from traitement import calculer_moyennes, detecter_pics


def _bytes_to_gb(b):
    try:
        return float(b) / (1024 ** 3)
    except Exception:
        return 0.0


def exporter_csv(metriques, fichier):
    """Exporte les métriques essentielles dans un CSV (append si existe)."""
    headers = ['timestamp', 'hostname', 'cpu_percent', 'mem_total_gb', 'mem_dispo_gb', 'mem_percent', 'disk_root_percent']
    # s'assurer que le dossier d'export existe
    dirpath = os.path.dirname(fichier)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    exists = os.path.exists(fichier)
    row = {}
    row['timestamp'] = metriques.get('timestamp')
    sys = metriques.get('systeme', {})
    row['hostname'] = sys.get('hostname')
    cpu = metriques.get('cpu', {})
    row['cpu_percent'] = cpu.get('utilisation')
    mem = metriques.get('memoire', {})
    row['mem_total_gb'] = f"{_bytes_to_gb(mem.get('total', 0)):.2f}"
    row['mem_dispo_gb'] = f"{_bytes_to_gb(mem.get('disponible', 0)):.2f}"
    row['mem_percent'] = mem.get('pourcentage')
    # chercher partition root '/'
    disk_percent = None
    for d in metriques.get('disques', []):
        if d.get('point_montage') == '/':
            disk_percent = d.get('pourcentage')
            break
    if disk_percent is None and metriques.get('disques'):
        disk_percent = metriques.get('disques')[0].get('pourcentage')
    row['disk_root_percent'] = disk_percent

    with open(fichier, 'a', newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=headers)
        if not exists:
            writer.writeheader()
        writer.writerow(row)


def exporter_json(metriques, fichier):
    """Sauvegarde les métriques complètes en JSON lisible."""
    dirpath = os.path.dirname(fichier)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    with open(fichier, 'w') as fh:
        json.dump(metriques, fh, indent=2)


def afficher_resume(metriques):
    sys = metriques.get('systeme', {})
    cpu = metriques.get('cpu', {})
    mem = metriques.get('memoire', {})
    print(f"Relevé: {metriques.get('timestamp')}")
    print(f"Host: {sys.get('hostname')} - OS: {sys.get('os')}")
    print(f"CPU: {cpu.get('utilisation')}%")
    print(f"RAM: { _bytes_to_gb(mem.get('total',0)):.2f} Go total, {mem.get('pourcentage')}% utilisé")


def collecter_en_continu(intervalle=5, nombre=0, fichier_csv='./Syswatch/Exports/syswatch_history.csv'):
    """Collecte en continu les métriques, les affiche et les sauvegarde en CSV.

    nombre=0 -> infini
    """
    compteur = 0
    try:
        while True:
            met = collector.collecter_tout()
            afficher_resume(met)
            exporter_csv(met, fichier_csv)
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
    parser = argparse.ArgumentParser(description='SysWatch v3 - export & collecte continue')
    parser.add_argument('--continu', action='store_true', help='Lancer la collecte continue')
    parser.add_argument('--intervalle', type=int, default=5, help='Intervalle en secondes')
    parser.add_argument('--nombre', type=int, default=0, help='Nombre de collectes (0 = infini)')
    parser.add_argument('--stats', action='store_true', help='Afficher statistiques depuis le CSV')
    parser.add_argument('--csv', default='./SysWatch/Exports/sysWatch_history.csv', help='Fichier CSV d\'historique')
    parser.add_argument('--json', default='./SysWatch/Exports/last_metrics.json', help='Fichier JSON de sortie pour la collecte unique')
    args = parser.parse_args()

    # générer un horodatage pour les noms de fichiers par défaut
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')

    # si l'utilisateur utilise le nom par défaut, horodater le fichier
    csv_default_name = './SysWatch/Exports/syswatch_history.csv'
    json_default_name = './SysWatch/Exports/last_metrics.json'

    csv_file = args.csv
    json_file = args.json
    if csv_file.endswith(os.path.basename(csv_default_name)):
        csv_file = csv_file.replace('.csv', f'_{ts}.csv')
    if json_file.endswith(os.path.basename(json_default_name)):
        json_file = json_file.replace('.json', f'_{ts}.json')

    if args.stats:
        stats = calculer_stats(args.csv)
        if stats is None:
            print('Fichier CSV introuvable ou vide:', args.csv)
            return
        print('Statistiques CPU:', stats.get('cpu'))
        print('Statistiques mémoire (%):', stats.get('mem_percent'))
        pics = detecter_pics_csv(args.csv)
        print(f'Pics détectés: {len(pics)}')
        return

    if args.continu:
        collecter_en_continu(intervalle=args.intervalle, nombre=args.nombre, fichier_csv=csv_file)
        return

    # collecte unique
    met = collector.collecter_tout()
    afficher_resume(met)
    exporter_csv(met, csv_file)
    exporter_json(met, json_file)


if __name__ == '__main__':
    main()
