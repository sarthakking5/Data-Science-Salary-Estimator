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

![alt text](https://github.com/sarthakking5/Data-Science-Salary-Estimator/blob/main/Images/Screenshot%202023-06-15%20221532.png)  ![alt text](https://github.com/sarthakking5/Data-Science-Salary-Estimator/blob/main/Images/download%20(3).png)
