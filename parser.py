# parser.py
import re
from ase import Atoms

def parse_structure(text: str):
    """
    Parse generator output into ASE Atoms object.
    """
    # Extract lattice constants
    a_match = re.search(r"a=([\d\.]+)", text)
    b_match = re.search(r"b=([\d\.]+)", text)
    c_match = re.search(r"c=([\d\.]+)", text)  # optional
    a = float(a_match.group(1)) if a_match else 3.0
    b = float(b_match.group(1)) if b_match else 3.0
    c = float(c_match.group(1)) if c_match else 6.0  # default for layered

    # Extract atomic coordinates
    atoms = []
    coords = []
    for line in text.splitlines():
        if ":" in line:
            atom, values = line.split(":")
            atom = atom.strip()
            matches = re.findall(r"\(([\d\.]+),([\d\.]+),([\d\.]+)\)", values)
            for m in matches:
                x, y, z = map(float, m)
                atoms.append(atom)
                coords.append([x, y, z])

    # Build ASE Atoms object
    structure = Atoms(symbols=atoms, positions=coords, cell=[a, b, c], pbc=True)
    return structure
