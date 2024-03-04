import streamlit as st

with st.expander("Start Camera"):
    image = st.camera_input("")

if image:
    st.image(image)
