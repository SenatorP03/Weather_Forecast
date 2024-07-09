# Import the required libraries
import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input,slider for number of days and subheader
st.title("WEATHER FORECAST FOR THE DAY")
Place = st.text_input("Enter a city name")
Days = st.slider("Forecast of days",min_value=1,max_value=5,
                 help="Select the number of days for forecast")
options=st.selectbox("Select data to view:",("Temperature","Weather"))
st.header(f"{options} for the next {Days} days in {Place}")

if Place:
    # Get the temperature/Weather data
    try:
        filtered_data= get_data(Place,Days)
        # create visualization
        if options == "Temperature":
            temperature= [dict["main"]["temp"]/10 for dict in filtered_data]
            date = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=date,y=temperature,labels={"x":"Date",
                                                        "y":"Temperature (C)"})
            st.plotly_chart(figure)

        if options == "Weather":
            images = {"Clear":"images/clear.png","Clouds":"images/cloud.png",
                      "Rain":"images/rain.png","Snow":"images/snow.png",}
            Sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_path=[images[condition] for condition in Sky_conditions]
            st.image(image_path,width=110)
    except KeyError:
        st.write("This place doesnt exist")