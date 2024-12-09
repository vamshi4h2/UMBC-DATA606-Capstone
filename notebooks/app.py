import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
DATA_URL = r"/Users/vamshikonapuram/Downloads/crash_df.csv"

@st.cache_data(persist=True)
def load_data():
    data = pd.read_csv(DATA_URL)
    # Convert 'crash_date' from object to datetime
    data['crash_date'] = pd.to_datetime(data['crash_date'])
    
    return data

data = load_data()

st.title("Traffic Collision Analysis")
st.markdown("This application visualizes traffic collisions and their outcomes.")

st.header("Map of Collision Locations with Injuries")
injured_filter = st.slider("Minimum number of injuries", 0, data['injuries_total'].max(), 1)
filtered_data = data[data['injuries_total'] >= injured_filter]

st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state={
         'latitude': data['latitude'].mean(),
         'longitude': data['longitude'].mean(),
         'zoom': 11,
         'pitch': 50,
     },
     layers=[
         pdk.Layer(
            "ScatterplotLayer",
            data=filtered_data,
            get_position=['longitude', 'latitude'],
            get_color='[200, 30, 0, 160]',
            get_radius=100,
         ),
     ],
))

st.header("Collisions by Hour of Day")
hour = st.slider("Hour to view", 0, 23, 0)
filtered_hour_data = data[data['crash_hour'] == hour]
st.markdown("Vehicle collisions between %i:00 and %i:01" % (hour, (hour + 1) % 24))
midpoint = (filtered_hour_data['latitude'].mean(), filtered_hour_data['longitude'].mean())
st.pydeck_chart(pdk.Deck(
     map_style='mapbox://styles/mapbox/light-v9',
     initial_view_state={
         'latitude': midpoint[0],
         'longitude': midpoint[1],
         'zoom': 11,
         'pitch': 50,
     },
     layers=[
         pdk.Layer(
             "HexagonLayer",
             data=filtered_hour_data[['crash_date', 'latitude', 'longitude']],
             get_position=['longitude', 'latitude'],
             radius=100,
             extruded=True,
             pickable=True,
             elevation_scale=4,
             elevation_range=[0, 1000],
         ),
     ],
 ))


# Collision Trends Over Time with Date Range Selection
st.header("Collision Trends Over Time")
min_date = data['crash_date'].min().date()
max_date = data['crash_date'].max().date()
date_from = st.date_input("Date from", min_date, min_value=min_date, max_value=max_date)
date_to = st.date_input("Date to", max_date, min_value=min_date, max_value=max_date)

# Filter data based on the selected date range
filtered_data_by_date = data[(data['crash_date'].dt.date >= date_from) & (data['crash_date'].dt.date <= date_to)]
time_data = filtered_data_by_date.groupby(filtered_data_by_date['crash_date'].dt.date).size()

fig_time = px.line(x=time_data.index, y=time_data.values, labels={'x': 'Date', 'y': 'Number of Collisions'})
st.plotly_chart(fig_time)


day_mapping = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}


st.header("Collisions by Day of the Week")

# Year filter
year_to_filter = st.selectbox("Select Year", options=data['crash_year'].unique(), index=len(data['crash_year'].unique()) - 1)
filtered_data_year = data[data['crash_year'] == year_to_filter]

# Time of day filter
time_of_day = st.selectbox("Select Time of Day", options=sorted(data['crash_time_of_day'].unique()))
filtered_data_time = filtered_data_year[filtered_data_year['crash_time_of_day'] == time_of_day]

# Apply mapping from number to day name
filtered_data_time['day_of_week_name'] = filtered_data_time['crash_day_of_week'].map(day_mapping)

# Group by the new 'day_of_week_name' column
day_of_week_data = filtered_data_time['day_of_week_name'].value_counts().sort_index()
fig_dow = px.bar(x=day_of_week_data.index, y=day_of_week_data.values, labels={'x': 'Day of the Week', 'y': 'Number of Collisions'})
st.plotly_chart(fig_dow)



# Severity filter
st.header("Collisions by Day of the Week")


severity = st.radio("Select Severity", ('All', 'Injuries', 'Fatal'))
if severity == 'Injuries':
    filtered_data_severity = data[data['has_injuries'] > 0]
elif severity == 'Fatal':
    filtered_data_severity = data[data['has_fatal'] > 0]
else:
    filtered_data_severity = data

# Apply mapping from number to day name
filtered_data_severity['day_of_week_name'] = filtered_data_severity['crash_day_of_week'].map(day_mapping)

# Group by the new 'day_of_week_name' column
day_of_week_data = filtered_data_severity['day_of_week_name'].value_counts().sort_index()
fig_dow = px.bar(x=day_of_week_data.index, y=day_of_week_data.values, labels={'x': 'Day of the Week', 'y': 'Number of Collisions'})
st.plotly_chart(fig_dow)


lighting_condition = st.selectbox("Select Lighting Condition", options=sorted(data['lighting_condition'].unique()))
filtered_by_lighting = data[data['lighting_condition'] == lighting_condition]

# Selection for weather conditions
weather_condition = st.selectbox("Select Weather Condition", options=sorted(data['weather_condition'].unique()))
filtered_by_weather = data[data['weather_condition'] == weather_condition]

# Plotting collisions by lighting condition
st.header(f"Collisions under {lighting_condition} Conditions")
lighting_data = filtered_by_lighting['crash_day_of_week'].value_counts().sort_index()
fig_lighting = px.bar(x=lighting_data.index.map(day_mapping), y=lighting_data.values, labels={'x': 'Day of the Week', 'y': 'Number of Collisions'})
st.plotly_chart(fig_lighting)

# Plotting collisions by weather condition
st.header(f"Collisions in {weather_condition} Weather")
weather_data = filtered_by_weather['crash_day_of_week'].value_counts().sort_index()
fig_weather = px.bar(x=weather_data.index.map(day_mapping), y=weather_data.values, labels={'x': 'Day of the Week', 'y': 'Number of Collisions'})
st.plotly_chart(fig_weather)






if st.checkbox("Show raw data", False):
    st.subheader('Raw Data')
    st.write(data)
