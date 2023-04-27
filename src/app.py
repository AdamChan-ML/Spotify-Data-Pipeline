import streamlit as st

from dashboard_page import show_explore_page
from about_project_page import show_about_project

st.sidebar.title("Selecting Visual Charts")
st.sidebar.markdown("Selecting the Charts accordingly.")
page = st.sidebar.selectbox("Explore / Predict", ("Dashboard", "About This Project"))

if page == "Dashboard":
    show_explore_page()
else:
    show_about_project()