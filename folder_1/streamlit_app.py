import streamlit as st
import pathlib
import sys


p = pathlib.Path(".")  #current folder (scripts) 
st.write("Current folder:")
st.write(p)
parent = p.resolve().parent.resolve() #parent folder 
libfolder = parent / "scmopt"  
sys.path.append(str(libfolder)) # add both paths 
sys.path.append(str(parent))
st.write(parent)
st.write(libfolder)
