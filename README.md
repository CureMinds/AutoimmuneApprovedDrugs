# Selection of FDA-Approved Autoimmune Drugs by Lipinski's Rule-of-Five

This project provides a **Streamlit-based web application** that allows users to filter FDA-approved drugs for autoimmune diseases based on **Lipinski's Rule-of-Five**. The app uses molecular descriptors like Molecular Weight, LogP, Number of Hydrogen Bond Donors, and Number of Hydrogen Bond Acceptors to evaluate and display drug candidates.

## Features

- **Molecular Descriptor Calculation**:
  - Molecular Weight (MW)
  - LogP
  - Number of Hydrogen Bond Donors (NumHDonors)
  - Number of Hydrogen Bond Acceptors (NumHAcceptors)
- **Interactive Filtering**:
  - Use sliders to set thresholds for molecular properties.
- **Molecule Visualization**:
  - Visualize filtered molecules and their properties using the `mols2grid` library.
- **Data**:
  - Preloaded dataset of FDA-approved autoimmune drugs.

## Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://huggingface.co/spaces/CureMinds/Autoimmune_Approved_Drugs)

## Getting Started

### Prerequisites

- Python 3.8 or above
- Required libraries:
  - `streamlit`
  - `rdkit`
  - `pandas`
  - `mols2grid`

Install the dependencies with:

```bash
pip install -r requirements.txt

Installation

### Clone this repository:
```bash
git clone https://github.com/AbdullahRagheb/Drug_Discovery_autoimmune.git
cd Drug_Discovery_autoimmune
