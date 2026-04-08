import os
import random
from vm import VM

def load_planetlab_data(folder_path, max_vms=140):
    vms = []
    all_files = []

    # Collect all files from subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            all_files.append(os.path.join(root, file))

    # Sort for consistency and limit number of VMs
    all_files = sorted(all_files)[:max_vms]

    for file_path in all_files:
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()

                values = []
                for line in lines:
                    line = line.strip()
                    if line.isdigit():
                        values.append(int(line))

                if not values:
                    continue

                avg_util = sum(values) / len(values)

                # Convert % → CPU units (0–100 range for stronger effect)
                cpu_units = int((avg_util / 100) * 100)

                # Add controlled variation (IMPORTANT)
                cpu_units += random.randint(-35, 35)

                # Ensure valid value
                cpu_units = max(cpu_units, 1)

                vms.append(VM(cpu_units))

        except:
            continue

    return vms