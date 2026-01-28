# 🔋 RAG-Supercapacitor-Discovery

> **Retrieval-Augmented Generation (RAG) pipeline for screening polymer candidates in supercapacitor applications.**

---

## 📖 Overview
This repository hosts a **reproducible computational pipeline** that integrates:
- **Retrieval** of candidate polymers from the Polymer Genome dataset.
- **Augmentation** with dielectric constant and band gap metrics.
- **Generation** of datasets, high-resolution figures, and CIF files for structural visualization.

The workflow is designed to support **transparent, reproducible materials discovery** and provide **publication-quality outputs** for energy storage research.

---

## ✨ Features
- **Datasets**
  - `candidates_final.csv` → all candidate polymers.
  - `promising_final.csv` → filtered promising candidates (diel_tot > 8, 1 < hse_gap < 3).
- **Figures (1200 dpi, journal-ready)**
  - Scatter plots (all candidates, promising subset, overlay).
  - Histograms (dielectric constants, band gaps).
  - Correlation heatmap.
  - Density plots, boxplots, joint plots.
  - 3D scatter plots.
  - Atomic structure projections (x–y, y–z, x–z).
- **CIF Export**
  - CIF files for each promising candidate.
  - Compatible with **VESTA/OVITO** for ball‑and‑stick 3D visualizations.

---

## 🛠️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/hassanabrar2026-dot/rag-supercapacitor-discovery.git
cd rag-supercapacitor-discovery
pip install -r requirements.txt
