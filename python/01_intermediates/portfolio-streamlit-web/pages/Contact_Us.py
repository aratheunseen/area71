import streamlit as st

st.title("Contact Us")

with st.form(key='form',clear_on_submit=True,border=True):
    user_email = st.text_input("Your Email Address",key='email')
    message = st.text_area("Your Message",key='message')
    button = st.form_submit_button("Submit",use_container_width=True)

    if button:
        st.success(f"Thank you for your message! We will get back to you at {user_email} as soon as possible.")


st.info("© 2024 aratheunseen. All rights reserved.")