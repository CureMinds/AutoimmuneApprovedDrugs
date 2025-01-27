import mols2grid
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from rdkit import Chem
from rdkit.Chem.Descriptors import ExactMolWt, MolLogP, NumHDonors, NumHAcceptors

st.title("Selection FDA-Autoimmune Approved Drugs by Lipinski's Rule-of-Five with Streamlit")

st.markdown("""
- App built by [Abdullah Ragheb](https://abdullahragheb.github.io/)
""")
st.markdown("""
- App built by [Abdullah Ragheb](https://abdullahragheb.github.io/)
""")

@st.cache_data
def download_dataset():
    """Loads once then cached for subsequent runs"""
    df = pd.read_csv(
        "https://raw.githubusercontent.com/AbdullahRagheb/Drug_Discovery_autoimmune/main/autoimmune_drug.txt", sep="\t"
    ).dropna()
    return df

# Calculate descriptors
def calc_mw(smiles_string):
    """Given a smiles string (ex. C1CCCCC1), calculate and return the molecular weight"""
    mol = Chem.MolFromSmiles(smiles_string)
    return ExactMolWt(mol)

def calc_logp(smiles_string):
    """Given a smiles string (ex. C1CCCCC1), calculate and return the LogP"""
    mol = Chem.MolFromSmiles(smiles_string)
    return MolLogP(mol)

def calc_NumHDonors(smiles_string):
    """Given a smiles string (ex. C1CCCCC1), calculate and return the NumHDonors"""
    mol = Chem.MolFromSmiles(smiles_string)
    return NumHDonors(mol)

def calc_NumHAcceptors(smiles_string):
    """Given a smiles string (ex. C1CCCCC1), calculate and return the NumHAcceptors"""
    mol = Chem.MolFromSmiles(smiles_string)
    return NumHAcceptors(mol)


# Copy the dataset so any changes are not applied to the original cached version
df = download_dataset().copy()

# Debugging: Inspect the DataFrame
print("Columns in DataFrame:", df.columns)
print("First few rows:", df.head())

# Check if 'smiles' column exists
if "smiles" in df.columns:
    df["MW"] = df.apply(lambda x: calc_mw(x["smiles"]), axis=1)
else:
    raise KeyError("The column 'smiles' does not exist in the DataFrame.")
df["LogP"] = df.apply(lambda x: calc_logp(x["smiles"]), axis=1)
df["NumHDonors"] = df.apply(lambda x: calc_NumHDonors(x["smiles"]), axis=1)
df["NumHAcceptors"] = df.apply(lambda x: calc_NumHAcceptors(x["smiles"]), axis=1)


# Sidebar panel
st.sidebar.header('Set parameters')
st.sidebar.write('*Note: Display compounds having values less than the following thresholds*')
weight_cutoff = st.sidebar.slider(
    label="Molecular weight",
    min_value=700,
    max_value=3650,
    value=2100,
    step=10,
)
logp_cutoff = st.sidebar.slider(
    label="LogP",
    min_value=-1.8,
    max_value=1.8,
    value=0.5,
    step=0.15,
)
NumHDonors_cutoff = st.sidebar.slider(
    label="NumHDonors",
    min_value=10,
    max_value=50,
    value=21,
    step=1,
)
NumHAcceptors_cutoff = st.sidebar.slider(
    label="NumHAcceptors",
    min_value=11,
    max_value=50,
    value=20,
    step=1,
)

df_result = df[df["MW"] < weight_cutoff]
df_result2 = df_result[df_result["LogP"] < logp_cutoff]
df_result3 = df_result2[df_result2["NumHDonors"] < NumHDonors_cutoff]
df_result4 = df_result3[df_result3["NumHAcceptors"] < NumHAcceptors_cutoff]

st.write(df_result4.shape)
st.write(df_result4)

# Rename columns to match mols2grid expectations
df_result4 = df_result4.rename(columns={"smiles": "SMILES", "generic_name": "Name"})

# Check the DataFrame
print("Columns in df_result4 after renaming:", df_result4.columns)
print("First few rows of df_result4:")
print(df_result4.head())

# Generate the mols2grid display
raw_html = mols2grid.display(
    df_result4,
    subset=["img", "Name", "MW", "LogP", "NumHDonors", "NumHAcceptors"],
    mapping={"SMILES": "SMILES", "Name": "Name"}
)._repr_html_()

# Render the HTML
components.html(raw_html, width=900, height=1100, scrolling=False)
