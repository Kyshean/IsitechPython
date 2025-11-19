"""Module de traitement pour les métriques (statistiques et détection de pics).
"""
import csv


def calculer_moyennes(fichier_csv):
    """Lit un fichier CSV et calcule des statistiques basiques.

    Retourne un dict:
    {
        'cpu': {'moyenne': , 'min': , 'max': },
        'mem_percent': {'moyenne': , 'min': , 'max': }
    }
    """
    cpu_vals = []
    mem_vals = []
    try:
        with open(fichier_csv, newline='') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                try:
                    cpu_vals.append(float(row.get('cpu_percent', 0) or 0))
                except Exception:
                    pass
                try:
                    mem_vals.append(float(row.get('mem_percent', 0) or 0))
                except Exception:
                    pass
    except FileNotFoundError:
        return None

    def stats(values):
        if not values:
            return {'moyenne': None, 'min': None, 'max': None}
        return {'moyenne': sum(values) / len(values), 'min': min(values), 'max': max(values)}

    return {'cpu': stats(cpu_vals), 'mem_percent': stats(mem_vals)}


def detecter_pics(fichier_csv, seuil_cpu=80.0, seuil_mem=80.0):
    """Identifie lignes où CPU > seuil_cpu ou mem_percent > seuil_mem.

    Retourne une liste de dicts: {'timestamp':..., 'cpu_percent':..., 'mem_percent':...}
    """
    pics = []
    try:
        with open(fichier_csv, newline='') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                try:
                    cpu = float(row.get('cpu_percent', 0) or 0)
                except Exception:
                    cpu = 0.0
                try:
                    mem = float(row.get('mem_percent', 0) or 0)
                except Exception:
                    mem = 0.0
                if cpu > seuil_cpu or mem > seuil_mem:
                    pics.append({'timestamp': row.get('timestamp'), 'cpu_percent': cpu, 'mem_percent': mem})
    except FileNotFoundError:
        return []
    return pics
