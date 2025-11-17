''' 
TP Informations système

Créer un script permettant d'afficher les informations système de base telles que le nom de l'hôte, l'adresse IP, le système d'exploitation et la version de Python installée.
'''

import os
import platform
import socket
import sys

host_architecture = platform.machine()
host_info = platform.uname()
host_ip = socket.gethostbyname(host_info.node)

machine = {host_architecture, host_info.node, host_info.machine, host_info.processor, host_info.system, host_ip}

for i in machine:
    print(i)