from host import Host


# -------- FIRST FIT --------
def first_fit(vms, hosts):
    for vm in vms:
        placed = False

        for host in hosts:
            if host.can_allocate(vm):
                host.allocate(vm)
                placed = True
                break

        if not placed:
            new_host = Host(70)
            new_host.allocate(vm)
            hosts.append(new_host)


# -------- BEST FIT --------
def best_fit(vms, hosts):
    for vm in vms:
        best_host = None
        min_space_left = float('inf')

        for host in hosts:
            if host.can_allocate(vm):
                space_left = host.cpu_capacity - (host.used_cpu + vm.cpu)

                if space_left < min_space_left:
                    min_space_left = space_left
                    best_host = host

        if best_host is not None:
            best_host.allocate(vm)
        else:
            new_host = Host(70)
            new_host.allocate(vm)
            hosts.append(new_host)


# ENERGY AWARE 
def energy_aware(vms, hosts):
    for vm in vms:
        best_host = None
        best_score = -1  # we want highest utilization after placement

        for host in hosts:
            if host.can_allocate(vm):
                new_util = (host.used_cpu + vm.cpu) / host.cpu_capacity

                # Prefer hosts that are already ON and will become highly utilized
                score = new_util

                if score > best_score:
                    best_score = score
                    best_host = host

        if best_host is not None:
            best_host.allocate(vm)
        else:
            # Only create new host if absolutely necessary
            new_host = Host(70)
            new_host.allocate(vm)
            hosts.append(new_host)