import csv
import random
import matplotlib.pyplot as plt
import pandas as pd

# -------------------------------
# 1. Generate Synthetic Candidates
# -------------------------------
candidates = []
for i in range(1, 101):  # 100 candidates
    diel = round(random.uniform(2.0, 12.0), 2)   # dielectric constant
    gap = round(random.uniform(0.5, 5.0), 2)    # band gap
    candidates.append({
        "id": f"Polymer_{i:03d}",
        "label": f"Hypothetical_Polymer_{i:03d}",
        "diel_tot": diel,
        "hse_gap": gap
    })

# -------------------------------
# 2. Save to CSV
# -------------------------------
with open("new_candidates.csv", "w", newline="") as csvfile:
    fieldnames = ["id", "label", "diel_tot", "hse_gap"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for c in candidates:
        writer.writerow(c)

print("Synthetic candidates saved to new_candidates.csv")

# -------------------------------
# 3. Load DataFrame for Plotting
# -------------------------------
df = pd.DataFrame(candidates)

# -------------------------------
# 4. Scatter Plot (Dielectric vs Band Gap)
# -------------------------------
plt.figure(figsize=(7,6))
plt.scatter(df["hse_gap"], df["diel_tot"], c="blue", alpha=0.7, edgecolors="k")
plt.xlabel("Band Gap (eV)")
plt.ylabel("Dielectric Constant")
plt.title("Synthetic Polymer Candidates")
plt.grid(True)
plt.savefig("scatter_candidates.png", dpi=1200)
plt.close()

# -------------------------------
# 5. Histogram of Dielectric Constants
# -------------------------------
plt.figure(figsize=(7,6))
plt.hist(df["diel_tot"], bins=15, color="green", edgecolor="black", alpha=0.7)
plt.xlabel("Dielectric Constant")
plt.ylabel("Frequency")
plt.title("Distribution of Dielectric Constants")
plt.savefig("hist_dielectric.png", dpi=1200)
plt.close()

# -------------------------------
# 6. Histogram of Band Gaps
# -------------------------------
plt.figure(figsize=(7,6))
plt.hist(df["hse_gap"], bins=15, color="orange", edgecolor="black", alpha=0.7)
plt.xlabel("Band Gap (eV)")
plt.ylabel("Frequency")
plt.title("Distribution of Band Gaps")
plt.savefig("hist_bandgap.png", dpi=1200)
plt.close()

print("Figures saved: scatter_candidates.png, hist_dielectric.png, hist_bandgap.png (all 1200 dpi)")
