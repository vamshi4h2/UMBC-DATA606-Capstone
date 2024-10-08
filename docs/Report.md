
## 1. Project Title - Chicago Traffic Crash Analysis and Modeling

- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang - Fall 2024 Semester
- Author: Vamshi Konapuram
- GitHub : https://github.com/vamshi4h2
- Linkedin : https://www.linkedin.com/in/vamshi-konapuram-2640b11a1/


## 2. Background
### What is it about? 
This project aims to analyze traffic crashes in Chicago to better understand the factors influencing accident rates, severity, and patterns. By examining temporal, spatial, environmental, and human factors, the project seeks to identify trends and correlations that can help improve traffic safety. The analysis will also explore demographic patterns, the relationship between traffic volume, speed limits, and accident hotspots.
### Why does it matter? 
Traffic accidents are a major public health and safety issue, especially in large urban areas like Chicago. Understanding the dynamics of traffic crashes is crucial for reducing fatalities and injuries, improving road safety, and optimizing urban planning. Insights from this project can inform evidence-based policies, improve law enforcement strategies, and enhance the design of transportation infrastructure. The goal is to reduce accident rates and advance sustainable transportation options for the city and other similar urban centers.

### Research Questions:
1. What are the temporal patterns (yearly, monthly, and daily) of traffic crashes in Chicago?
2. How do environmental factors (weather, lighting, road conditions) contribute to traffic accidents?
3. What are the demographic correlations in traffic crashes, and how do human factors (e.g., driver behavior, alcohol involvement) influence accident severity?
4. Can spatial analysis identify accident hotspots, and how do traffic volume and speed limits relate to crash rates?
5. How can the findings support the creation of effective traffic safety programs and policy initiatives?



## 3. DATA
Description : 

1. Data Source : *[Chicago Data Portal](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/data)*. :link:

2. Data Size : 472 MB

3. Data Shape
   > - Number of columns =  47
   > - Number of rows    = 872078

4. Time period (2014 - 2024)
5. What does dataset represent - The Traffic Crashes dataset from the City of Chicago includes detailed records of traffic incidents, capturing crash location, date, and time, along with conditions like weather, road surface, and traffic control. It also provides data on crash types, contributing factors, damage, and injuries, enabling analysis of traffic safety and patterns.

6. Data Dictionary
   
### Data Dictionary

| **Column Name**                        | **Definition**                                                                    |
|----------------------------------------|------------------------------------------------------------------------------------|
| `CRASH_RECORD_ID`                      | Unique identifier for each traffic crash record.                                   |
| `CRASH_DATE_EST_I`                     | Indicates whether the crash date is an estimate.                                   |
| `CRASH_DATE`                           | Actual date and time when the crash occurred.                                      |
| `POSTED_SPEED_LIMIT`                   | Speed limit posted at the crash location.                                          |
| `TRAFFIC_CONTROL_DEVICE`               | Type of traffic control device present at the crash location.                      |
| `DEVICE_CONDITION`                     | Condition of the traffic control device.                                           |
| `WEATHER_CONDITION`                    | Weather conditions at the time of the crash.                                       |
| `LIGHTING_CONDITION`                   | Lighting conditions during the crash.                                              |
| `FIRST_CRASH_TYPE`                     | The first harmful event in the crash.                                              |
| `TRAFFICWAY_TYPE`                      | Type of trafficway where the crash occurred.                                       |
| `LANE_CNT`                             | Number of lanes at the crash location.                                             |
| `ALIGNMENT`                            | The alignment of the road where the crash occurred.                                |
| `ROADWAY_SURFACE_COND`                 | Condition of the road surface during the crash.                                    |
| `ROAD_DEFECT`                          | Any road defects that contributed to the crash.                                    |
| `REPORT_TYPE`                          | Type of report filed for the crash.                                                |
| `CRASH_TYPE`                           | The overall classification of the crash.                                           |
| `INTERSECTION_RELATED_I`               | Whether the crash was intersection-related.                                        |
| `NOT_RIGHT_OF_WAY_I`                   | Indicates failure to yield the right of way.                                       |
| `HIT_AND_RUN_I`                        | Whether the crash involved a hit-and-run.                                          |
| `DAMAGE`                               | The level of damage caused by the crash.                                           |
| `DATE_POLICE_NOTIFIED`                 | Date and time when the police were notified of the crash.                          |
| `PRIM_CONTRIBUTORY_CAUSE`              | Primary cause contributing to the crash.                                           |
| `SEC_CONTRIBUTORY_CAUSE`               | Secondary cause contributing to the crash (if applicable).                         |
| `STREET_NO`                            | Street number where the crash occurred.                                            |
| `STREET_DIRECTION`                     | Direction of the street where the crash occurred.                                  |
| `STREET_NAME`                          | Name of the street where the crash occurred.                                       |
| `BEAT_OF_OCCURRENCE`                   | Police beat where the crash occurred.                                              |
| `PHOTOS_TAKEN_I`                       | Indicates whether photos were taken at the crash scene.                            |
| `STATEMENTS_TAKEN_I`                   | Indicates whether statements were taken at the scene.                              |
| `DOORING_I`                            | Whether the crash involved dooring (when a car door opens into a cyclist's path).   |
| `WORK_ZONE_I`                          | Whether the crash occurred in a work zone.                                         |
| `WORK_ZONE_TYPE`                       | Type of work zone (if applicable).                                                 |
| `WORKERS_PRESENT_I`                    | Whether workers were present in the work zone.                                     |
| `NUM_UNITS`                            | Number of units involved in the crash (e.g., vehicles, pedestrians).               |
| `MOST_SEVERE_INJURY`                   | Most severe injury recorded in the crash.                                          |
| `INJURIES_TOTAL`                       | Total number of injuries resulting from the crash.                                 |
| `INJURIES_FATAL`                       | Total number of fatal injuries.                                                    |
| `INJURIES_INCAPACITATING`              | Total number of incapacitating injuries.                                           |
| `INJURIES_NON_INCAPACITATING`          | Total number of non-incapacitating injuries.                                       |
| `INJURIES_REPORTED_NOT_EVIDENT`        | Total number of reported but not evident injuries.                                 |
| `INJURIES_NO_INDICATION`               | Total number of people involved with no indication of injury.                      |
| `INJURIES_UNKNOWN`                     | Total number of unknown injuries.                                                  |
| `CRASH_HOUR`                           | The hour of the day when the crash occurred.                                       |
| `CRASH_DAY_OF_WEEK`                    | The day of the week when the crash occurred.                                       |
| `CRASH_MONTH`                          | The month when the crash occurred.                                                 |
| `LATITUDE`                             | Latitude coordinate of the crash location.                                         |
| `LONGITUDE`                            | Longitude coordinate of the crash location.                                        |
| `LOCATION`                             | Combined latitude and longitude in a human-readable format.                        |

### Target Variables

- **`has_injuries`**: Indicates whether the crash resulted in any injuries (1 = Yes, 0 = No).
- **`has_fatal`**: Indicates whether the crash resulted in any fatalities (1 = Yes, 0 = No).
- **`crash_type`**: The overall type or classification of the crash (e.g., vehicle collision, pedestrian).
- **`damage`**: The extent of damage caused by the crash (e.g., minor, major, total).
- **`injuries_total`**: Total number of injuries sustained as a result of the crash.
- **`injuries_fatal`**: Total number of fatal injuries sustained as a result of the crash.

### Selected Features/Predictors for the ML Models

The following columns are selected as features (predictors) to train the ML models:
- **`crash_date`**: The date when the crash occurred.
- **`crash_year`**: The year of the crash.
- **`crash_month`**: The month in which the crash occurred.
- **`crash_day_of_week`**: The day of the week when the crash occurred (e.g., Monday, Tuesday, etc.).
- **`crash_hour`**: The hour of the day when the crash occurred.
- **`crash_time_of_day`**: Describes the time of day during which the crash occurred (e.g., morning, night).
- **`latitude`**: Latitude coordinate of the crash location.
- **`longitude`**: Longitude coordinate of the crash location.
- **`beat_of_occurrence`**: The police beat where the crash occurred.
- **`address`**: The street address where the crash occurred.
- **`street_no`**: The street number where the crash occurred.
- **`street_direction`**: The direction of the street where the crash occurred (e.g., N, S, E, W).
- **`street_name`**: The name of the street where the crash occurred.
- **`posted_speed_limit`**: The speed limit posted on the street where the crash occurred.
- **`traffic_control_device`**: The traffic control device in place at the location of the crash (e.g., stop sign, signal).
- **`device_condition`**: The condition of the traffic control device at the time of the crash.
- **`weather_condition`**: The weather condition at the time of the crash (e.g., clear, rain, snow).
- **`lighting_condition`**: The lighting conditions during the crash (e.g., daylight, dark, streetlights on).
- **`trafficway_type`**: The type of trafficway involved in the crash (e.g., divided, undivided).
- **`alignment`**: The alignment of the road where the crash occurred (e.g., straight, curve).
- **`roadway_surface_cond`**: The condition of the road surface at the time of the crash (e.g., dry, wet).
- **`road_defect`**: Any defects present in the road at the time of the crash (e.g., potholes).
- **`first_crash_type`**: The first harmful event or crash type that occurred (e.g., collision with a vehicle).
- **`prim_contributory_cause`**: The primary cause contributing to the crash (e.g., speeding, failure to yield).
- **`sec_contributory_cause`**: The secondary cause contributing to the crash.
- **`num_units`**: The number of units (vehicles or persons) involved in the crash.

## 4. Exploratory Data Analysis(EDA)
### Data Cleansing and Preparation

Data cleansing and preparation is a vital step in transforming raw data into a format suitable for analysis. In this project, we worked with traffic crash data from the Chicago Data Portal, starting by loading and inspecting the raw dataset to identify missing values and assess its structure. We renamed several columns to create more concise and meaningful labels and dropped irrelevant fields like `LOCATION` and `LANE_CNT` to reduce noise. To handle missing values, we filled certain columns, such as `intersection_related_i` and `hit_and_run_i`, with default values of "N" for non-occurrence. Where crash type was categorized as "NO INJURY / DRIVE AWAY," missing injury-related columns were filled with zeros, and rows with critical missing data were removed.

The dataset was further standardized by converting date columns to a datetime format and extracting the crash year. Address fields were combined to create a single address column, ensuring consistency across location data. We also removed rows with invalid coordinates (latitude and longitude values of zero) to maintain the integrity of location-based analysis. Duplicate rows were retained, as they may represent repeated crash reports with the same characteristics.

Next, feature engineering was performed by rounding the posted speed limit to the nearest five and creating new binary features such as `has_injuries` and `has_fatal` to indicate whether a crash involved injuries or fatalities. We also categorized the time of day into periods (overnight, morning, mid-day, evening) based on the hour of the crash. Following final cleaning steps to handle any remaining inconsistencies, the data was saved to CSV files, ready for further analysis. This cleansing process improved data quality, ensured consistency, and created meaningful features that enhanced the dataset’s analytical value.

![Yearly Crash Counts](./images/crash_data.png)
![Monthly Crash Counts](./images/crash_data.png)
![Crash Counts by Day](./images/crash_data.png)
