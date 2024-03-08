import streamlit as st

st.title("Weather Forecast Dashboard")

place = st.text_input("Place")
days = st.slider("Forecast Days",min_value=0,max_value=5,help="Select number for forecast days.")
view = st.selectbox("Select data to view",("Temperatue","Sky views"))

st.subheader(f"{view} for the next {days} days in {place}")
