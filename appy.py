import streamlit as st
import os

# I-print natin kung ano ang nakikita ng server
st.write("Checking folder contents:")
try:
    files = os.listdir("image")
    st.write(files)
except FileNotFoundError:
    st.error("Error: Hindi mahanap ang folder na 'image'. Siguraduhin na nasa main folder ito.")

# Subukan ang image
if os.path.exists("image/1.png"):
    st.image("image/1.png")
else:
    st.error("Error: Ang file na 'image/1.png' ay hindi matagpuan sa disk.")