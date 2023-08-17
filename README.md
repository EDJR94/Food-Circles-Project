# 1. Business Problem

Food Circles is a restaurant marketplace. Its core business is to facilitate the connection and negotiations between customers and restaurants. Restaurants register on the Food Circles platform, providing information such as address, cuisine type, reservation availability, delivery options, and a rating for their services and products, among other details.

The CEO needs to make informed strategic decisions, and to do so, an analysis of the company's data is required along with the creation of dashboards within a unified tool. These dashboards will allow the CEO to quickly access information and make swift decisions. The CEO is interested in the following growth insights:

## Overview:
1. How many unique restaurants are registered?
2. How many unique countries are registered?
3. How many unique cities are registered?
4. What is the total number of reviews?
5. How many distinct cuisine types are registered?

## Country View:
1. Which country has the most registered cities?
2. Which country has the most registered restaurants?
3. Which country has the most restaurants with a price level of 4?
4. Which country has the highest number of distinct cuisine types?
5. Which country has the most reviews?
6. Which country has the most restaurants offering delivery?
7. Which country has the most restaurants accepting reservations?
8. Which country has the highest average number of reviews?
9. Which country has the highest average rating?
10. Which country has the lowest average rating?
11. What is the average price for a meal for two, per country?

## City View:
1. Which city has the most registered restaurants?
2. Which city has the most restaurants with an average rating above 4?
3. Which city has the most restaurants with an average rating below 2.5?
4. Which city has the highest average price for a meal for two?
5. Which city has the most distinct cuisine types?
6. Which city has the most restaurants accepting reservations?
7. Which city has the most restaurants offering delivery?
8. Which city has the most restaurants accepting online orders?

## Restaurants View:
1. Which restaurant has the most reviews?
2. Which restaurant has the highest average rating?
3. Which restaurant has the highest average price for a meal for two?
4. Among Brazilian cuisine restaurants, which has the lowest average rating?
5. Among Brazilian cuisine restaurants in Brazil, which has the highest average rating?
6. Are restaurants that accept online orders also the ones with the highest average number of reviews?
7. Are restaurants that accept reservations also the ones with the highest average price for a meal for two?
8. Do Japanese cuisine restaurants in the United States have a higher average price for a meal for two compared to American BBQ restaurants?

## Cuisine View:
1. Among Italian cuisine restaurants, which has the highest average rating?
2. Among Italian cuisine restaurants, which has the lowest average rating?
3. Among American cuisine restaurants, which has the highest average rating?
4. Among American cuisine restaurants, which has the lowest average rating?
5. Among Arabian cuisine restaurants, which has the highest average rating?
6. Among Arabian cuisine restaurants, which has the lowest average rating?
7. Among Japanese cuisine restaurants, which has the highest average rating?
8. Among Japanese cuisine restaurants, which has the lowest average rating?
9. Among homemade cuisine restaurants, which has the highest average rating?
10. Among homemade cuisine restaurants, which has the lowest average rating?
11. Which cuisine type has the highest average price for a meal for two?
12. Which cuisine type has the highest average rating?
13. Which cuisine type has the most restaurants accepting online orders and offering delivery?

# 2. Assumptions
1. Marketplace model was assumed for the business.
2. Assumed views for the business are: Overview, Country, Cuisine, and City.

# 3. Solution Strategy

1. Dashboards were built based on key metrics from the main business views:
    1. Overview
    2. Country
    3. City
    4. Cuisine
2. Each view is represented by the following sets of metrics:
    
    ### Overview:
    
    1. Registered restaurants
    2. Distinct registered countries
    3. Distinct registered cities
    4. Offered cuisines
    5. Total reviews on the platform
    6. Map showing restaurant locations
    
    ### Country View:
    
    1. Number of restaurants per country
    2. Price for Two People by country
    3. Distinct cuisine types per country
    4. Average rating by country
    
    ### Cuisine View:
    
    1. Restaurant with the most reviews
    2. Best-rated restaurant
    3. Restaurant with highest price for Two People
    4. Best-rated cuisine
    
    ### City View:
    
    1. Number of restaurants per city
    2. Cities with the best and worst ratings
    3. Cities with the highest price for Two People
    4. Cities with the highest number of restaurants accepting online orders.

# 4. Top Data Insights

1. Restaurants that accept online orders are not necessarily the ones with the most reviews on the platform.
2. Restaurants that accept reservations tend to have higher average prices for a meal for two.
3. Despite having the highest number of restaurants with the highest price level, the United States does not have the highest average price for a meal for two.

# 5. Final Product

An online dashboard hosted in the cloud, accessible from any internet-connected device.

The dashboard can be accessed through this link: [https://projects-foodcircle.streamlit.app/](https://projects-foodcircle.streamlit.app/)

# 6. Conclusion

The aim of this project is to create dashboards with charts and tables that present business metrics in the best possible way for the CEO to make decisions.

We can conclude that the dashboard fulfills the CEO's requirements, allowing them to select desired metrics in the preferred way, covering the main views of the Food Circles marketplace.

# 7. Next Steps

1. It's evident that a significant portion of the business is concentrated in the United States and India, where established restaurants with numerous reviews are located. The CEO should focus efforts on countries with lower platform adoption and lower ratings, such as Brazil.
2. Streamline the number of metrics in each view to focus on asking the right questions.

