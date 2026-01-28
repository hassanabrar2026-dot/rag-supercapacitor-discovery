# generator.py
from transformers import pipeline

# Load a text-generation model (can swap with Mistral, LLaMA, etc.)
generator = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.2")

def generate_candidate(context, query: str):
    """
    Generate a new candidate superconductor structure using RAG.
    """
    context_str = "\n".join([f"{m['formula']} (Tc={m['Tc']}K, {m['dimensionality']})" for m in context])
    prompt = f"""
    ### Instruction:
    Generate atomic structure description with lattice lengths, angles, coordinates, and atom types.

    ### Input:
    Retrieved examples:
    {context_str}
    Target: {query}

    ### Response:
    """
    result = generator(prompt, max_length=300, do_sample=True, temperature=0.7)
    return result[0]["generated_text"]
