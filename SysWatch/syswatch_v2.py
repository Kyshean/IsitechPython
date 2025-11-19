"""Affichage des métriques système recueillies par `collector`.
"""
from datetime import datetime
import collector

def octets_vers_go(octets):
    """Conversion d'Octets vers les Go

    Args:
        octets (float): nombre d'octets 

    Returns:
        float: chaîne formatée en Go
    """
    try:
        Go = float(octets) / (1024 ** 3)
    except Exception:
        Go = 0.0
    return f"{Go:.2f} Go"


def afficher_systeme(data):
    """Affiche les informations système (dictionnaire retourné par collector)."""
    systeme_data = data
    print("="*25+" Système "+"="*25)
    print(f"OS: {systeme_data.get('os')}")
    print(f"Architecture: {systeme_data.get('architecture')}")
    print(f"Hostname: {systeme_data.get('hostname')}")


def afficher_cpu(data):
    """Affiche les informations CPU (dictionnaire retourné par collector)."""
    print("="*25+" CPU "+"="*25)
    print(f"Coeurs physiques: {data.get('coeurs_physiques')}")
    print(f"Coeurs logiques: {data.get('coeurs_logiques')}")
    print(f"Utilisation: {data.get('utilisation')} %")


def afficher_memoire(data):
    """Affiche les informations mémoire (dictionnaire retourné par collector)."""
    print("="*25+" Mémoire "+"="*25)
    print(f"Total: {octets_vers_go(data.get('total'))}")
    print(f"Disponible: {octets_vers_go(data.get('disponible'))}")
    print(f"Utilisation: {data.get('pourcentage')} %")


def afficher_disques(disques):
    """Affiche la liste des partitions (liste de dicts retournée par collector)."""
    print("="*25+" Disques "+"="*25)
    if not disques:
        print("Aucune partition accessible trouvée.")
        return
    for disque in disques:
        print(f"Point de montage: {disque.get('point_montage')}")
        print(f"  Total: {octets_vers_go(disque.get('total'))}")
        print(f"  Utilisé: {octets_vers_go(disque.get('utilise'))}")
        print(f"  Pourcentage: {disque.get('pourcentage')} %")

def display_processor_info(data_cpu=None):
    """Affiche les informations processeur.

    """
    if data_cpu is None:
        data_cpu = collector.collecter_cpu()
    afficher_cpu(data_cpu)


def display_system_info(data_system=None):
    """Affiche les informations système.    
    """
    
    if data_system is None:
        data_system = collector.collecter_info_systeme()
    afficher_systeme(data_system)


def display_ram_info(data_memoire=None):
    """Affiche les informations mémoire.
    """
    
    if data_memoire is None:
        data_memoire = collector.collecter_memoire()
    afficher_memoire(data_memoire)


def display_disk_info(disques=None):
    """Affiche les informations sur les disques/partitions.
    """

    if disques is None:
        disques = collector.collecter_disques()
    afficher_disques(disques)


def display_header(timestamp):
    print(f"Relevé: {timestamp}")


def main():
    data = collector.collecter_tout()
    display_header(data.get('timestamp'))
    display_system_info(data.get('systeme', {}))
    display_processor_info(data.get('cpu', {}))
    display_ram_info(data.get('memoire', {}))
    display_disk_info(data.get('disques', []))


if __name__ == '__main__':
    main()
