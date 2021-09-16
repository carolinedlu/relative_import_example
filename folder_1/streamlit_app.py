import streamlit as st
import pathlib

current_path = pathlib.Path(__file__).parent.resolve()
st.write(current_path)
