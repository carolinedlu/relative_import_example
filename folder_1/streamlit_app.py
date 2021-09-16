import streamlit as st
import pathlib

current_path = pathlib.Path(__file__).parent.resolve()

st.write("Path to Python file containing Streamlit app (using pathlib):")
st.write(current_path)
