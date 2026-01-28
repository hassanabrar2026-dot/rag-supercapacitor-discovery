import matplotlib.pyplot as plt
from alignn.models.alignn import ALIGNN
from jarvis.db.figshare import data

def main():
    # 1. Load pretrained ALIGNN model
    print("Loading ALIGNN pretrained model...")
    model = ALIGNN.load_pretrained("jarvis_alignn_torch")

    # 2. Load superconductors dataset (replace with your own if needed)
    print("Loading JARVIS superconductors dataset...")
    dataset = data("jcse_expt")

    materials = []
    tc_values = []
    energies = []

    # 3. Run predictions
    print("Running predictions...")
    for entry in dataset[:50]:  # adjust slice for your dataset size
        mat_name = entry["formula"]
        structure = entry["structure"]
        formation_energy = entry.get("formation_energy", None)

        prediction = model(structure)  # ALIGNN prediction
        materials.append(mat_name)
        tc_values.append(prediction.item())
        energies.append(formation_energy)

    # 4a. Bar chart of Tc values
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(materials, tc_values, color='#1f77b4', edgecolor='black')

    ax.set_xlabel('Material', fontsize=12)
    ax.set_ylabel('Predicted Tc (K)', fontsize=12)
    ax.set_title('Predicted Superconducting Critical Temperatures (Tc)', fontsize=14)
    plt.xticks(rotation=90)

    plt.tight_layout()
    plt.savefig("predicted_tc_results.png", dpi=300)
    plt.close(fig)

    # 4b. Scatter plot Tc vs formation energy
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(energies, tc_values, c='red', alpha=0.7)
    ax.set_xlabel("Formation Energy (eV/atom)", fontsize=12)
    ax.set_ylabel("Predicted Tc (K)", fontsize=12)
    ax.set_title("Stability vs Superconducting Performance", fontsize=14)

    plt.tight_layout()
    plt.savefig("tc_vs_energy.png", dpi=300)
    plt.close(fig)

    print("Analysis complete. Figures saved as:")
    print(" - predicted_tc_results.png")
    print(" - tc_vs_energy.png")

if __name__ == "__main__":
    main()
