import streamlit as st

st.form(clear_on_submit=True,border=True,key='form')
st.text_input("Your Email Address",key='email')
st.text_area("Your Message",key='message')
st.button("Submit",use_container_width=True,key='submit')
# st.form_submit_button("Submit",use_container_width=False)