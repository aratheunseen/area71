import streamlit as st
import plotly.express as px

st.title("Weather Forecast Dashboard")

place = st.text_input("Place")
days = st.slider("Forecast Days",min_value=0,max_value=5,
                 help="Select number for forecast days.")
view = st.selectbox("Select data to view",("Temperatue","Sky views"))

st.subheader(f"{view} for the next {days} days in {place}")

def get_data(days):
    dates = ["2024-05-01", "2024-05-02", "2024-05-03", "2024-05-02", "2024-05-03"]
    temperatures = [1,2,3,4,5]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperature (C)"})

st.plotly_chart(figure)