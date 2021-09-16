import streamlit as st
import pathlib

current_path = pathlib.Path(__file__).parent.resolve()

st.write("Path to Python file containing Streamlit app (using pathlib):")
st.write(current_path)

p = pathlib.Path(".")  #current folder (scripts) 
st.write("pathlib.Path")
st.write(p)
parent = p.resolve().parent.resolve() #parent folder 
libfolder = parent / "scmopt"  
sys.path.append(str(libfolder)) # add both paths 
sys.path.append(str(parent))
