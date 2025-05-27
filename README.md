
# 📊 Plot Energy vs Time

This Python script processes energy values from a VASP `OSZICAR` file and plots energy as a function of time. It is useful for analyzing molecular dynamics simulations by extracting clean energy trends over time, while filtering out unphysical noise.

---

## 🔧 Features

- Parses VASP `OSZICAR` files
- User-defined time step (in femtoseconds)
- Automatically skips the first 3 picoseconds (equilibration)
- Analyzes energy between 3 ps and 10 ps
- Filters out 4 highest unphysical energy spikes
- Plots and saves a high-quality energy vs time curve
- Command-line interface with flexible arguments

---

## 📦 Requirements

Make sure you have the following Python packages:

- Python 3.x
- `numpy`
- `matplotlib`

You can install the dependencies using pip:

```bash
pip install numpy matplotlib
```

---

## 🚀 Usage

```bash
python plot_oszicar.py --dt <time_step_fs> [--file <OSZICAR_file>] [--out <output_image>]
```

### Required argument:

- `--dt`: Time step in **femtoseconds** (e.g., `--dt 2` for a 2 fs timestep)

### Optional arguments:

- `--file`: Path to the `OSZICAR` file (default: `OSZICAR`)
- `--out`: Output image filename (default: `energy_vs_time.png`)

---

## 📁 Examples

```bash
# Basic usage with 2 fs timestep
python plot_oszicar.py --dt 2

# Using a custom OSZICAR file and output image name
python plot_oszicar.py --dt 1.5 --file my_OSZICAR --out my_plot.png
```

This will:
- Ignore the first 3 ps (e.g. 1500 steps if dt = 2 fs)
- Extract and filter energy data between 3 ps and 10 ps
- Remove 4 extreme outliers in energy values
- Plot and save the filtered curve

---

## 🧪 Notes

- The script looks for lines containing `"E="` in the OSZICAR file to extract energy values.
- If you want to analyze a different time window or change the outlier filtering strategy, you can modify the script.


---

## 🤝 Contributing

Pull requests are welcome! If you find a bug or have an idea for improvement, feel free to open an issue or PR.
