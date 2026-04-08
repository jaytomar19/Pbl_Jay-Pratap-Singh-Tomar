from host import Host
from algorithms import first_fit, best_fit, energy_aware
from planetlab_loader import load_planetlab_data
import matplotlib.pyplot as plt


# Run one simulation
def run_once(algorithm):
    hosts = [Host(70)]

    vms = load_planetlab_data("planetlab_data", max_vms=120)

    algorithm(vms, hosts)

    total_power = sum(host.power() for host in hosts)

    return len(hosts), total_power


# Run multiple simulations
def run_experiment(algorithm, runs=10):
    host_results = []
    power_results = []

    for _ in range(runs):
        hosts, power = run_once(algorithm)
        host_results.append(hosts)
        power_results.append(power)

    avg_hosts = sum(host_results) / len(host_results)
    avg_power = sum(power_results) / len(power_results)

    return avg_hosts, avg_power


sample_vms = load_planetlab_data("planetlab_data", max_vms=120)
print("VMs Loaded:", len(sample_vms))


# Run experiments
ff_hosts, ff_power = run_experiment(first_fit)
bf_hosts, bf_power = run_experiment(best_fit)
ea_hosts, ea_power = run_experiment(energy_aware)


# Print results
print("\n--- Results (PlanetLab Dataset) ---")
print("First Fit -> Hosts:", ff_hosts, "Power:", ff_power)
print("Best Fit -> Hosts:", bf_hosts, "Power:", bf_power)
print("Energy Aware -> Hosts:", ea_hosts, "Power:", ea_power)


# Graphs
algorithms = ["First Fit", "Best Fit", "Energy Aware"]
host_values = [ff_hosts, bf_hosts, ea_hosts]
power_values = [ff_power, bf_power, ea_power]

# Hosts graph
plt.figure()
plt.bar(algorithms, host_values)
plt.xlabel("Algorithm")
plt.ylabel("Average Hosts Used")
plt.title("Hosts Comparison (PlanetLab Dataset)")

# Power graph
plt.figure()
plt.bar(algorithms, power_values)
plt.xlabel("Algorithm")
plt.ylabel("Average Power Consumption")
plt.title("Power Comparison (PlanetLab Dataset)")

plt.show()