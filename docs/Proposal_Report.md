
## 1. Project Title - E-Commerce Product Delivery Prediction
- Prepared for UMBC Data Science Master Degree Capstone by Dr Chaoji (Jay) Wang - Fall 2024 Semester
- Author: Vamshi Konapuram
- GitHub : https://github.com/vamshi4h2
- Linkedin : https://www.linkedin.com/in/vamshi-konapuram-2640b11a1/


## 2. Background
### What is it about? 
This project aims to predict whether a product from an international e-commerce company will be delivered on time or not. It also analyzes various factors that impact delivery times and studies customer behavior patterns. By using machine learning techniques, this project seeks to identify key factors influencing timely deliveries and customer satisfaction.

### Why does it matter? 
Timely delivery is a critical factor for customer satisfaction in the e-commerce industry. Late deliveries can result in negative customer experiences, loss of sales, and damage to the company’s reputation. By predicting the likelihood of late deliveries, the company can proactively address logistics challenges, optimize operations, and improve customer satisfaction. Additionally, understanding customer behavior and the factors affecting delivery efficiency can provide valuable insights for decision-making.

### Research Questions:
1. What are the primary factors influencing whether a product reaches its destination on time?
2. Can machine learning models effectively predict product delivery outcomes based on customer and shipment data?
3. How can the company optimize its logistics processes to minimize delays?



## 3. DATA
Description : 

1. Data Source : *[Chicago Data Portal](https://data.cityofchicago.org/Transportation/Traffic-Crashes-Crashes/85ca-t3if/data)*. :link:

2. Data Size : 472 MB

3. Data Shape
   > - Number of columns =  47
   > - Number of rows    = 872078

4. What does dataset represent - The Traffic Crashes dataset from the City of Chicago includes detailed records of traffic incidents, capturing crash location, date, and time, along with conditions like weather, road surface, and traffic control. It also provides data on crash types, contributing factors, damage, and injuries, enabling analysis of traffic safety and patterns.

5. Data Dictionary
   
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
