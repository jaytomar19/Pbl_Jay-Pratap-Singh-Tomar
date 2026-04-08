import random
from vm import VM

def generate_vms(n):
    vms = []
    for _ in range(n):
        cpu = random.randint(5, 60)
        vms.append(VM(cpu))
    return vms