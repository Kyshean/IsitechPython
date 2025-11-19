"""Module `collector` — collecte des métriques système.
"""
from datetime import datetime
import platform
import socket
import psutil


def collecter_info_systeme():
	"""Retourne des informations système (pas de variables globales).

	Clés retournées:
	- 'os'
	- 'architecture'
	- 'hostname'
	- 'ip'
	"""
	host_info = platform.uname()
	try:
		host_ip = socket.gethostbyname(host_info.node)
	except Exception:
		host_ip = None
	version_token = host_info.version.split()[0] if host_info.version else ""
	os_string = f"{host_info.system} {version_token}".strip()
	return {
		'os': os_string,
		'architecture': platform.machine(),
		'hostname': host_info.node,
		'ip': host_ip,
	}


def collecter_cpu():
	"""Retourne les métriques CPU.

	Clés retournées:
	- 'coeurs_physiques'
	- 'coeurs_logiques'
	- 'utilisation'
	"""
	return {
		'coeurs_physiques': psutil.cpu_count(logical=False),
		'coeurs_logiques': psutil.cpu_count(),
		'utilisation': psutil.cpu_percent(interval=1),
	}


def collecter_memoire():
	"""Retourne les informations mémoire.

	Clés retournées:
	- 'total' (octets)
	- 'disponible' (octets)
	- 'pourcentage' (utilisation en %)
	"""
	host_virtual_memory = psutil.virtual_memory()
	return {
		'total': host_virtual_memory.total,
		'disponible': host_virtual_memory.available,
		'pourcentage': host_virtual_memory.percent,
	}


def collecter_disques():
	"""Retourne une liste de partitions et leurs métriques.

	Chaque élément est un dict contenant:
	- 'point_montage'
	- 'total' (octets)
	- 'utilise' (octets)
	- 'pourcentage'

	Les partitions inaccessibles sont ignorées (PermissionError).
	"""
	partitions = []
	for partition in psutil.disk_partitions():
		try:
			usage = psutil.disk_usage(partition.mountpoint)
		except PermissionError:
			continue
		partitions.append({
			'point_montage': partition.mountpoint,
			'total': usage.total,
			'utilise': usage.used,
			'pourcentage': usage.percent,
		})
	return partitions


def collecter_tout():
	"""Agrège toutes les informations collectées et ajoute un timestamp.

	Structure retournée:
	{
		'timestamp': ISO timestamp,
		'systeme': {...},
		'cpu': {...},
		'memoire': {...},
		'disques': [...],
	}
	"""
	return {
		'timestamp': datetime.now().isoformat(),
		'systeme': collecter_info_systeme(),
		'cpu': collecter_cpu(),
		'memoire': collecter_memoire(),
		'disques': collecter_disques(),
	}