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


	def __str__():
 		return "timestamp: " + timestamp + " , " + "hostname: " + hostname + " , " + "cpu_percent: " + cpu_percent + " , " + "memory_total: " + memory_total + " , " + "memory_available: " + memory_available + " , " + "memory_percent: " + memory_percent + " , " + "disk_usage: " + disk_usage
