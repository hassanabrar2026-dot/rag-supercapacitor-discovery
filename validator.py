from parser import parse_structure
from alignn.models.alignn import ALIGNN
from alignn.utils import get_prediction

def validate_candidate(candidate: str):
    """
    Validate candidate using ALIGNN property prediction.
    """
    structure = parse_structure(candidate)

    # Save to CIF for ALIGNN
    structure.write("candidate.cif")

    # Load pretrained ALIGNN model
    model = ALIGNN.load_pretrained("jarvis_alignn_torch")

    # Predict properties
    prediction = get_prediction(model, "candidate.cif")

    return {
        "candidate": candidate,
        "predicted_Tc": prediction.get("Tc", None),
        "formation_energy": prediction.get("formation_energy", None),
        "stability": "Stable" if prediction.get("Ehull", 1.0) < 0.3 else "Unstable"
    }
