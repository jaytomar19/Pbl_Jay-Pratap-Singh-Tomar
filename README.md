# Energy-Aware Cloud Resource Simulator
 Overview

This project implements a simulation framework for **virtual machine (VM) allocation in cloud data centers** with a focus on **energy efficiency**.
It compares multiple allocation strategies and evaluates their impact on **host utilization and power consumption** using real-world workload trac
 Objectives

* Simulate VM allocation in a cloud environment
* Compare different allocation heuristics
* Analyze energy consumption behavior
* Demonstrate effectiveness of an energy-aware strategy

## Algorithms Implemented

### 1. First Fit

* Allocates each VM to the first host with sufficient capacity
* Fast but may lead to inefficient packing

### 2. Best Fit

* Allocates VM to the host with least remaining capacity after placement
* Attempts tighter packing

### 3. Energy-Aware (Proposed)

* Selects host that **maximizes utilization after allocation**
* Minimizes number of active hosts
* Reduces overall power consumptiom

## Energy Model

Each host follows a linear power model:

* Idle host → **0 power (OFF)**
* Active host →
  `Power = Base + (Max - Base) × Utilization`

Where:

* Base Power = 100
* Max Power = 200

This reflects real-world server behavior.

---

## Dataset

The simulator uses workload traces from:

* PlanetLab VM traces (March–April 2011)

### Processing:

* CPU utilization values are averaged per VM
* Converted into CPU demand units
* Controlled variability added to simulate real-world fluctuations

---

## Features

* Real dataset integration
* Multiple algorithm comparison
* Energy-aware scheduling strategy
* Visualization using bar graphs
* Optional Streamlit-based UI

---

## Project Structure

```
cloud_sim/
│
├── main.py                  # Simulation runner
├── host.py                  # Host model + power calculation
├── vm.py                    # VM model
├── algorithms.py            # Allocation algorithms
├── planetlab_loader.py      # Dataset loader
├── app.py                   # Streamlit UI (optional)
├── planetlab_data/          # Dataset folder (sample included)
```

---

## How to Run

### 1. Clone repository

```
git clone <your-repo-link>
cd cloud_sim
```

### 2. Install dependencies

```
pip install matplotlib streamlit
```

### 3. Run simulation

```
python main.py
```

### 4. Run UI (optional)

```
python -m streamlit run app.py
```

---

## Results

The simulator compares:

* Average number of hosts used
* Average power consumption

### Key Observation

Under constrained resources and variable workloads:

* The **energy-aware algorithm reduces power consumption**
* Achieved through better consolidation of VMs

---

## Conclusion

The project demonstrates that:

* VM placement significantly impacts energy efficiency
* Consolidation-based strategies reduce active hosts
* Energy-aware scheduling improves overall system efficiency

---

## Future Work

* VM migration and dynamic workloads
* Time-based simulation
* Integration with real cloud frameworks
* Advanced energy models

---

## Author

Jay Pratap Singh Tomar
