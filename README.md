# Data Science Salary Estimator: Project Overview
•	Created a tool that estimates data science salaries (MAE - $ 11K) to help data scientists negotiate their income when they get a job.

•	Scraped over 1000 job descriptions from glassdoor using python and selenuim.

•	Engineered features from the text of each job description to quantify the value companies put on Python, SQL, R, Excel , AWS and Spark.

•	Optimized Linear, Lasso and Random Forest Regressors using GridSearchCV to reach out the best model.

•	Built a client facing API using flask

## Code and Resources Used

**Python Version**: 3.11
**Packages Used**:Pandas, Numpy, Sklearn, Seaborn, Selenium, Flask, Json, Pickle\
**For Web Framework Requirements**:`pip install -r requirements.txt`\
**Scrapper Github**: https://github.com/arapfaik/scraping-glassdoor-selenium \
**Scrapper Article**: https://mersakarya.medium.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905

## Web Scrapping

Tweaked the web scrapper repo to scrape 1000 job postings from glassdoor.com. With each job, we got the following:

+ Job title
+ Salary Estimate
+ Job Description
+ Rating
+ Company
+ Location
+ Company Headquarters
+ Company Size
+ Company Founded Date
+ Type of Ownership
+ Industry
+ Sector
+ Revenue
+ Competitors
  
## Data Cleaning

After scraping the data. It was needed to be cleaned to be usable for our model. The following changes were made:

+ Parsed numeric salary data.
+ Made columns for employer-provided salary and hourly wages.
+ Removed roes without salary.
+ Parsed rating out of company text.
+ Added a column if the job was at the company's headquarters.
+ Transformed founded date to the age of the company.
+ Made columns for different skills listed in the job description:
    + Python
    + R
    + SQL
    + AWS
    + Spark
    + Excel
+ Column for simplified job title and seniority
+ Column for job description length

## Exploratory Data Analysis
After looking at the distribution of the data and the value counts for various categorical variables. Below are few highlights from the pivot tables.

![alt text](https://github.com/sarthakking5/Data-Science-Salary-Estimator/blob/main/Images/Screenshot%202023-06-15%20221532.png)       ![alt text](https://github.com/sarthakking5/Data-Science-Salary-Estimator/blob/main/Images/download%20(3).png)

 ![alt text](https://github.com/sarthakking5/Data-Science-Salary-Estimator/blob/main/Images/download.png) 

## Model Building

Firstly, the categorical variables were transformed into dummy variables, and the data was then split into training and testing sets with a test size of 20%.

The data was trained and tested using three different models and then were further evaluated using Mean Absolute Error. MAE was chosen as it is relatively easy to interpret and outliers weren't particularly bad for this type of model.

The three different models were as follows:
  + **Multiple Linear Regression** - Baseline for the model
  + **Lasso Regression** - Because of the sparse data from the many categorical variables, a normalized regression like lasso was found to be effective.
  + **Random Forest** - With sparsity associated with the data, this model was also found to be a good fit.

## Model Performance

The Random Forest model far outperformed the other approaches on the test and validation sets.
  + **Random Forest**: MAE = 11.90
  + **Linear Regression** : MAE = 19.59
  + **Ridge Regression** : MAE = 19.69

## Productionization

In this step, a Flask API endpoint was built and hosted on a local webserver. The API endpoint takes in a request with a list of values from a job listing and returns an estimated salary.
