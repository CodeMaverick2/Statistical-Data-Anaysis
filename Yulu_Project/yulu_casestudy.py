# -*- coding: utf-8 -*-
"""Yulu_CaseStudy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XKICJB7ZSDOBEw64XyFByeT1wvIDvVYp

# **Yulu Buisness Case Study**

# **About Yulu**
Yulu is India’s leading micro-mobility service provider, which offers unique vehicles for the daily commute. Starting off as a mission to eliminate traffic congestion in India, Yulu provides the safest commute solution
through a user-friendly mobile app to enable shared, solo and sustainable commuting.


**Business Problem**

Yulu's market research team want's to know if there are any relation between the customer's and the product they buy such that they can focus on that and improve the experience for customer's.

1. **Descriptive Analysis:**Which variables are significant in predicting the demand for shared electric cycles in the Indian market?

2. **Demands :** How well those variables describe the electric cycle demands
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import scipy.stats as spy

"""Importing libraries"""

!wget https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/001/428/original/bike_sharing.csv?1642089089 -O yulu_data.csv

"""In the above step we are downloading the data from the link"""

df = pd.read_csv("yulu_data.csv")
df

"""Here we successfully read the file and print it

# **Exploratory Data Analysis (EDA)**

## **Numerical Analysis**
"""

df.shape

"""Shape of the dataset"""

df.info()

df.columns

"""Columns of the dataset"""

df.head()

"""Head function gives us the top 5 default rows of the dataset."""

df.tail()

"""Tail function gives us the bottom 5 default rows of the dataset."""

print(df.describe())

df.dtypes

"""Datatype of the columns"""

print(df['season'].unique())

"""This provides us with unique season's numbering"""

print(df['holiday'].unique())

"""This provides us with unique holiday's numbering"""

print(df['workingday'].unique())

"""This provide us with workingday's numbering"""

print(df['weather'].unique())

"""This provides us with unique weather's numbering"""

df['datetime'] = pd.to_datetime(df['datetime'])

"""We have successfully changed the datatype of datetime"""

weather_conditions = df['weather'].value_counts()
print(weather_conditions)
plt.pie(weather_conditions, labels=weather_conditions.index)
plt.show()

"""Pie chart to analyze the distribution of weather
> The clear weather is dominant among all hugely

> The bad weather or heavily raining is less than 1%
"""

holiday_counts = df['holiday'].value_counts()
print(holiday_counts)
plt.pie(holiday_counts, labels=holiday_counts.index)
plt.show()

"""This pie chart shows us the holiday distribution and working day's

## **Null value's detection**

First calculating IQR through calculating Q1 and Q3 and then judging the outliers based on the lower bound and upper bound
"""

Q1 = df['count'].quantile(0.25)
Q3 = df['count'].quantile(0.75)
IQR = Q3 - Q1
print(IQR)
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['count'] < lower_bound) | (df['count'] > upper_bound)]

print("Outliers:")
print(outliers)

plt.figure(figsize=(8, 6))
sns.boxplot(x='count', data=df, palette='coolwarm')
plt.title('Distribution of Rental Counts (with Outliers)')
plt.xlabel('Rental Counts')
plt.show()

"""Visualize the distribution of 'count' attribute with outliers"""

plt.figure(figsize=(8, 6))
sns.boxplot(x='count', data=df[(df['count'] >= lower_bound) & (df['count'] <= upper_bound)], palette='coolwarm')
plt.title('Distribution of Rental Counts (without Outliers)')
plt.xlabel('Rental Counts')
plt.show()

"""Visualize the distribution of count attribute without outliers

## **Probability Analysis**
"""

# Calculate the total number of observations
total_obs = len(df)

# Calculate the probability of a user being casual
prob_casual = len(df[df['casual'] > 0]) / total_obs

# Calculate the probability of a user being registered
prob_registered = len(df[df['registered'] > 0]) / total_obs

# Calculate the probability of a user being both casual and registered (assuming independence)
prob_both = len(df[(df['casual'] > 0) & (df['registered'] > 0)]) / total_obs

# Calculate the probability of a user being either casual or registered (assuming independence)
prob_either = (len(df[df['casual'] > 0]) + len(df[df['registered'] > 0]) - prob_both) / total_obs

# Display probabilities
print("Probability of a user being casual:", prob_casual)
print("Probability of a user being registered:", prob_registered)
print("Probability of a user being both casual and registered:", prob_both)
print("Probability of a user being either casual or registered:", prob_either)

"""## **Univariate Analysis**"""

plt.figure(figsize=(10, 6))
sns.histplot(df['count'], bins=30, kde=True)
plt.title('Distribution of Count')
plt.xlabel('Count')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(df['temp'], bins=30, kde=True, color='skyblue', label='Temperature')
sns.histplot(df['atemp'], bins=30, kde=True, color='salmon', label='Feeling Temperature')
plt.title('Distribution of Temperature and Feeling Temperature')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Frequency')
plt.legend()
plt.show()

""" Distribution of Temperature and Feeling Temperature"""

plt.figure(figsize=(12, 6))
sns.histplot(df['humidity'], bins=30, kde=True, color='lightgreen')
plt.title('Distribution of Humidity')
plt.xlabel('Humidity')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(df['windspeed'], bins=30, kde=True, color='lightcoral')
plt.title('Distribution of Wind Speed')
plt.xlabel('Wind Speed')
plt.ylabel('Frequency')
plt.show()

"""Distribution of Humidity and Wind Speed"""

plt.figure(figsize=(12, 6))
sns.histplot(df['casual'], bins=30, kde=True, color='skyblue', label='Casual Users')
sns.histplot(df['registered'], bins=30, kde=True, color='salmon', label='Registered Users')
plt.title('Distribution of Casual and Registered Users')
plt.xlabel('Number of Users')
plt.ylabel('Frequency')
plt.legend()
plt.show()

"""Distribution of Casual and Registered Users"""

plt.figure(figsize=(8, 6))
sns.countplot(x='weather', data=df, palette='pastel')
plt.title('Distribution of Weather Conditions')
plt.xlabel('Weather')
plt.ylabel('Count')
plt.show()

"""Distribution of Weather Conditions"""

plt.figure(figsize=(8, 6))
sns.countplot(x='season', data=df, palette='bright')
plt.title('Distribution of Seasons')
plt.xlabel('Season')
plt.ylabel('Count')
plt.show()

"""Distribution of Seasons"""

plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
sns.histplot(df['temp'], bins=30, kde=True, color='skyblue')
plt.title('Distribution of Temperature')

plt.subplot(2, 2, 4)
sns.histplot(df['count'], bins=30, kde=True, color='salmon')
plt.title('Distribution of Rental Counts')

plt.tight_layout()
plt.show()

"""Distribution plots of continuous variables

## **Bivariate Analysis**
"""

plt.figure(figsize=(12, 6))
sns.boxplot(x='workingday', y='count', data=df)
plt.title('Count vs Working Day')
plt.xlabel('Working Day')
plt.ylabel('Count')
plt.show()

"""Boxplot for count vs working day.

The box plot suggests that the count of rental bikes may be slightly higher on working days compared to non-working days.

"""

plt.figure(figsize=(12, 6))
sns.boxplot(x='season', y='count', data=df)
plt.title('Count vs Season')
plt.xlabel('Season')
plt.ylabel('Count')
plt.show()

"""Boxplot for count vs season.

> Count vs Season: There are variations in the count of rental bikes across different seasons, with potentially higher counts during certain seasons.
"""

plt.figure(figsize=(12, 6))
sns.boxplot(x='weather', y='count', data=df)
plt.title('Count vs Weather')
plt.xlabel('Weather')
plt.ylabel('Count')
plt.show()

"""Boxplot for count vs weather

 > Count vs Weather: The box plot shows variations in the count of rental bikes based on weather conditions, with fewer rentals during adverse weather conditions.

## **Analysis on EDA**

**Comments on EDA :**

- Shape of data: The dataset contains 10886 rows and 12 columns.
- Data types: All attributes are of appropriate data types.
- Missing values: There are no missing values in the dataset.
- Statistical summary: Provides summary statistics for numerical attributes.

**Univariate Analysis :**
  - Temperature: Approximately normal distribution.
  - Humidity: Slightly right-skewed distribution.
  - Windspeed: Right-skewed distribution with some outliers.
  - Rental Counts: Right-skewed distribution with potential outliers.
  - Weather Conditions: Majority of days have weather condition 1.
  - Seasons: Dataset contains roughly equal observations across all four seasons.

**Bivariate Analysis :**
  - Rental counts tend to be slightly higher on working days compared to non-working days.
  - Rental counts vary across different seasons and weather conditions.

# **Hypothesis Testing**

## **2- Sample T-Test**

**Problem Statement:
To determine if there is a significant difference in the number of electric cycles rented between working days and non-working days.**
* Null Hypothesis (H0): There is no significant difference in the number of electric cycles rented between working days and non-working days.

* Alternative Hypothesis (H1): There is a significant difference in the number of electric cycles rented between working days and non-working days.

**Visual analysis according to the test**
"""

plt.figure(figsize=(8, 6))
sns.boxplot(x='workingday', y='count', data=df, palette='coolwarm')
plt.title('Number of Electric Cycles Rented by Working Day')
plt.xlabel('Working Day')
plt.ylabel('Number of Electric Cycles Rented')
plt.show()

"""**Selecting appropriate test and assumptions**
> Selecting the appropriate test

* We will use a 2-sample t-test to compare the means of the number of electric cycles rented on working days and non-working days.

> Check test assumptions

> Assumption 1: Independence of observations

> Add blockquote


* We assume that the observations of the number of electric cycles rented on working days are independent from the observations on non-working days.

> Assumption 2: Normality of data

* We need to check if the data for the number of electric cycles rented on working days and non-working days are approximately normally distributed.

* We can visually inspect the distributions using histograms or Q-Q plots, and we can also perform normality tests such as Shapiro-Wilk test.

**Let's check the normality assumption using Q-Q plots**
"""

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
spy.probplot(df[df['workingday'] == 1]['count'], dist="norm", plot=plt)
plt.title('Q-Q Plot for Number of Electric Cycles Rented on Working Days')

plt.subplot(1, 2, 2)
spy.probplot(df[df['workingday'] == 0]['count'], dist="norm", plot=plt)
plt.title('Q-Q Plot for Number of Electric Cycles Rented on Non-Working Days')
plt.tight_layout()
plt.show()

workingday_yes = df[df['workingday'] == 1]['count']
workingday_no = df[df['workingday'] == 0]['count']

t_stat, p_value = spy.ttest_ind(workingday_yes, workingday_no)

print("2-Sample T-Test for Working Day:")
print("Test Statistic:", t_stat)
print("P-Value:", p_value)

alpha = 0.05

if p_value < alpha:
    print("Conclusion: Reject the null hypothesis. There is a significant difference in the number of electric cycles rented between working days and non-working days.")
else:
    print("Conclusion: Fail to reject the null hypothesis. There is no significant difference in the number of electric cycles rented between working days and non-working days.")

"""Sample T-test to check if Working Day has an effect on the number of electric cycles rented.

After succesfully testing the hypothesis we conclude that There is no significant difference in the number of electric cycles rented between working days and non-working days

## **ANNOVA**

**ANNOVA to check if No. of cycles rented is similar or different in different 1. weather 2. season**

* Null Hypothesis (H0): The mean number of cycles rented is equal across all weather conditions or seasons.

* Alternative Hypothesis (H1): The mean number of cycles rented is not equal across all weather conditions or seasons.

* Significance Level (alpha): 0.05.
"""

f_stat_weather, p_value_weather = spy.f_oneway(df['count'][df['weather'] == 1],
                                               df['count'][df['weather'] == 2],
                                               df['count'][df['weather'] == 3],
                                               df['count'][df['weather'] == 4])

print("\nANOVA for Weather:")
print("F-Statistic:", f_stat_weather)
print("P-Value:", p_value_weather)

if p_value_weather < alpha:
    print("Conclusion: Reject the null hypothesis. The mean number of cycles rented is different across different weather conditions.")
else:
    print("Conclusion: Fail to reject the null hypothesis. The mean number of cycles rented is similar across different weather conditions.")

"""Anova results for Weather after testing the hypothesis we conclude that the mean number of cycles rented is different across different weather conditions."""

f_stat_season, p_value_season = spy.f_oneway(df['count'][df['season'] == 1],
                                             df['count'][df['season'] == 2],
                                             df['count'][df['season'] == 3],
                                             df['count'][df['season'] == 4])

print("\nANOVA for Season:")
print("F-Statistic:", f_stat_season)
print("P-Value:", p_value_season)

if p_value_season < alpha:
    print("Conclusion: Reject the null hypothesis. The mean number of cycles rented is different across different seasons.")
else:
    print("Conclusion: Fail to reject the null hypothesis. The mean number of cycles rented is similar across different seasons.")

"""## **Chi-square test**

**Chi-square test to check if Weather is dependent on the season**
* Null Hypothesis (H0): Weather and season are independent of each other.
* Alternative Hypothesis (H1): Weather and season are dependent on each other.
* Significance Level (alpha): 0.05.
"""

weather_season_cross = pd.crosstab(df['weather'], df['season'])

plt.figure(figsize=(8, 6))
sns.heatmap(weather_season_cross, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap of Weather and Season')
plt.xlabel('Season')
plt.ylabel('Weather')
plt.show()

chi2_stat, p_value_chi2, dof, expected = spy.chi2_contingency(weather_season_cross)

print("\nChi-Square Test for Weather and Season:")
print("Chi-Square Statistic:", chi2_stat)
print("P-Value:", p_value_chi2)

if p_value_chi2 < alpha:
    print("Conclusion: Reject the null hypothesis. Weather and season are dependent on each other.")
else:
    print("Conclusion: Fail to reject the null hypothesis. Weather and season are independent of each other.")

"""# **Conclusion**

## **Insights and recommendation's**

**Insights based on the analysis and hypothesis testing done**
> **1. Optimizing Service Availability :**

* Since there is no significant difference in rental counts between working days and non-working days, Yulu can consider adjusting its operational hours to better cater to customer demand patterns.

* For instance, if there are specific time slots during non-working days where demand is consistently high, Yulu could extend its operating hours during those periods to accommodate more riders.

> **2. Promotional Strategies :**

* Given the significant variation in rental counts across different weather conditions and seasons, Yulu can develop targeted promotional campaigns to incentivize ridership during less favorable conditions.

* For example, offering discounts or rewards for rides taken during rainy or colder seasons can encourage riders to choose Yulu's electric cycles over other modes of transportation.

> **3. Consistency in Rental Demand :**

* There is consistent demand for Yulu's shared electric cycles across both working and non-working days, indicating that the service is utilized regularly by users regardless of the day of the week.

> **4. Weather-Specific Service Enhancements :**

* Yulu can invest in weather-specific enhancements to improve the user experience and ensure rider safety during adverse weather conditions.
For instance, providing rain covers or waterproof accessories for electric cycles during monsoon seasons can make riding more comfortable and appealing to users.

> **5. Dependency between Weather and Season :**

* There is a dependency between weather conditions and seasons, suggesting that certain weather patterns are more prevalent during specific seasons.

* This highlights the importance of considering both weather and seasonality factors when planning operational activities and promotional strategies.

> **6. Seasonal Fleet Management :**

* Based on the dependency between weather and season, Yulu can adopt a dynamic fleet management approach to optimize resource allocation.
This could involve adjusting the distribution of electric cycles across different zones or neighborhoods based on anticipated changes in weather patterns and seasonal demand fluctuations.

> **7. Customer Communication and Education :**

* Yulu can proactively communicate with users about how weather conditions may impact their riding experience and provide tips for riding safely in different conditions.

* By educating users on the benefits of using Yulu's service regardless of weather or season, the company can foster greater loyalty and engagement among its customer base.

> **8. Collaboration with Local Authorities :**

* Yulu can collaborate with local authorities to implement infrastructure improvements that support safe and convenient riding experiences year-round.
This could include initiatives such as expanding dedicated bike lanes, installing sheltered bike parking facilities, or improving road conditions in areas with high ridership.

* By implementing these recommendations, Yulu can further enhance its service offerings, attract more users, and establish itself as a reliable and sustainable micro-mobility solution in the Indian market.

> **9. Effect of Working Day on Rental Counts :**

* The 2-sample t-test results suggest that there is no significant difference in the number of electric cycles rented between working days and non-working days.

* This implies that Yulu's service is utilized consistently across both working and non-working days.

* Recommendation: Yulu's R&D team should focus on maintaining a consistent level of service availability and promotion strategies across all days of the week.

> **10. Effect of Weather and Season on Rental Counts :**

* The ANOVA tests indicate that the mean number of electric cycles rented varies significantly across different weather conditions and seasons.
This suggests that weather and seasonal factors play a role in influencing customer demand.

* Recommendation: Yulu should adapt its operations and marketing strategies based on weather forecasts and seasonal trends. For instance, offering promotions during favorable weather conditions or seasonal events can help boost ridership.

> **11. Dependency between Weather and Season :**

* The Chi-square test results show that weather and season are dependent on each other.

* This implies that certain weather conditions are more prevalent during specific seasons.

* Recommendation: Yulu should consider the interplay between weather and season when planning operational activities, such as maintenance schedules or fleet adjustments.

## **Final Analysis**

**Overall Insights :**

* The data-driven analysis provides valuable insights into the factors influencing the demand for Yulu's shared electric cycles.
Understanding these factors can help Yulu optimize its operations, enhance user experience, and drive business growth.

* The main profit that lie's for yulu is in accomodating close to perfect number of bikes on specific location's according to predicted need for user's such that the whole fleet is used efficiently and the potential is not wasted.

* Yulu's R&D team should continue monitoring and analyzing rental patterns to identify emerging trends and opportunities for improvement.

**Future Directions :**

* Further analysis could explore additional variables such as time of day, geographical location, or promotional activities to gain deeper insights into rental patterns.

* Yulu could also consider implementing predictive analytics models to forecast demand and optimize resource allocation.

* Predictive analaytics model are a way to sustain and make the best out of yulu's bike fleet rather than increasing the fleet size they could first find out if they can optimize and make user's availabillity for bikes in heavy usage areas.
"""