import streamlit as st
import pathlib
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(layout="wide", page_title="BD Job Market", page_icon="🇧🇩")

html_path = pathlib.Path("Bd-Job-Market-Dashboard.html")

if html_path.exists():
    html_content = html_path.read_text(encoding="utf-8")
    st.components.v1.html(html_content, height=1200, scrolling=True)
else:
    st.error("Bd-Job-Market-Dashboard.html not found - make sure file is in same folder as app.py")