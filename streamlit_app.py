import streamlit as st
from map import get_position_from_map
from get_weather import WeatherData
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import dotenv
import os

dotenv.load_dotenv('.env')


def layout():
    """create the layout for the web application"""

    st.title("Delfinen - Temperature")
    st.write("Please select a location on the map to see the temperature at that location.")
    position = get_position_from_map()
    if position != None:
        lat, lon = position[0], position[1]
    else:
        lat, lon = 59.3293, 18.0686
        
    st.markdown("## Temperature")
    current_temp = WeatherData(lat=lat, lon=lon, api_key=os.getenv('api_key')).get_current_temp()
    if current_temp is None:
        st.error("Failed to fetch current temperature. Please check the API or try again later.")
    else:
        st.metric("Current temperature", f"{int(current_temp)} °C")
    #st.metric("Current temperature", f"{int(current_temp)} °C")
    st.write(f"Showing temperature at latitude {lat} and longitude {lon}.")


    st.markdown("## Hourly forecast for the next 24 hours")
    temp_next_24h = WeatherData(lat=lat, lon=lon, api_key=os.getenv('api_key')).get_temp_next_24h()
    col1, col2 = st.columns([2,1])

    with col2:
        df = pd.DataFrame(temp_next_24h, columns=['Time', 'Temperature'])
        st.write(df)

    with col1:
        fig, ax = plt.subplots()
        ax.plot(df['Time'], df['Temperature'])
        for i, value in enumerate(df['Temperature']):
            plt.text(df['Time'][i], df['Temperature'][i], f"{round(value)}°", fontsize=8, ha='left', va='bottom')
        ax.set_xlim(min(df['Time']), max(df['Time']))
        ax.xaxis.set_tick_params(rotation=45, labelsize=9)
        ax.yaxis.set_tick_params(labelsize=9)
        ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H'))
        ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        plt.xlabel('Time')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature forecast for the next 24 hours')
        st.pyplot(plt)




if __name__ == "__main__":
    layout()

