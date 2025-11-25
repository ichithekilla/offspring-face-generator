import streamlit as st
import random
from pathlib import Path
from PIL import Image
import numpy as np

# Set paths
male_dir = Path("faces/male")
female_dir = Path("faces/female")

# List images
male_faces = list(male_dir.glob("*.jpg")) + list(male_dir.glob("*.png"))
female_faces = list(female_dir.glob("*.jpg")) + list(female_dir.glob("*.png"))

st.title("Offspring Face Generator (v1)")

# Select random faces
father = random.choice(male_faces) if male_faces else None
mother = random.choice(female_faces) if female_faces else None

st.subheader("Parents")
col1, col2 = st.columns(2)
with col1:
    st.text("Father")
    if father:
        st.image(father)
with col2:
    st.text("Mother")
    if mother:
        st.image(mother)

# Add offspring generation
if st.button("Generate Offspring"):
    if father and mother:
        father_img = Image.open(father).convert("RGB")
        mother_img = Image.open(mother).convert("RGB")
        # Resize mother to father's size for simplicity (should improve later!)
        mother_img = mother_img.resize(father_img.size)
        
        # Convert images to numpy arrays
        arr_f = np.array(father_img).astype(np.float32)
        arr_m = np.array(mother_img).astype(np.float32)
        
        # Blend faces by averaging pixels (50/50 mix)
        offspring_arr = ((arr_f + arr_m) / 2).astype(np.uint8)
        offspring_img = Image.fromarray(offspring_arr)

        st.subheader("Offspring")
        st.image(offspring_img)
    else:
        st.warning("Could not find both parent images to blend.")
