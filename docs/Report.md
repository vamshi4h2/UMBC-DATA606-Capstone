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

1. Data Source : *[Kaggle](https://www.kaggle.com/datasets/pankajbhosale/e-commmerce?select=E_Commerce.csv)*. :link:

2. Data Size : 440 KB

3. Data Shape
   > - Number of columns =  12
   > - Number of rows    = 10,999

4.What does dataset represent - This dataset includes customer information, shipment details, and delivery outcomes.

5. Data Dictionary
   
| **Variable**           | **Description**                                                              |
|------------------------|-------------------------------------------------------------------------------|
| **ID**                 | ID Number of Customers                                                       |
| **Warehouse_block**     | Warehouse section where the product was stored (A, B, C, D, E)               |
| **Mode_of_Shipment**    | Mode of product transportation (Ship, Flight, Road)                          |
| **Customer_care_calls** | Number of customer service calls made regarding the shipment                 |
| **Customer_rating**     | Rating provided by the customer (1 = Worst, 5 = Best)                        |
| **Cost_of_the_Product** | Product cost in US Dollars                                                   |
| **Prior_purchases**     | Number of previous purchases made by the customer                            |
| **Product_importance**  | Importance of the product (Low, Medium, High)                                |
| **Gender**              | Customer's gender (Male, Female)                                             |
| **Discount_offered**    | Discount percentage on the product                                           |
| **Weight_in_gms**       | Product weight in grams                                                     |
| **Reached.on.Time_Y.N** | Target variable: 1 = Product did not reach on time, 0 = Product delivered on time |

### Target Variable: 
- **`The Reached.on.Time_Y.N`**: column, where 1 indicates that the product did not reach on time, and 0 indicates it was delivered on time.

### Selected Features/Predictors for the ML Models

The following columns are selected as features (predictors) to train the ML models:

- **`Warehouse_block`**: The section of the warehouse where the product is stored (A, B, C, D, E).
- **`Mode_of_Shipment`**: Mode of product transportation (Ship, Flight, Road).
- **`Customer_care_calls`**: The number of customer service calls made regarding the shipment.
- **`Customer_rating`**: Rating provided by the customer (1 = Worst, 5 = Best).
- **`Cost_of_the_Product`**: Cost of the product in US Dollars.
- **`Prior_purchases`**: Number of previous purchases made by the customer.
- **`Product_importance`**: Importance level of the product (Low, Medium, High).
- **`Gender`**: Customer's gender (Male, Female).
- **`Discount_offered`**: Discount percentage on the product.
- **`Weight_in_gms`**: Weight of the product in grams.

