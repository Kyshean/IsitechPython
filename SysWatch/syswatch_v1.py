import platform
import socket
import psutil

# Déclaration des variables
host_cpu_usage = psutil.cpu_percent(interval=1)
host_phys_heart = psutil.cpu_count(logical=False)
host_logic_heart = psutil.cpu_count()
host_architecture = platform.machine()
host_info = platform.uname()
host_ip = socket.gethostbyname(host_info.node)
host_system = platform.system()
host_python = platform.python_version()
host_ram = psutil.virtual_memory().total / (1024 **3)
free_ram = psutil.virtual_memory().percent
used_ram = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
disks = psutil.disk_partitions()

# Déclaration de l'affichage

def display_processor_info():
    """Affiche les informations du processeur dans la console
    """
    print(f"="*25+" Informations Processeur "+"="*25)
    print(f"\nLe taux d'utilisation du processeur est {host_cpu_usage}%")
    print(f"Le processeur dispose de {host_logic_heart} coeurs logiques")
    print(f"Le processeur dispose de {host_phys_heart} coeurs physique \n")

def display_system_info():
    """Affiche les informations du système dans la console
    """
    print(f"Nom du poste : {host_info.node} \n")
    print("="*25+" Informations Système "+"="*25)
    print(f"\n Ce poste dispose d'un système d'exploitation {host_info.system}")
    print(f"L'architecture est la suivante {host_info.machine}")
    print(f"La version de python est la suivante {host_python}\n")

def display_ram_info():
    """Affiche les informations de mémoire Vive dans la Console
    """
    print(f"="*25+" Informations Mémoire Vive "+"="*25)
    print(f"\nLe poste dispose de {round(host_ram, 1)}Go de mémoire Vive (RAM)")
    print(f"Le poste utilise présentement {round(used_ram, 1)}% de RAM")
    print(f"La mémoire Vive (RAM) libre est de {free_ram}%")

def display_disk_info():
    """Affiche les informations de chaque disque et chaque partition
    """
    for partition in disks:
        print(f"="*25+" Informations sur la partition "+"="*25)
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Point de montage: {partition.mountpoint}")
        print(f"  Type de système de fichiers: {partition.fstype}")
        print(f"  Taille totale: {round(partition_usage.total / (1024 **3), 2)} Go")
        print(f"  Espace utilisé: {round(partition_usage.used / (1024 **3), 2)} Go")
        print(f"  Espace libre: {round(partition_usage.free / (1024 **3), 2)} Go")
        print(f"  Pourcentage utilisé: {partition_usage.percent}%\n")

if __name__ == "__main__":
    display_system_info()
    display_processor_info()
    display_ram_info()
    display_disk_info()