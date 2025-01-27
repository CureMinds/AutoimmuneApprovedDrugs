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

## Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Installation

### Clone this repository:
```bash
git clone https://github.com/AbdullahRagheb/Drug_Discovery_autoimmune.git
cd Drug_Discovery_autoimmune
```

## Run the application:
```bash
streamlit run app.py
```

## Usage

1. Launch the app by running the command above.
2. Use the sidebar sliders to adjust thresholds for molecular properties.
3. View the filtered drug list and their molecular descriptors in the main panel.

## Dataset

The dataset used in this project is publicly available and can be downloaded from [here](https://raw.githubusercontent.com/AbdullahRagheb/Drug_Discovery_autoimmune/main/autoimmune_drug.txt). It includes information about FDA-approved autoimmune drugs, including their SMILES strings and generic names.

## Code Highlights

- **Descriptor Calculation**:  
  Functions are provided to calculate molecular weight, LogP, number of hydrogen bond donors, and acceptors using `rdkit`.

- **Filtering Logic**:  
  Interactive filters allow users to set thresholds for drug properties, dynamically updating the displayed results.

- **Visualization**:  
  Molecules are visualized with `mols2grid`, showing images alongside calculated properties.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Libraries**:
  - [Streamlit](https://streamlit.io/)
  - [RDKit](https://www.rdkit.org/)
  - [mols2grid](https://github.com/cbouy/mols2grid)

Special thanks to the open-source community for providing tools and resources that made this project possible.
