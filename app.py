import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Airport Passenger Prediction",
    layout="wide"
)

st.title("✈️ AI-Based Airport Passenger Flow Prediction System")

st.markdown("""
Forecasting passenger demand at
San Francisco International Airport (SFO)
using historical passenger traffic data and SARIMA forecasting.
""")

try:
    forecast_df = pd.read_csv("future_passenger_forecast.csv")

    st.subheader("Future Passenger Forecast")

    st.dataframe(forecast_df)

    st.line_chart(forecast_df.iloc[:,1])

except Exception as e:
    st.error(f"Error loading forecast file: {e}")

st.subheader("Operational Insights")

st.subheader("Project Summary")

st.write("""
This project uses historical passenger traffic data from
San Francisco International Airport (SFO) to forecast future
passenger volumes.

A Seasonal ARIMA (SARIMA) forecasting model was developed
to identify trends and seasonal variations in airport traffic.

The predicted passenger demand helps airport authorities
improve resource allocation, workforce planning,
terminal management and operational efficiency.
""")