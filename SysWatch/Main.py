import platform
import socket
import psutil

host_cpu_usage = psutil.cpu_percent(interval=1)
host_architecture = platform.machine()
host_info = platform.uname()
host_ip = socket.gethostbyname(host_info.node)
host_system = platform.system()
host_python = platform.python_version()

print(f"Nom du poste : {host_info.node}")
print("="*25+" CPU "+"="*25)
print(f"Le taux d'utilisation du processeur est {host_cpu_usage}%")
print(f"Ce poste dispose d'un système d'exploitation {host_info.system}")
print(f"L'architecture est la suivante {host_info.machine}")
print(f"La version de python est la suivante {host_python}")