class Host:
    def __init__(self, cpu_capacity):
        self.cpu_capacity = cpu_capacity
        self.used_cpu = 0
        self.vms = []

    def can_allocate(self, vm):
        return self.used_cpu + vm.cpu <= self.cpu_capacity

    def allocate(self, vm):
        self.vms.append(vm)
        self.used_cpu += vm.cpu

    def utilization(self):
        if self.cpu_capacity == 0:
            return 0
        return self.used_cpu / self.cpu_capacity

    def power(self):
        # If no VM → host is OFF
        if self.used_cpu == 0:
            return 0

        base_power = 100
        max_power = 200

        return base_power + (max_power - base_power) * self.utilization()

    def __repr__(self):
        return f"Host(used={self.used_cpu}/{self.cpu_capacity})"