import streamlit as st
import pathlib
import sys


p = pathlib.Path(".")  #current folder (scripts) 
# st.write("Current folder:")
# st.write(p)
parent = p.resolve().parent.resolve() #parent folder 
# libfolder = parent / "scmopt"  
# new_path = sys.path.append(str(libfolder)) # add both paths 
new_path_1 = sys.path.append("../..")
st.write(new_path_1)
# st.write(parent)
# st.write(libfolder)
