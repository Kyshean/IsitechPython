import collector
from datetime import datetime

class SystemMetrics:
    def __init__(self, timestamp, hostname, cpu_percent, memory_total, memory_available, memory_percent, disk_usage):
        self.timestamp = timestamp
        self.hostname = hostname
        self.cpu_percent = cpu_percent
        self.memory_total = memory_total
        self.memory_available = memory_available
        self.memory_percent = memory_percent
        self.disk_usage = disk_usage

    def get_timestamp(self):
        return self.timestamp

    def get_hostname(self):
        return self.hostname

    def get_cpu_percent(self):
        return self.cpu_percent

    def get_memory_total(self):
        return self.memory_total

    def get_memory_available(self):
        return self.memory_available

    def get_memory_percent(self):
        return self.memory_percent

    def get_disk_usage(self):
        return self.disk_usage

    def __str__(self):
        return (
            f"timestamp: {self.timestamp}\n"
            f"hostname: {self.hostname}\n"
            f"cpu_percent: {self.cpu_percent}\n"
            f"memory_total: {self.memory_total}\n"
            f"memory_available: {self.memory_available}\n"
            f"memory_percent: {self.memory_percent}\n"
            f"disk_usage: {self.disk_usage}"
        )

# Récupère les valeurs spécifiques depuis les dictionnaires du module collector
system_info = collector.collecter_info_systeme()
hostname = system_info['hostname']

cpu_info = collector.collecter_cpu()
cpu_percent = cpu_info['utilisation']

mem_total = collector.collecter_memoire()['total']
mem_available = collector.collecter_memoire()['disponible']
mem_percent = collector.collecter_memoire()['pourcentage']

disk_info = []
disk_in_use = collector.collecter_disques()
for disk in disk_in_use:
    disk_info.append(disk["utilise"] / 1024 ** 3)
disk_info = [round(x, 2) for x in disk_info]



# Instanciation de l'objet Pouet selon la classe SystemMetrics avec les valeurs extraites
host_measured = SystemMetrics(
    timestamp=datetime.now(),
    hostname=hostname,
    cpu_percent=cpu_percent,
    memory_total=mem_total,
    memory_available=mem_available,
    memory_percent=mem_percent,
    disk_usage=disk_info
)

print(host_measured)
