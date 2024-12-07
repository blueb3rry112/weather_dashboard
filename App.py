import streamlit as st
import requests
import pandas as pd
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.pexels.com/photos/1118873/pexels-photo-1118873.jpeg?cs=srgb&dl=pexels-jplenio-1118873.jpg&fm=jpg");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
) 

resp = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,relative_humidity_2m,is_day,precipitation,surface_pressure,wind_speed_10m&daily=temperature_2m_max,sunrise,sunset,precipitation_sum")
import json
value = json.loads(resp.text)
st.write("Haleema")
st.title("weather dashboard")
st.subheader("asia/colombo")
st.image("colombo-sri-lanka.jpg")
st.sidebar.write("location details")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", value["current"]["temperature_2m"], "1.2 F")
col2.metric("Wind", value["current"]["wind_speed_10m"], "-8%")
col3.metric("Humidity", value["current"]["relative_humidity_2m"], "4%")
st. sidebar.selectbox("pick your data",
("Precipitation", "Sunrise", "Sunset", "Maximum Temperature"))
st.video("https://www.youtube.com/watch?v=yrOYxLt9SCI&list=PPSV")


# st.sidebar.write("latitude", value ['latitude'])
# st.sidebar.write("longitude", value ['longitude'])
st.title("Weather Dashboard")

# st.sidebar.header("Input Location")
latitude = st.sidebar.text_input("Latitude", "37.7749")
longitude = st.sidebar.text_input("Longitude", "-122.4194")

if st.sidebar.button("Get Weather Data"):
    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data["hourly"]["temperature_2m"]
        time_series = range(len(temperature))
        
        # Convert to DataFrame for better visualization
        df = pd.DataFrame({"Time": time_series, "Temperature": temperature})
        
        st.write("Hourly Temperature Data:")
        st.line_chart(df.set_index("Time"))  # Plot temperature as a line chart
    else:
        st.error("Failed to retrieve data. Please check your inputs.")

