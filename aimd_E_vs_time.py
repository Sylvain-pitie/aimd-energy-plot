#!/usr/bin/env python3
import argparse
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Argument parser
parser = argparse.ArgumentParser(description="Plot energy vs. time from a VASP OSZICAR file.")
parser.add_argument("--dt", type=float, required=True, help="Time step in femtoseconds (e.g., 2)")
parser.add_argument("--file", type=str, default="OSZICAR", help="Path to OSZICAR file (default: OSZICAR)")
parser.add_argument("--out", type=str, default="energy_vs_time.png", help="Output image filename (default: energy_vs_time.png)")
args = parser.parse_args()

# ------------------------------------------------------------
# Parameters
time_step_fs = args.dt
time_step_ps = time_step_fs / 1000.0  # Convert fs to ps
input_file = args.file
output_file = args.out

# Time window to analyze
start_ps = 3.0
end_ps = 10.0

# ------------------------------------------------------------
# Read energies from OSZICAR
energies = []
with open(input_file, 'r') as f:
    for line in f:
        if "E=" in line:
            try:
                parts = line.split()
                e_index = parts.index("E=")
                energy = float(parts[e_index + 1])
                energies.append(energy)
            except (ValueError, IndexError):
                continue

# ------------------------------------------------------------
# Generate time vector
time = [i * time_step_ps for i in range(len(energies))]

# Select the time window [3 ps, 10 ps]
start_idx = int(start_ps / time_step_ps)
end_idx = int(end_ps / time_step_ps)

time_window = time[start_idx:end_idx]
energy_window = energies[start_idx:end_idx]

# ------------------------------------------------------------
# Remove the 4 highest peaks (likely noise)
for _ in range(4):
    if len(energy_window) == 0:
        break
    max_idx = np.argmax(energy_window)
    del energy_window[max_idx]
    del time_window[max_idx]

# ------------------------------------------------------------
# Plot
plt.figure(figsize=(8, 6))
plt.plot(time_window, energy_window, color='blue')
plt.xlabel("Time (ps)", fontsize=14)
plt.ylabel("Energy (eV)", fontsize=14)
plt.xlim([start_ps, end_ps])
#plt.title("Energy vs Time from OSZICAR (filtered)", fontsize=16)
plt.tight_layout()
plt.savefig(output_file, dpi=300)
