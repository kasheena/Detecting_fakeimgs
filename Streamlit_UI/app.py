import streamlit as st
import dashboard
import classifyPage

st.set_page_config(
    page_title="Deforgify",
    page_icon="🤖",
    layout="wide")

PAGES = {
    "Dashboard": dashboard,
    "Classify Image": classifyPage
}

st.sidebar.title("💡 Ideation")

st.sidebar.write("Enhancing Image Authenticity Verification through Deep Learning Techniques: A Study on the Detection and Mitigation of Fake Images")

st.sidebar.title(" Team Members:")
st.sidebar.write(" Kasheena Mulla
                 Shruti Kharche
                 Pratichee Mishra")
                 
st.sidebar.subheader('Navigation:')
selection = st.sidebar.radio("", list(PAGES.keys()))

page = PAGES[selection]

page.app()
