import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load Polymer Genome dataset
with open("pgnome.json", "r") as f:
    dataset = json.load(f)

records = []
for entry in dataset[:10]:  # limit to first 10 for demo
    diel = entry.get("diel_tot")
    gap = entry.get("hse_gap")
    coords = np.array(entry["atoms"]["coords"], dtype=float)
    elements = entry["atoms"]["elements"]

    # Save each atom coordinate
    for i, (x, y, z) in enumerate(coords):
        records.append({
            "polymer_id": entry.get("id"),
            "element": elements[i],
            "x": x,
            "y": y,
            "z": z,
            "diel_tot": float(diel) if diel else None,
            "hse_gap": float(gap) if gap else None
        })

# Save to CSV
df = pd.DataFrame(records)
df.to_csv("polymer_coordinates.csv", index=False)
print("Saved polymer_coordinates.csv")

# Plot x-y projection of first polymer
first_polymer = df[df["polymer_id"] == df["polymer_id"].unique()[0]]
plt.figure(figsize=(6,6))
plt.scatter(first_polymer["x"], first_polymer["y"], s=200,
            c="skyblue", edgecolors="k")
for i, row in first_polymer.iterrows():
    plt.text(row["x"], row["y"], row["element"], fontsize=8)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Polymer Structure Projection (x-y plane)")
plt.savefig("polymer_structure_xy.png", dpi=1200)
plt.close()
